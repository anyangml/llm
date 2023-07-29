import gradio as gr
from util import OCRhelper


class Gradio:

    ocr = OCRhelper()

    def launch(self):
        demo = gr.Interface(
            fn=Gradio.ocr.pipeline,
            inputs=[
                gr.inputs.Image(source="upload", type="pil", label="Latex Image"),
                gr.inputs.Image(source="upload", type="pil", label="Document Image"),
            ],
            outputs=["text"],
            cache_examples=False,
        )
        demo.launch()


if __name__ == "__main__":
    Gradio().launch()
