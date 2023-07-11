import gradio as gr
from flask import Flask

app = Flask(__name__)

def greet(name):
    return f"Hello, {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

@app.route("/")
def gradio_interface():
    return iface.launch(share=False)

if __name__ == '__main__':
    app.run()
