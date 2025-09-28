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
- Como esse modelo de linguagem rodará em nuvem, certifique-se de ter uma conta ollama.
```bash
 ollama pull deepseek-v3.1:671b-cloud
 python app.py
 ```
