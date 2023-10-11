# HuggingFace

This repo contains notes and experiment code for learning purpose. The following core modules are covered in this repo:
    
- [HuggingFace](#huggingface)
  - [Transformers](#transformers)
  - [Datasets](#datasets)
- [Resource](#resource)


## Transformers
The `Transformers` module is a high-level api that provides access to many pre-trained models to perform various downstream tasks including _NLP_, _CV_, _Generation_, etc. It does not only support inference, but also model fine-tuning. 

<details open>
  <summary> Pipleline </summary>
  
  The [`pipleline`](https://huggingface.co/docs/transformers/main_classes/pipelines) function is used to instantiate models for inference with a sepcific task, available tasks are listed in [_SUPPORTED_TASKS_](https://github.com/huggingface/transformers/blob/fc63914399b6f60512c720959f9182b02ae4a45c/src/transformers/pipelines/__init__.py#L155C1-L155C16). For example, to perform a sentiment analysis task, simply do the following:
  ```
  from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")
  ```
A model can be specified to overwrite the default model.

</details>

<details open>
  <summary> Customize NLP Pipleline </summary>

  A pipeline for NLP tasks typically involes 3 core components: _tokenizer_, _model_, _post-processing_.
  Each model is pre-trained with a tokenizer, so they are used in pairs. The tokenizer is used to transform raw text inputs into model understandable tensors (tokenization, encoding, embedding).

</details>

<details open>
  <summary> Model Fine-tuning </summary>

  To fine-tune a model, the first step is to prepare the training data. There are many datasets available in the [`datasets`](https://huggingface.co/docs/datasets/load_hub) module. To batch process the raw text data, we can use the `map` method thanks to _Apache Arrow_.

  ```
  def tokenizer_func(data):
    return tokenizer(...)

processed_data = raw_data.map(tokenizer_func, batched=True, num_proc=...)
  ```
  The function that is responsible for putting together samples inside a batch is called a _collate_ function. It can be used to pad samples within the same batch to the same length using _Dynamic Padding_.
  Once the data is ready for training, we can use the high-level api _Trainer_ to fine-tune the model.

  ```
  trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)
trainer.train()
```
To understand how the trainer works, check out [this](https://huggingface.co/learn/nlp-course/chapter3/4?fw=pt).
</details>

## Datasets
# Resource
- [NLPCourse](https://huggingface.co/learn/nlp-course/chapter0/1?fw=pt)
- [PPO Reinforcement Learning](https://huggingface.co/learn/deep-rl-course/unit0/introduction)
- MyUnderStandingOfTransformer
  - different models
  - tokenizers
  - padding? batch with different length
  - evaluation metrics
  - peft