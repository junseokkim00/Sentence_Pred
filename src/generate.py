from transformers import GPT2LMHeadModel, AutoTokenizer
import torch
import pandas as pd
from utils import generate
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_text", default="철수는 영희를 좋아한다. 그런데 ", type=str)
    parser.add_argument("--num_of_generate", default=4, type=int)
    
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GPT2LMHeadModel.from_pretrained("./best_model_theRealNewVersion").to(device)
    tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")

    gen_sentences = generate(input_text=args.input_text,tokenizer=tokenizer, model=model, num=args.num_of_generate)
    for text in gen_sentences:
        print(text)