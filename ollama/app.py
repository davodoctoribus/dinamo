from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.post('/generate')
def generate():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Missing prompt"}), 400

        prompt = data["prompt"]

        response = ollama.chat(
            model="deepseek-v3.1:671b-cloud",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.get("message", {}).get("content", "")

        return jsonify({"response": content})
    except Exception as e:
        print("Erro no /generate:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)