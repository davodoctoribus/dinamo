import os
from PyPDF2 import PdfReader

PASTA_BASE = "./docs"
SAIDA_TXT = "./docs/base_texto.txt"

def extrair_texto_pdf(caminho_pdf):
    try:
        reader = PdfReader(caminho_pdf)
        texto = ""
        for pagina in reader.pages:
            if pagina.extract_text():
                texto += pagina.extract_text() + "\n"
        return texto
    except Exception as e:
        print(f"Erro {caminho_pdf}: {e}")
        return ""

def processar_pasta(pasta_base, saida_txt):
    with open(saida_txt, "w", encoding="utf-8") as f:
        for raiz, _, arquivos in os.walk(pasta_base):
            for arquivo in arquivos:
                if arquivo.lower().endswith(".pdf"):
                    caminho = os.path.join(raiz, arquivo)
                    print(f"Extraindo: {caminho}")
                    texto = extrair_texto_pdf(caminho)
                    f.write(f"\n\n===== {caminho} =====\n\n")
                    f.write(texto)
    print(f"\nTexto salvo em: {saida_txt}")

if __name__ == "__main__":
    processar_pasta(PASTA_BASE, SAIDA_TXT)
