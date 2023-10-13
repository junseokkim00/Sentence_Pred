import os
import argparse
import torch
from tqdm import tqdm
from transformers import (
    GPT2LMHeadModel,
    PreTrainedTokenizerFast,
    AdamW,
    get_linear_schedule_with_warmup
)

from dataloader import GPTDataLoader
from utils import generate

import wandb
import pandas as pd

if __name__ == "__main__":
    wandb.init()
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", default="skt/kogpt2-base-v2", type=str)
    parser.add_argument("--data_dir", default="./data", type=str)
    parser.add_argument("--batch_size", default=32, type=int)
    parser.add_argument("--epochs", default=50, type=int)
    parser.add_argument("--lr", default=2e-5, type=float)
    parser.add_argument("--warmup_steps", default=200, type=int)
    args = parser.parse_args()
    wandb.config.update(args)

    BASE_DIR = os.getcwd()
    DATA_DIR = os.path.join(BASE_DIR, args.data_dir)

    tokenizer = PreTrainedTokenizerFast.from_pretrained(args.model_name, bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')
    file_path = os.path.join(DATA_DIR, "final_train.csv")

    # make train and val dataloader
    data = pd.read_csv(file_path)[['prev', 'next']]
    data = data.sample(frac=1).reset_index(drop=True)
    num = int(len(data) * 0.8)
    train_data, val_data = data[:num], data[:num]

    train_dataloader = GPTDataLoader(tokenizer=tokenizer,data=train_data, batch_size=args.batch_size)
    val_dataloader = GPTDataLoader(tokenizer=tokenizer, data=val_data, batch_size=args.batch_size)



    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GPT2LMHeadModel.from_pretrained(args.model_name).to(device)
    wandb.watch(model)
    model.train()

    optimizer = AdamW(model.parameters(), lr=args.lr)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=args.warmup_steps, num_training_steps=-1
    )
    criterion = torch.nn.CrossEntropyLoss(reduction="none")
    min_loss = int(1e9)
    Sneg = -1e18
    for epoch in range(args.epochs):
        print(f"Training epoch {epoch}")
        for samples in tqdm(train_dataloader):
            optimizer.zero_grad()
            input_ids, mask, label = samples
            out = model(input_ids)
            out = out.logits
            mask_3d = mask.unsqueeze(dim=2).repeat_interleave(repeats=out.shape[2], dim=2)
            mask_out = torch.where(mask_3d == 1, out, Sneg * torch.ones_like(out))
            loss = criterion(mask_out.transpose(2, 1), label)
            avg_loss = loss.sum() / mask.sum()
            # out = model(input_ids, labels=label)
            # loss = out[0]
            avg_loss.backward()
            # loss.backward()
            optimizer.step()
            scheduler.step()
    
        print("Validating...")
        cnt=0
        with torch.no_grad():
            test_loss=0
            for samples in tqdm(val_dataloader):
                cnt+=1
                input_ids, mask, label = samples
                out = model(input_ids)
                out = out.logits
                mask_3d = mask.unsqueeze(dim=2).repeat_interleave(repeats=out.shape[2], dim=2)
                mask_out = torch.where(mask_3d == 1, out, Sneg * torch.ones_like(out))
                loss = criterion(mask_out.transpose(2, 1), label)
                avg_loss = loss.sum() / mask.sum()
                # out = model(input_ids, labels=label)
                # loss = out[0]
                test_loss+=avg_loss
                # test_loss+=loss
            test_loss/=cnt
            wandb.log({
                "Train Loss": avg_loss,
                "# of Epoch": epoch,
                "Valdiation Loss": test_loss
            })
            print(f"epoch: {epoch}/{args.epochs} loss: {test_loss:0.2f}")
            gen = generate("나는 밥을 먹었다. 그런데", tokenizer, model, 1)
            print("Input: 나는 밥을 먹었다. 그런데")
            print(f"Output: {gen[0]}")

            if test_loss < min_loss:
                min_loss = test_loss
                model.save_pretrained("./best_model_theRealNewVersion")
    print("Training Done")
