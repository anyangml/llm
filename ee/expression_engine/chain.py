from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from example import examples
import openai


class Chain:

    example = examples

    example_template = """
    User: {latex}
    AI: {yaml}
    """
    prefix = """Pretend you are a software engineer, and you are implementing calculators defined in latex format with raw text 
    documentations describing the parameter used in the calculator. For each term present in the latex equation, a parameter need to be
    defined according to the corresponding raw text description and it must have a human readable varialbe name that is used in the input field
    and the symbol field. You need to reformat the information into a yaml format, below is an example:
    """

    suffix = """
    User: {latex}
    AI: """

    def create_prompt(self, input: str) -> str:
        """
        This method creates a prompt with examples defined in the examples.py file.
        The prompt is used to transform the OCR outputs (raw string: latex + doc)
        into the expected yaml output for expression_engine

        Parameters:
        -----------
        input : str
            The OCR output string

        Returns:
        --------
        prompt : str
            The final prompt with few shot learning.
        """
        example_prompt = PromptTemplate(
            input_variables=["latex", "yaml"], template=self.example_template
        )

        few_shot_prompt_template = FewShotPromptTemplate(
            examples=self.example,
            example_prompt=example_prompt,
            prefix=self.prefix,
            suffix=self.suffix,
            input_variables=["latex"],
            example_separator="\n\n",
        )
        prompt = few_shot_prompt_template.format(latex=input)
        return prompt

    def get_yaml(self, prompt: str, model: str = "gpt-3.5-turbo") -> str:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]
