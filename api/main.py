from typing import Union

from fastapi import FastAPI
import utils1, utils2, utils3

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/{conj}/{sent}")
def generate_1(sent: str, conj: str):
    res = []
    if conj == '그런데':
        for func in utils1.utils1_list:
            res.append(func(sent)['choices'][0]['message']['content'])
    if conj =='그러나':
        for func in utils2.utils2_list:
            res.append(func(sent)['choices'][0]['message']['content'])
    if conj =='따라서':
        for func in utils3.utils3_list:
            res.append(func(sent)['choices'][0]['message']['content'])
    return {"response": res}
