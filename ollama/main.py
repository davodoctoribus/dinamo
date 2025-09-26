from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.post('/generate')
def generate(prompt: str):
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response["message"]["content"]}

if __name__ == "__main__":
    app.run(debug=True)