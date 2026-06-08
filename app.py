import gradio as gr
from markitdown import MarkItDown

md = MarkItDown()


def convert_to_md(file):
    if file is None:
        return "Please drag and drop a file."
    try:
        result = md.convert(file.name)
        return result.text_content
    except Exception as e:
        return f"Error converting file: {str(e)}"


demo = gr.Interface(
    fn=convert_to_md,
    inputs=gr.File(label="Drag & Drop your file here (PDF, DOCX, etc.)"),
    outputs=gr.Textbox(label="Markdown Output"),
    title="MarkItDown Converter",
)

# Launch the app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)