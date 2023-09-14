import os
import argparse
import torch
from tqdm import tqdm
from transformers import (
    GPT2LMHeadModel,
    AutoTokenizer,
    AdamW,
    get_linear_schedule_with_warmup
)

from dataloader import GPTDataLoader
from utils import generate

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", default="skt/kogpt2-base-v2", type=str)
    parser.add_argument("--data_dir", default="./data", type=str)
    parser.add_argument("--batch_size", default=32, type=int)
    parser.add_argument("--epochs", default=10, type=int)
    parser.add_argument("--lr", default=2e-5, type=float)
    parser.add_argument("--warmup_steps", default=200, type=int)
    args = parser.parse_args()

    BASE_DIR = os.getcwd()
    DATA_DIR = os.path.join(BASE_DIR, args.data_dir)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    tokenizer.add_special_tokens({"pad_token": "<pad>"})

    train_dataloader = GPTDataLoader(tokenizer=tokenizer, file_path=os.path.join(DATA_DIR, "train.csv"), batch_size=args.batch_size)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GPT2LMHeadModel.from_pretrained(args.model_name).to(device)
    model.train()

    optimizer = AdamW(model.parameters(), lr=args.lr)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=args.warmup_steps, num_training_steps=-1
    )

    min_loss = int(1e9)

    for epoch in range(args.epochs):
        print(f"Training epoch {epoch}")
        for input_text in tqdm(train_dataloader):
            input_tensor = input_text.to(device)
            outputs = model(input_tensor, labels=input_tensor)
            loss = outputs[0]

            optimizer.zero_grad()
            model.zero_grad()
            loss.backward()
            optimizer.step()
            scheduler.step()
        
        print(f"epoch {epoch} loss {outputs[0].item():0.2f}")

        gen = generate("나는 밥을 먹었다. 그런데", tokenizer, model, 1)
        print(f"{gen[0]}")

        if outputs[0].item() < min_loss:
            min_loss = outputs[0].item()
            model.save_pretrained("./best_model")
    print("Training")
