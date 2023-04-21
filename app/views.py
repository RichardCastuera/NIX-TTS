from distutils.log import error
from app import app
import io
from flask import render_template, request, Response, stream_with_context
from app.tts import synthesizer

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/call/NIX", methods = ["POST"])
def call_NIX():
    if(request.form["text"]):
        text = request.form["text"]
        def generate():
            outputs = synthesizer.tts(text)
            out = io.BytesIO()
            synthesizer.save_wav(outputs, out)
            out.seek(0)
            data = out.read(1024)
            while data:
                yield data
                data = out.read(1024)
        return Response(stream_with_context(generate()), mimetype="audio/wav")
    else:
        return {"error": "Please provide the text"}, 400
    