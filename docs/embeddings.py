from langchain.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

ARQUIVO_CHUNKS = "docs/base_chunks.txt"
PASTA_CHROMA = "db_intercambio" 

def carregar_chunks(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
    partes = conteudo.split("===== CHUNK")
    chunks = [p.strip() for p in partes if p.strip()]
    return chunks

if __name__ == "__main__":
    
    chunks = carregar_chunks(ARQUIVO_CHUNKS)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=PASTA_CHROMA
    )

    vectorstore.persist()
    print(f"Base vetorial salva em: {PASTA_CHROMA}")

