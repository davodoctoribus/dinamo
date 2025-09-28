from langchain.text_splitter import RecursiveCharacterTextSplitter

ARQUIVO_ENTRADA = "docs/base_texto.txt"
ARQUIVO_SAIDA = "docs/base_chunks.txt"

def carregar_texto(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return f.read()

def salvar_chunks(chunks, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            f.write(f"\n\n===== CHUNK {i+1} =====\n\n")
            f.write(chunk)

def gerar_chunks(texto, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(texto)

if __name__ == "__main__":
    texto = carregar_texto(ARQUIVO_ENTRADA)
    chunks = gerar_chunks(texto)
    print(f"Gerados {len(chunks)} chunks")
    salvar_chunks(chunks, ARQUIVO_SAIDA)
