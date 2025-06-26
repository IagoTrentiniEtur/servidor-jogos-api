# 🎮 API - Servidor de Jogos Multiplayer

Este projeto é uma API RESTful simulando um servidor de jogos multiplayer. A API foi desenvolvida como parte de um trabalho final da disciplina de Cloud Computing, com foco no método `GET` e automação de deploy em ambiente cloud utilizando práticas DevOps.

---

## 📌 Funcionalidades

- `GET /status`: Verifica se a API está online.
- `GET /jogadores_online`: Lista jogadores atualmente online no servidor.

---

## 🗃️ Estrutura dos Dados

Os dados estão armazenados localmente em arquivos JSON, simulando jogadores online com as seguintes informações:

```json
[
  {
    "id_jogador": "PlayerX123",
    "nickname": "ShadowHunter",
    "nivel": 27,
    "pontuacao_rank": 2350,
    "status": "Em partida"
  },
  ...
]
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- Pytest

---

## 🚀 Como Executar Localmente

### ✅ Pré-requisitos

- Python instalado ([download aqui](https://www.python.org/downloads/))
- Git instalado (opcional)
- VS Code (opcional)

### 💻 Passo a Passo

#### 1. Clone o Repositório

```bash
git clone https://github.com/seu_usuario/servidor-jogos-api.git
cd servidor-jogos-api
```

#### 2. Crie e Ative o Ambiente Virtual

##### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

##### Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

#### 4. Execute a API

```bash
uvicorn app.main:app --reload
```

Acesse:
- http://127.0.0.1:8000/status
- http://127.0.0.1:8000/jogadores_online
- http://127.0.0.1:8000/docs (Swagger UI)

---

## 🧪 Rodando Testes Unitários

Com o ambiente virtual ativado:

```bash
pytest
```

Os testes garantem que as rotas `/status` e `/jogadores_online` estão funcionando corretamente.

---

## 📝 Autor

Este projeto foi desenvolvido por **Iago** como parte do trabalho final da disciplina **Cloud Computing**.
