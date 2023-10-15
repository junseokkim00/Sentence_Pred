from transformers import GPT2LMHeadModel, AutoTokenizer
import torch
import pandas as pd
import argparse
from collections import defaultdict
from tqdm import tqdm


def generate(input_text):
    generated_sentence=[]
    for _ in range(4):
        token_ids = tokenizer(input_text, return_tensors='pt')['input_ids'].to(device)

        gen_ids = model.generate(token_ids,
                                max_length=32,
                                repetition_penalty=2.0,
                                pad_token_id = tokenizer.pad_token_id,
                                eos_token_id = tokenizer.eos_token_id,
                                bos_token_id = tokenizer.bos_token_id,
                                use_cache=True,
                                do_sample=True
                                )
        sentence = tokenizer.decode(gen_ids[0])
        if '</s>' in sentence:
            sentence = sentence[:sentence.index('</s>')]
        generated_sentence.append(sentence)
        
    return generated_sentence

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", default="./sample.txt", type=str)
    parser.add_argument("--num_of_generate", default=4, type=int)
    
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GPT2LMHeadModel.from_pretrained("./best_model_theRealNewVersion").to(device)
    tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2",bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')
    # final = defaultdict(list)
    final = []
    with open(args.file_path,'r') as f:
        final = f.readlines()
        # for line in tqdm(f):
        #     # final[line] = generate(line)
        #     print(line.strip())
    final = [line.strip() for line in final]
    with open('./report.txt', 'w') as f:
        for line in tqdm(final):
            f.write(line+'\n')
            generateList = generate(line)
            for idx, candidate in enumerate(generateList):
                f.write(f'{idx+1}: {candidate}\n')

   
