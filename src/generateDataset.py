import pandas as pd

file_path="./input.txt"

data_list = []

with open(file_path) as file:
    data_list = file.readlines()
# 문장을 하나씩 받음
data_list = [i.rstrip() for i in data_list]
inputs = []
output = []
for txt in data_list:
    txt_list = txt.split()
    conjunction_idx = txt_list.index('그런데')
    inputs.append(' '.join(txt_list[:conjunction_idx+1]))
    output.append(' '.join(txt_list[conjunction_idx+1:]))

d = {'prev': inputs, 'next': output}
df = pd.DataFrame(data=d)
df.to_csv('train.csv')