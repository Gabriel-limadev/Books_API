# 📚 Books API

**Books API** é uma API construída com **FastAPI** para consulta de dados de livros.  
O projeto foi desenvolvido como **1° trabalho na Pós em Engenharia de Machine Learning pela FIAP**.

---

## 🚀 Funcionalidades

- 📖 Listar todos os livros  
- 🔎 Buscar livro por ID  
- 🏷️ Filtrar livros por título e/ou categoria
- 📚 Listar todas as categorias
- ❤️ Health check da API
- 📄 Documentação automática com Swagger (FastAPI)

---

## 🌐 API em Produção

A API está disponível em produção no Render:

👉 **https://books-api-j70z.onrender.com/api/v1**

Documentação:

👉 **https://books-api-j70z.onrender.com/docs**

---

## 📌 Endpoints

| Método | Endpoint | Descrição | Exemplo de busca |
|--------|----------|-----------|------------------|
| GET | `/api/v1` | Informações da API | — |
| GET | `/api/v1/health` | Verifica se a API está ativa | — |
| GET | `/api/v1/books` | Lista todos os livros | — |
| GET | `/api/v1/books/{id}` | Busca livro por ID | `/api/v1/books/1` |
| GET | `/api/v1/books/search` | Busca livros por título e/ou categoria | `/api/v1/books/search?title=harry`<br>`/api/v1/books/search?category=Fantasy`<br>`/api/v1/books/search?title=harry&category=Fantasy` |
| GET | `/api/v1/categories` | Lista todas as categorias | — |


---

## 🛠 Tecnologias Utilizadas

- **Python**
- **FastAPI**
- **SQLModel**
- **SQLite**
- **Uvicorn**
- **Render (deploy)**
- **Selenium (Web Scraping)**

---

## 🕸️ Web Scraper

Os dados utilizados nesta API foram obtidos por meio de um **web scraper desenvolvido em Python**, responsável por coletar informações de livros como:

- Título
- Categoria
- Preço
- Avaliação
- Disponibilidade

O site utilizado como fonte dos dados foi:

🔗 https://books.toscrape.com/

---

### 📦 Banco de dados (`books.db`)

Para facilitar o uso da API e a avaliação do projeto, o arquivo **`books.db` já está incluído no repositório**.  
Dessa forma, a API pode ser executada imediatamente, sem a necessidade de rodar o scraper.

Essa decisão foi tomada para:
- Simplificar a execução do projeto
- Evitar dependências de scraping durante a execução da API
- Garantir que os dados estejam disponíveis desde o início

O scraper permanece disponível no repositório apenas como etapa opcional de coleta e atualização dos dados.

---

### ▶️ Executando o scraper manualmente

Caso alguém queira **analisar o scraper** ou **gerar novamente o banco de dados**, basta:

1. Clonar o repositório:
   ```bash
   git clone https://github.com/Gabriel-limadev/Books_API.git
   cd Books_API
2. Instalar dependências:
   ```bash
   pip install -r requirements.txt

3. Executar scraper
   ```bash
   python scraper/run_scraper.py

---

## 👨‍💻 Autor

Gabriel Lima  
Pós-graduação em Engenharia de Machine Learning — FIAP

