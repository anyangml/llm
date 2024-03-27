import gradio as gr
from util import OCRhelper

ocr = OCRhelper()
demo = gr.Interface(
    fn=ocr.pipeline,
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

if __name__ == "__main__":
    demo.launch()
