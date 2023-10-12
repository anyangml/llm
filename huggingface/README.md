# HuggingFace

This repo contains notes and experiment code for learning purpose. The following core modules are covered in this repo:
    
- [HuggingFace](#huggingface)
  - [Transformers](#transformers)
  - [Datasets](#datasets)
  - [Parameter Efficient Fine-tuning (PEFT)](#parameter-efficient-fine-tuning-peft)
- [Resource](#resource)


## Transformers
The `Transformers` library is a high-level api that provides access to many pre-trained models to perform various downstream tasks including _NLP_, _CV_, _Generation_, etc. It does not only support inference, but also model fine-tuning. 

<details closed>
  <summary> Pipleline </summary>
  
  The [`pipleline`](https://huggingface.co/docs/transformers/main_classes/pipelines) function is used to instantiate models for inference with a sepcific task, available tasks are listed in [_SUPPORTED_TASKS_](https://github.com/huggingface/transformers/blob/fc63914399b6f60512c720959f9182b02ae4a45c/src/transformers/pipelines/__init__.py#L155C1-L155C16). For example, to perform a sentiment analysis task, simply do the following:
  ```
  from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")
  ```
A model can be specified to overwrite the default model.

</details>

<details closed>
  <summary> Customize NLP Pipleline </summary>

  A pipeline for NLP tasks typically involes 3 core components: _tokenizer_, _model_, _post-processing_.
  Each model is pre-trained with a tokenizer, so they are used in pairs. The tokenizer is used to transform raw text inputs into model understandable tensors (tokenization, encoding, embedding).

</details>

<details closed>
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

<details closed>
  <summary> Load/Buid Dataset </summary>

The `Datasets` library allows easy access to collections of datasests for model training across many tasks. We can check out a dataset without downloading it using the _load_dataset_builder_ function:

```
from datasets import load_dataset_builder

ds_builder = load_dataset_builder("rotten_tomatoes")
ds_builder.info.description
ds_builder.info.features
```

and we can download the dataset using the _load_dataset_ function:

```
from datasets import load_dataset

dataset = load_dataset("rotten_tomatoes", split="train")
```
Since datasets are _Apache Arrow_ objects, we can use the _map_ method mentioned in the `Transformers` section to perform bulk processing.

To build a customized dataset, checkout [this](https://huggingface.co/docs/datasets/create_dataset).

</details>

## Parameter Efficient Fine-tuning (PEFT)

<details closed>
  <summary> Low-Rank Adaptation (LORA) </summary>

  LORA is probably the most frequently used PEFT technique. It does not change the original model parameters, instead it adds a LORA adapter on top of the parameter matrix to represent the changes. The adapter uses the product of two lower rank matrices as the tunable parameter matrix. We can use _get_peft_model_ function to add LORA adapters to the original model with a _LoraConfig_, and simply use _Trainer_ to train the lora model:

  ```
  from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    r=32, # Rank
    lora_alpha=32,
    target_modules=["q", "v"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.SEQ_2_SEQ_LM # FLAN-T5
)

peft_model = get_peft_model(original_model, 
                            lora_config)

peft_trainer = Trainer(
    model=peft_model,
    args=peft_training_args,
    train_dataset=tokenized_datasets["train"],
)

peft_trainer.train()
  ```
</details>


# Resource
- [NLPCourse](https://huggingface.co/learn/nlp-course/chapter0/1?fw=pt)
- [PPO Reinforcement Learning](https://huggingface.co/learn/deep-rl-course/unit0/introduction)
- [MyUnderStandingOfTransformer](https://anyangpeng.notion.site/anyangpeng/NLP-Notes-f337664ce2444b6c8cef8abb84a24528)
