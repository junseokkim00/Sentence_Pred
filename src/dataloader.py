import pandas as pd
from torch.utils.data import Dataset, DataLoader
import numpy as np
import torch

"""
Data 생김새

input: <첫 문장> <접속사>
output: <뒷 문장>
"""
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
class GPTDataset(Dataset):
    def __init__(self, tokenizer, file_path):
        self.data = pd.read_csv(file_path)[['prev', 'next']]
        self.length = self.data.shape[0]
        self.tokenizer = tokenizer
    
    def __getitem__(self, i):
        prev, _next = self.data.iloc[i]['prev'], self.data.iloc[i]['next']
        prev = self.tokenizer.encode(prev)
        _next = self.tokenizer.encode(_next)
        # inputs_id = prev + [self.tokenizer.bos_token_id] + _next
        inputs_id = prev + _next
        while len(inputs_id) < 50:
            inputs_id.append(self.tokenizer.pad_token_id)
        
        outputs_id = [self.tokenizer.mask_token_id,] * (len(prev)-1) + _next + [self.tokenizer.eos_token_id]
        while len(outputs_id) < 50:
            outputs_id.append(self.tokenizer.pad_token_id)
        mask = [0] * len(prev) + [1] * len(_next) + [0] * (50 - len(prev) - len(_next))
        inputs_id = torch.LongTensor(inputs_id).to(device)
        outputs_id = torch.LongTensor(outputs_id).to(device)
        mask = torch.LongTensor(mask).to(device)
        return inputs_id, mask, outputs_id
    
    def __len__(self):
        return self.length

# def collate_batch(batch):
#     data = [item[0] for item in batch]
#     mask = [item[1] for item in batch]
#     label = [item[2] for item in batch]
#     return torch.LongTensor(data), torch.LongTensor(mask), torch.LongTensor(label)
    


def GPTDataLoader(tokenizer, file_path, batch_size):
    data = GPTDataset(tokenizer=tokenizer, file_path=file_path)
    return DataLoader(data, batch_size=batch_size)