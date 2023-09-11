# Sentence_Pred

## TODO
- [ ] Data pre-processing
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