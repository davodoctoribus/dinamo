from flask import Flask, request, jsonify
import ollama
from flask_cors import CORS
from langchain.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

app = Flask(__name__)
CORS(app)

# Caminho da base vetorial
PASTA_CHROMA = "db_intercambio"

# Inicializar embeddings e carregar base
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=PASTA_CHROMA, embedding_function=embeddings)

# Prompt base para orientar o modelo
prompt_sistema = """
Você é um assistente especializado em intercâmbios e duplo diploma. 
Use os textos que o usuário trouxer para responder dúvidas sobre processos de intercâmbio, editais e requisitos.
Sempre explique de forma clara e didática.
Seja conciso e direto em um parágrafo, não responda mais do que foi pedido.
Não invente informações fora do contexto fornecido.
Sempre incentive o aprendizado do usuário.
Não utilize marcação em markdown, apenas plain text
Não deixe explicito que o contexto provém de editais que foram mandados a você, finja que você ja sabe essas informações
"""

def buscar_documentos(pergunta, top_k=3):
    """
    Retorna os top_k chunks mais relevantes da base vetorial para a pergunta.
    """
    resultados = vectorstore.similarity_search(pergunta, k=top_k)
    textos = [r.page_content for r in resultados]
    return textos

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        pergunta = data.get('pergunta')
        if not pergunta:
            return jsonify({'resposta': 'Pergunta não fornecida.'}), 400

        # Buscar contexto na base vetorial
        contexto = buscar_documentos(pergunta)
        if not contexto:
            contexto_texto = "Nenhum documento relevante encontrado."
        else:
            contexto_texto = "\n\n".join(contexto)

        # Montar mensagem final para o modelo
        mensagem = f"{prompt_sistema}\n\nContexto:\n{contexto_texto}\n\nPergunta do usuário: {pergunta}"

        # Chamada ao Ollama
        response = ollama.chat(
            model="deepseek-v3.1:671b-cloud",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": mensagem}
            ]
        )

        resposta = response['message']['content']
        return jsonify({'resposta': resposta})

    except Exception as e:
        print("Erro no /chat:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
