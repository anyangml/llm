import gradio as gr
from util import OCRhelper


class Gradio:

    ocr = OCRhelper()

    def launch(self):


        demo = gr.Interface(
            fn=Gradio.ocr.pipeline,
            inputs=[
                gr.inputs.Image(source="upload", type="pil", label="Latex Image"),
                gr.inputs.Image(source="upload", type="pil", label="Document Image 1"),
                gr.inputs.Image(source="upload", type="pil", label="Document Image 2"),
            ],
            outputs=[
                gr.outputs.Textbox(type="text", label="YAML config"),
                gr.Markdown(label="Output latex")
            ],
            cache_examples=False,
        )
        demo.launch()


if __name__ == "__main__":
    Gradio().launch()
