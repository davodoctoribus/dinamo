# ChatBot Dinamo! 🚀
Esta é a implementação prática da Equipe Roxa no PS do PET ENG COMP. Bem-vindo ao README do nosso projeto!

---

## 📝 Sobre o Projeto
O Dinamo tem como função auxiliar os estudantes da UFC com o processo de experiências fora do nosso país - intercâmbios e duplos diplomas.

Sabemos da dificuldade encarada pelos estudantes de reunir os dados e as informações necessárias para tal finalidade. Incrição, documentos necessários, cadeiras requisitadas, tempo mínimo e máximo de permanência, são dúvidas recorrentes enfrentadas pelos interessados na área.

Por isso, desenvolvemos um chatbot, do zero, que possa ajudar com informações precisas, baseadas nos editais atualizados, acerca de todas as experiências internacionais que a universidade pode proporcionar aos alunos. Esse é o Dinamo!

---

## 🚀 Funcionalidades  

- 📚 **Busca semântica** em editais e documentos oficiais.  
- 🎓 Respostas **didáticas e contextualizadas** sobre processos de intercâmbio.  
- 🔍 Recuperação de trechos relevantes dos PDFs para justificar a resposta.  
- 🌐 **Interface web simples** com backend em Flask.  
- 💾 Base vetorial persistida em **SQLite3 + ChromaDB**.

---

## 🛠️ Tecnologias Utilizadas  

- [Python 3.10+](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://www.langchain.com/)  
- [Chroma](https://www.trychroma.com/) (armazenamento vetorial)  
- [Ollama](https://ollama.com/) (modelos de linguagem e embeddings)  

## ⚙️ Como rodar o projeto  

### 1. Clonar repositório  

```bash
git clone https://github.com/davodoctoribus/dinamo
cd dinamo
```
### 2. Instalar dependências 
```bash
pip install -r requirements.txt
```

### 3. Criar base vetorial

 - Adicione as fontes em PDF na pasta `./docs/data` e rode:
```bash
ollama pull nomic-embed-text
python ./docs/scrapping.py
```
 - Os embeddings serão salvos no banco vetorial na pasta `./db_intercambio`

### 4. Rode o servidor
- Como esse modelo de linguagem rodará em nuvem, certifique-se de ter uma conta Ollama.
```bash
 ollama pull deepseek-v3.1:671b-cloud
 python app.py
 ```
---

## 🧩 O que foi feito 

Este projeto utiliza o paradigma de **RAG (Retrieval-Augmented Generation)**, que combina a capacidade de raciocínio e geração de texto dos **modelos de linguagem (LLMs)** com a confiabilidade de informações estruturadas extraídas de documentos oficiais. Na prática, os editais são convertidos em texto e divididos em **chunks**, que são transformados em **embeddings** (vetores numéricos que representam semanticamente o conteúdo) e armazenados em uma base vetorial (ChromaDB). Quando o usuário faz uma pergunta, a aplicação calcula o embedding da pergunta e realiza uma **busca semântica** para recuperar os chunks mais relevantes, garantindo que o modelo não precise “inventar” informações. Esses chunks, junto com a pergunta do usuário, são enviados ao modelo Ollama na nuvem, que gera uma resposta didática e contextualizada. Dessa forma, a abordagem RAG permite que o chatbot forneça respostas precisas e confiáveis, mantendo a capacidade de linguagem natural e explicação detalhada, ao mesmo tempo em que aproveita dados reais como referência, equilibrando geração de texto e veracidade das informações.

As principais etapas foram:  

1. **Extração de dados**:  
   - Os editais em PDF foram processados e convertidos em texto.  
   - Esse texto foi dividido em **chunks** (fragmentos menores) para melhor indexação.  

2. **Criação de base vetorial**:  
   - Cada chunk foi transformado em um **vetor numérico** (embedding) usando o modelo `nomic-embed-text`.  
   - Os vetores foram armazenados em um banco **ChromaDB persistente (SQLite3)**.  

3. **Busca semântica**:  
   - Quando o usuário faz uma pergunta, a aplicação gera o embedding da pergunta e busca os chunks mais relevantes na base vetorial via **similaridade de cosseno**.  

4. **Integração com LLM (Ollama Cloud)**:  
   - Os chunks recuperados são enviados junto com a pergunta para o modelo de linguagem.  
   - O modelo gera uma resposta didática, utilizando o contexto dos documentos reais.  

5. **API Flask**:  
   - Foi criada uma rota `/chat` que recebe perguntas via requisições `POST`.  
   - A API retorna uma resposta em JSON pronta para ser consumida pelo frontend.  

6. **Frontend Web**:  
   - Desenvolvido com **HTML, CSS puro e JavaScript**.  
   - O usuário digita a pergunta em um campo de input e clica em "Enviar".  
   - Um **script JS** envia a pergunta para o backend Flask via **fetch API** (`POST /chat`).  
   - A resposta retornada em JSON é exibida dinamicamente na página.  

---


