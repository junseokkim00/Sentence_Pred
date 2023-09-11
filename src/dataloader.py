import pandas as pd
from torch.utils.data import Dataset, DataLoader

"""
Data 생김새

input: <첫 문장> <접속사>
output: <뒷 문장>

"""

class GPTDataset(Dataset):
    def __init__(self, tokenizer, file_path):
        data = pd.read_csv(file_path)
        concats = [
            prev +"|"+_next for prev, _next in zip(data["prev"], data["next"])
        ]
        self.item = tokenizer(concats,return_tensors='pt',padding="max_length",truncation=True,max_length=32)["input_ids"]
        self.length = len(concats)
    
    def __getitem__(self, i):
        return self.item[i]
    
    def __len__(self):
        return self.length
    


def GPTDataLoader(tokenizer, file_path, batch_size):
    data = GPTDataset(tokenizer=tokenizer, file_path=file_path)
    return DataLoader(data, batch_size=batch_size)