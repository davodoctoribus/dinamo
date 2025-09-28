from flask import Flask, request, jsonify
import ollama
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

prompt = f"""
        Você é um tutor de cálculo focado em integrais simples.
        Sua função é explicar de forma clara uma dúvida específica de integral, e não a solução inteira

        Regras obrigatórias:
        - Explique de forma didática.
        - Sempre incentive o aprendizado, não apenas entregue o resultado.
        - Se a pergunta for fora do escopo (ex: fraudar prova ou pedir algo que não seja cálculo de integrais simples),
          recuse educadamente e explique o motivo.
        - Sempre finalize com o aviso fixo:
          "Este chatbot é uma ferramenta de apoio ao estudo. 
          Não deve ser usado para fraudar avaliações. Use-o para aprender e praticar."
        - Não utilize marcação em markdown nem fórmulas em latex
        - Faça o aluno refletir sobre o próximo passo a se fazer, não dê a resposta final.
"""


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        pergunta = data.get('pergunta')
        
        if not pergunta:
            return jsonify({'resposta': 'Pergunta não fornecida.'}), 400
        
        response = ollama.chat(
            model="deepseek-v3.1:671b-cloud",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": pergunta}
            ]
        )
        
        resposta = response['message']['content']
        
        return jsonify({'resposta': resposta})
    
    except Exception as e:
        print("Erro no /chat:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)