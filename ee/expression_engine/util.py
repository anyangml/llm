from typing import Dict
from typing import Optional
from pix2tex.cli import LatexOCR
from pix2text import Pix2Text
from chain import Chain
import re

class OCRhelper:
    """
    A helper class to use Pix2Text and LatexOCR.
    """

    latex_model = LatexOCR()
    doc_model = Pix2Text()

    def pipeline(self, latex_img, doc_img1, doc_img2 = None):
        """
        This is this main function used by Gradio to get the final output

        Parameters:
        ----------
        latex_img : PIL
            image of the latex equation

        doc_img1 : PIL
            image of the documentation

        doc_img1 : Optional[PIL]
            image of the documentation continue, default to None

        Returns:
        --------
        yaml : str
            The yaml output of the input.
        """

        # extracting info from latex and doc images
        latex = self.latex_model(latex_img)
        raw_doc = self.doc_model(doc_img1)
        parsed_doc = OCRhelper.parse_doc(raw_doc)
        if doc_img2 is not None:
            raw_doc = self.doc_model(doc_img2)
            parsed_doc += OCRhelper.parse_doc(raw_doc)
        print("Before: \n")
        print(latex)
        print("After: \n")

        latex = latex.replace("\\bigl", "")
        latex = latex.replace("\\bigr", "")
        print(latex)

        ocr_output = (
            f"{OCRhelper.curly_bracket(latex)} \n {OCRhelper.curly_bracket(parsed_doc)}"
        )
        # creating few shot prompt with ocr_output
        chain = Chain()
        prompt = chain.create_prompt(ocr_output)

        # get yaml output
        yaml = chain.get_yaml(prompt)
        all_latex = re.findall(r"(?<=latex:)[\s\S]?\s\S*\b[\s\S]*?(?=\n)", yaml)
        all_latex = [x.strip() for x in all_latex]

        def latex_render(all_latex):
            final_str = ""
            for latex in all_latex:
                final_str += "## $" + latex + "$  </br>"
            return rf"{final_str}"

        final_markdown = latex_render(all_latex)
        # print(final_markdown)
        return yaml, final_markdown

    @staticmethod
    def parse_doc(raw_doc: Dict) -> str:
        """
        Parses a raw document generated by Pix2Text into a list of sentences.

        Parameter
        ---------
        raw_doc : Dict
            The output dictionary from Pix2Text to be parsed.

        Returns
        -------
        parsed : str
            A string of sentences.
        """
        parsed = []
        line_number = 0
        temp = ""
        for output in raw_doc:
            if output["type"] == "text":
                if output["line_number"] == line_number:
                    temp += " " + output["text"]
                else:
                    parsed.append(temp)
                    temp = output["text"]
                    line_number += 1
        parsed.append(temp)
        return " \n ".join(parsed)

    @staticmethod
    def curly_bracket(text: str) -> str:
        """
        Wrap curly_brackets with another layer of curly_brackets.
        This is to fix parsing issue in LangCahin FewShotPromptTemplate.

        Parameters
        ----------
        text : str
            The text to be wrapped.

        Returns
        -------
        text : str
            The wrapped text.
        """
        text = text.replace("}", "}}")
        text = text.replace("{", "{{")
        return text

    @staticmethod
    def undo_curly_bracket(text: str) -> str:
        """
        Unwrap curly_brackets to single layer of curly_brackets.

        Parameters
        ----------
        text : str
            The text to be unwrapped.

        Returns
        -------
        text : str
            The nwrapped text.
        """
        text = text.replace("}}", "}")
        text = text.replace("{{", "{")
        return text
