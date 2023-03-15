import gradio as gr
import tiktoken

encodings = tiktoken.list_encoding_names()
encodings.reverse()


def calc(input: str, encoding: str) -> int:
    tokens = tiktoken.get_encoding(encoding).encode(input)
    return len(tokens)


gr.Interface(
    calc,
    inputs=[
        gr.Text(label="Input", lines=6, placeholder="Enter text here..."),
        gr.Dropdown(
            label="Encoding",
            choices=encodings,
            value="cl100k_base",
            info="The encoding to use. (GPT-3.5 and GPT-4 use cl100k_base as their encoding.)",
        ),
    ],
    outputs=gr.Number(label="Output"),
    title="Tiktoken Calculator",
    allow_flagging="never",
).launch()
