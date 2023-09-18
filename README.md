# Sentence_Pred

## TODO
- [X] Data pre-processing
- [ ] KoGPT-2 finetuning





## Main Task
Our Main Task is to predict Next Sentence via previous sentence and Conjunctions.
According to the logic from Rhetorike, sentence could be distinguished into finite amount of structures.
Assume that the user gives the first sentence and choose the conjunction they want to use, our task is to predict the next sentence that smoothly connects the given String. We tried to address the problem by building a model for each structures, which could generate plausible sentences.

## Model explanation

### input Notation
Each sentence structure has two models. For better explanation, we assume a structure which shows the general case of the sentence structures
```
<A> <B> <CONJUNCTION> <B> <C>
```

> Note that the following example is just one of the examples from the sentence structure

+ `<A> <B>` is going to be the `<prev_sentence>`
+ `<CONJUNCTION>` is going to be the `<CONJ>` token

### specific model task

1. `<B>` prediction model
   - Input: `<prev_sentence><CONJ>`
   - Output: `<B>`

2. `<C>` prediction model
   - Input: `<prev_sentence><CONJ><B>`
   - Output: `<C>`

By concatenating the output from the first model, we could get the input for the second model, and after the second model, we concatenate `<B>` and `<C>` which is the output sentence.

### Pretraining & Fine-tuning

TODO application



### 서버에서 돌리는 방법

1. github link 서버에 연결시키기
```
git remote add origin https://github.com/junseokkim00/Sentence_Pred.git
```
2. git pull로 가져오기
```
git pull
```
3. conda 이용해서 가상환경 만들기
+ 만일 python이 없을 경우, `conda install ipykernel`하기
+ python 잡히면, `pip install -r requirements.txt` 돌리기

4. 학습시키는 방법

**KoGPT-2 (skt)**
```
cd src
python3 train.py
```

**KoGPT-3 (kakaobrain)**
```
cd src
python3 train2.py
```