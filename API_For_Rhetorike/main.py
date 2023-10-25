from typing import Union

from fastapi import FastAPI

from sen_gen_util import send_message

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/그런데/{num}")
def generate_1(num: int):
    res = []
    for _ in range(num):
        res.append(send_message(""))
    return {"response": res}
