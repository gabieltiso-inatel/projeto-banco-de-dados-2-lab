## Projeto Final Disciplina Banco de Dados 2 - Laboratório

### Como rodar o projeto

- Clone o repositório
- Já dentro do diretório do repositório, crie um `virtualenv` e
siga os passos para acioná-lo em sue sistema operacional.
- Instale as bibliotecas necessárias: `pip install -r requirements.txt`
- Crie um arquivo `.env` que contenha as seguintes informações:
```
DB_URI=<URI_DO_BANCO_NEO4J>
DB_USER=<USUARIO_DO_BANCO_NEO4J>
DB_PASSWORD=<SENHA_DO_BANCO_NEO4J>
```
Onde essas informações são obtidas ao criar um novo banco na [sandbox do neo4j](https://sandbox.neo4j.com/)

- Depois disso, ainda com o seu `venv` ativado, digite o comando: `python main.py`
