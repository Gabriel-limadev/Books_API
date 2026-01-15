# 📚 Books API

**Books API** é uma API construída com **FastAPI** para consulta de dados de livros.  
O projeto foi desenvolvido como **1° trabalho na Pós em Engenharia de Machine Learning pela FIAP**.

---

## 🌐 API em Produção
``` code
Rota inicial:  https://books-api-j70z.onrender.com/api/v1
Documentação:  https://books-api-j70z.onrender.com/docs
Status da API: https://books-api-j70z.onrender.com/api/v1/health
```

---

## 🚀 Funcionalidades

- 📖 Scraping de livros
- 📖 Listar todos os livros
- 🔎 Buscar livro por ID
- 🏷️ Filtrar livros por título e/ou categoria
- ⭐ Buscar pelos livros com maiores ratings
- 💰 Filtrar por um range de valores
- 📚 Listar todas as categorias
- 📊 Trazer um overview com as métricas principais
- ❤️ Health check da API
- 📄 Documentação automática com Swagger (FastAPI)

---

## 🧱 Arquitetura do Projeto

O projeto segue uma arquitetura simples e organizada, separando responsabilidades:

``` text
Books_API/
├── app/
│   ├── api/                 # Rotas da API
│   │   └── v1/
│   │       ├── endpoints/   # Endpoints (auth, books, categories, health, scraping, stats)
│   │       └── router.py    # Router principal
│   │
│   ├── core/
│   │   └── config.py       
|   |   └── security.db     
│   │
│   ├── db/                  # Banco de dados
│   │   └── session.py       # Sessão SQLite
|   |   └── books.db         # Banco SQLite
│   │
│   ├── models/              # Modelos (SQLModel)
│   │   └── auth.py
│   │   └── book.py
│   │
│   ├── repositories/        # Acesso ao banco
│   │   └── auth_repository.py
│   │   └── book_repository.py
│   │
|   ├── schemas/             # Schemas do Banco    
|   |   └── auth.py
|   |   └── book.py
|   |   └── stats.py
|   |
│   ├── services/            # Regras de negócio
│   |   └── auth_service.py
|   |   └── book_service.py
|   |   └── health_service.py
|   |   └── scraping_service.py
|   |   └── stats_service.py
│   |
|   ├── scraper/             # 🕷️ Coleta de dados
│   |   └── book_scraper.py
|   |   └── parser.py
|
├── main.py                  # Inicialização da API
├── pyproject.toml
├── poetry.lock
├── requirements.txt
├── runtime.txt
├── README.md
```

## 📌 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1` | Informações da API |
| GET | `/api/v1/health` | Verifica se a API está ativa |
| POST | `/api/v1/auth/register` | Responsavel pelo cadastro do usuario |
| POST | `/api/v1/auth/login` | Responsavel pelo login do usuario |
| POST | `/api/v1/scraping` | Realiza o scraping e atualiza o banco |
| GET | `/api/v1/books` | Lista todos os livros | 
| GET | `/api/v1/books/{id}` | Busca livro por ID |
| GET | `/api/v1/books/search` | Busca livros por título e/ou categoria |
| GET | `/api/v1/books/top-rated?5` | Busca livros por maiores ratings |
| GET | `/api/v1/books/price-range?min=2&max=10` | Busca livros por range de preço |
| GET | `/api/v1/categories` | Lista todas as categorias |
| GET | `/api/v1/stats/overview` | Lista principais métricas dos livros |
| GET | `/api/v1/stats/categories` | Lista principais métricas das categorias |

---

### 🚀 Como utilizar a API

A API possui autenticação via **JWT (Bearer Token)**. Para consumir as rotas protegidas, é necessário realizar o cadastro e o login do usuário.

---

#### 1️⃣ Cadastro de usuário

Realize o cadastro através da rota: 
``` code
POST /api/v1/auth/register
```
Informe o username e o password no corpo da requisição.
```code
{
    "username": str,
    "password": str
}
```

---

#### 2️⃣ Login

Após o cadastro, realize o login na rota: POST /api/v1/auth/login

Essa requisição retornará um **token de acesso (JWT)**, que será necessário para acessar as demais rotas da API.

Informe o username e o password no corpo da requisição.
```code
{
    "username": str,
    "password": str
}
```
---

#### 3️⃣ Utilizando a API pelo Swagger (/docs)

1. Acesse o endpoint `/docs`
2. Clique no botão **Authorize**
3. Cole o token no formato: Bearer SEU_TOKEN_AQUI
4. Após a autenticação, as rotas protegidas estarão liberadas para consumo.

---

#### 4️⃣ Utilizando a API pelo Postman

1. Crie uma nova requisição no Postman
2. Vá até a aba **Authorization**
3. Em **Auth Type**, selecione **Bearer Token**
4. Cole o token de acesso no campo correspondente
5. Execute a requisição normalmente

---

Com o token configurado, será possível acessar a rota de scraping da API.

---

## 📄 Exemplos de Requests e Responses

### 🔹 Verificar saúde da API
**Request**
```http
GET /api/v1/health
```
**Response**
```code
{
  "status": "ok"
}
```

### 🔹 Realizar cadastro
**Request**
```http
POST /api/v1/auth/register
```

### 🔹 Realizar login
**Request**
```http
POST /api/v1/auth/login
```
**Response**
```code
{
    "access_token": str
    "refresh_token": str,
    "token_type": "bearer"
}
```

### 🔹 Realizar Scraping
**Request**
```http
POST /api/v1/auth/scraping
```
**Response**
```code
{
    "total": int
    "inserted": int,
    "updated": int
}
```


### 🔹 Buscar todos os livros
**Request**
```http
GET /api/v1/books
```
**Response**
```code
[
   {
     "id": 1,
     "title": "1,000 Places to See Before You Die",
     "price": 26.08,
     "rating": 5,
     "availability": 1,
     "category": "Travel",
     "image": "https://books.toscrape.com/media/cache/9e/10/9e106f81f65b293e488718a4f54a6a3f.jpg"
   }
]
```
### 🔹 Buscar livros por título e/ou categoria
**Request**
```http
GET /api/v1/books/search?title=harry&category=Fantasy
```
**Response**
```code
[
   {
     "id": 327,
     "title": "Harry Potter and the Order of the Phoenix (Harry Potter #5)",
     "price": 31.63,
     "rating": 4,
     "availability": 4,
     "category": "Fantasy",
     "image": "https://books.toscrape.com/media/cache/ca/56/ca565814dfe2d9f73d3d6b1ad7265984.jpg"
   }
]
```
### 🔹 Buscar livro pelo id
**Request**
```http
GET /api/v1/books/2
```
**Response**
```code
[
   {
     "id": 2,
     "title": "1st to Die (Women's Murder Club #1)",
     "price": 53.98,
     "rating": 1,
     "availability": 1,
     "category": "Mystery",
     "image": "https://books.toscrape.com/media/cache/f6/8e/f68e6ae2f9da04fccbde8442b0a1b52a.jpg"
   }
]
```

### 🔹 Buscar livros por maiores ratings
**Request**
```http
GET /api/v1/books/top-rated?5
```
**Response**
```code
[
    {
        "id": 996,
        "title": "Sapiens: A Brief History of Humankind",
        "price": 54.23,
        "rating": 5,
        "availability": 20,
        "category": "History",
        "image": "https://books.toscrape.com/media/cache/ce/5f/ce5f052c65cc963cf4422be096e915c9.jpg"
    },
   ...
]
```

### 🔹 Buscar livros por range de preço
**Request**
```http
GET /api/v1/books/price-range?min=2&max=10
```
**Response**
```code
[
    {
        "id": 362,
        "title": "An Abundance of Katherines",
        "price": 10.0,
        "rating": 5,
        "availability": 5,
        "category": "Young Adult",
        "image": "https://books.toscrape.com/media/cache/9b/c8/9bc86bc10a6beea536422bbe82e076fb.jpg"
    }
]

```

### 🔹 Buscar categorias
**Request**
```http
GET /api/v1/categories
```
**Response**
```code
[
  "string"
]
```

### 🔹 Listar principais métricas dos livros
**Request**
```http
GET /api/v1/stats/overview
```
**Response**
```code
{
    "total_livros": 1000,
    "preco_medio": 35.07034999999999,
    "distribuicao_ratings": [
        {
            "rating": 1,
            "quantidade": 226
        },
       ...
    ]
}
```

### 🔹 Listar principais métricas das categorias
**Request**
```http
GET /api/v1/stats/categories
```

**Response**
```code
[
    {
        "category": "Academic",
        "total_livros": 1,
        "preco_medio": 13.12
    },
    ...
]
```

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
Dessa forma, a API pode ser executada imediatamente, sem a necessidade de rodar o scraper pela rota.
Porém caso queira fazer o scraper, utilize a rota api/v1/scraping para atualizar a tabela.

---

### ▶️ Executando a API manualmente

Caso queira **Rodar a API em sua máquina local**

1. Clonar o repositório:
   ```bash
   git clone https://github.com/Gabriel-limadev/Books_API.git
   cd Books_API
   
2. Instalar dependências:
   ```bash
   pip install -r requirements.txt

3. Rodar API
   ```bash
   uvicorn app.main:app --reload

A API ficará disponivel localmente em: http://127.0.0.1:8000/api/v1

## 🏗️ Plano Arquitetural

### 🔄 Pipeline de Dados

O fluxo de dados do sistema inicia na coleta de informações a partir do site **Books to Scrape**, passando por um processo de scraping e tratamento dos dados, que são posteriormente armazenados em um banco de dados SQLite.

A API desenvolvida com **FastAPI** é responsável por expor esses dados por meio de endpoints REST, utilizando autenticação **JWT** para controle de acesso. A API pode ser consumida por aplicações externas ou ferramentas de teste de API, como Postman e Swagger.

<p align="center">
  <img width="900" height="650" alt="Pipeline" src="https://github.com/user-attachments/assets/389fc3d1-bf64-4373-bc38-23848df1af0e" />
</p>

---

### 📈 Escalabilidade Futura

A arquitetura da aplicação foi desenvolvida de forma **modular**, permitindo sua evolução sem a necessidade de grandes refatorações. A separação entre ingestão de dados, persistência e exposição via API facilita a substituição ou melhoria de componentes conforme o crescimento do projeto.

Como possibilidades de escalabilidade futura, destacam-se:

- Substituição do banco de dados SQLite por um banco relacional mais robusto, como **PostgreSQL** ou **MySQL**.
- Containerização da aplicação utilizando **Docker**, facilitando o deploy em ambientes de nuvem.
- Implantação em provedores cloud, como **AWS**, **GCP** ou **Render**, com suporte a múltiplas instâncias.
- Implementação de cache (ex.: **Redis**) para melhorar a performance em requisições frequentes.
- Automatização do pipeline de ingestão de dados por meio de tarefas agendadas.

Essa abordagem garante que a API possa crescer em volume de dados e número de usuários sem comprometer sua estrutura.

---

### 📊 Cenário de Uso para Cientistas de Dados e Machine Learning

A API também foi pensada para atender **cientistas de dados e analistas**, servindo como uma fonte centralizada e confiável de dados.

Os dados disponibilizados pela API podem ser consumidos para:

- Análises exploratórias dos livros cadastrados.
- Criação de dashboards analíticos.
- Estudos estatísticos sobre preços, categorias e avaliações.

Dessa forma, a API atua como uma camada intermediária entre o banco de dados e os processos analíticos, evitando o acesso direto ao banco e garantindo padronização no consumo dos dados.

---

### 🤖 Plano de Integração com Modelos de Machine Learning

A arquitetura permite a integração futura com modelos de **Machine Learning** de forma desacoplada. Os dados fornecidos pela API podem ser utilizados para treinamento de modelos, enquanto a inferência pode ser realizada por meio de novos endpoints.

Um possível fluxo de integração seria:

- Extração dos dados da API para treinamento de modelos de ML.
- Armazenamento do modelo treinado.
- Criação de um endpoint específico na API (ex.: `/predict`) para realizar previsões em tempo real.

Essa abordagem possibilita a evolução do sistema para casos de uso mais avançados, como sistemas de recomendação ou previsão de preços, sem impactar negativamente a API principal.

## 👨‍💻 Autor

Gabriel Lima  
Pós-graduação em Engenharia de Machine Learning — FIAP

