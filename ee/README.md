# Expression Engine

This tool uses ORC algorithms to extract raw text from images (latex and plain text) and standarize the text into structed data format (yaml). The standarized output can be used by pydantic to create python objects directly.

<img width="1509" alt="Screenshot 2023-08-02 at 5 42 23 PM" src="https://github.com/christwy0614/NLP_team_project/assets/66216181/1b4bcf7f-7579-49ea-abd6-9ca86ed3a136">

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

    `cd llm/ee`

    `poetry shell`

    `poetry install`

3. launch

    `python expression_engine/main.py`
   