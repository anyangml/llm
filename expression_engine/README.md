# Expression Engine

This tool uses ORC algorithms to extract raw text from images (latex and plain text) and standarize the text into structed data format (yaml). The standarized output can be used by pydantic to create python objects directly.

![image](https://github.com/anyangml/llm/assets/137014849/21e5dc97-a9f9-4121-b123-819b6ad4e11f)

### Tools used
- Pic2tex
- Pic2text
- gradio
- langchain
- openai api
  
### How to Use

1. clone the repo
   
   `git clone https://github.com/anyangml/llm.git`

2. install dependencies

    `cd llm/expression_engine`

    `poetry shell`

    `poetry install`

3. launch

    `python expression_engine/main.py`
   
