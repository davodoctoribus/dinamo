from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

PASTA_PDFS = "docs/data"
PASTA_CHROMA = "db_intercambio"

# Cria embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Carregar PDFs
docs = []
import os
for arquivo in os.listdir(PASTA_PDFS):
    if arquivo.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PASTA_PDFS, arquivo))
        docs.extend(loader.load())

# Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(docs)

# Criar base vetorial
vectorstore = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=PASTA_CHROMA)
vectorstore.persist()

print(f"Base vetorial criada com {len(chunks)} chunks.")
