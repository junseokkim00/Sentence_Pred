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


if __name__ == "__main__":
    wandb.init()
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", default="skt/kogpt2-base-v2", type=str)
    parser.add_argument("--data_dir", default="./data", type=str)
    parser.add_argument("--batch_size", default=32, type=int)
    parser.add_argument("--epochs", default=10, type=int)
    parser.add_argument("--lr", default=2e-5, type=float)
    parser.add_argument("--warmup_steps", default=200, type=int)
    args = parser.parse_args()
    wandb.config.update(args)

    BASE_DIR = os.getcwd()
    DATA_DIR = os.path.join(BASE_DIR, args.data_dir)

    tokenizer = PreTrainedTokenizerFast.from_pretrained(args.model_name, bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')
    # file_path = os.path.join(DATA_DIR, "final_train.csv")

    train_dataloader = GPTDataLoader(tokenizer=tokenizer, file_path=os.path.join(DATA_DIR, "final_train.csv"), batch_size=args.batch_size)

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
            # model.zero_grad()
            avg_loss.backward()
            optimizer.step()
            scheduler.step()
        wandb.log({
            "Loss": loss
        })
        print(f"epoch {epoch} loss {avg_loss:0.2f}")

        


        gen = generate("나는 밥을 먹었다. 그런데", tokenizer, model, 1)
        print(f"{gen[0]}")

        if avg_loss < min_loss:
            min_loss = avg_loss
            model.save_pretrained("./best_model_newVersion")
    print("Training Done")
