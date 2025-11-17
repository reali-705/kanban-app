# Orientações para o Agente de IA - Projeto Kanban Pessoal

## 1. Visão Geral do Projeto

Este é um gerenciador de tarefas pessoal no estilo Kanban, projetado para ser um executável para Windows. O objetivo é criar uma aplicação autocontida, onde cada executável gerencia seu próprio estado e dados.

- **Linguagem Principal:** Python
- **Backend:** FastAPI (API RESTful)
- **Frontend:** Flet (para a interface gráfica)
- **Banco de Dados:** SQLite (local, gerenciado pelo backend)

## 2. Arquitetura e Estrutura de Arquivos

A arquitetura é modular para separar claramente as responsabilidades:

- `src/kanban/`: Contém toda a lógica da API, acesso ao banco de dados e regras de negócio.
  - `main.py`: Ponto de entrada da API FastAPI, onde as rotas são definidas e incluídas.
  - `database.py`: Configuração da conexão com o banco de dados SQLite e a dependência `get_db`.
  - `models/`: Define as tabelas do banco de dados usando o ORM do SQLAlchemy.
  - `schemas/`: Define os modelos de dados da API (validação e serialização) usando Pydantic.
  - `routes/`: Contém os roteadores modulares da API (ex: `kanbans_rotas.py`).
  - `services/`: Contém a lógica de negócio (operações CRUD).
- `frontend/`: Conterá o código da interface do usuário com Flet.
- `pyproject.toml`: Arquivo central que define metadados do projeto e dependências.
- `setup.ps1`: Script PowerShell para automatizar a configuração do ambiente de desenvolvimento.

## 3. Fluxo de Trabalho do Desenvolvedor

**Configuração do Ambiente:**
1.  Para configurar o ambiente do zero, execute o script `setup.ps1` no PowerShell:
    ```powershell
    .\setup.ps1
    ```
2.  Este script irá:
    - Verificar se o Python está instalado.
    - Criar um ambiente virtual em `.venv/` se não existir.
    - Instalar todas as dependências listadas em `pyproject.toml` (principais e de desenvolvimento).

**Gerenciamento de Dependências:**
- Para adicionar uma nova dependência, adicione-a à seção apropriada no `pyproject.toml` e execute novamente `.\setup.ps1` ou `pip install -e .[dev]`.

**Executando o Backend:**
- Para iniciar o servidor da API em modo de desenvolvimento (com recarregamento automático):
  ```powershell
  # Ative o ambiente virtual primeiro: .\.venv\Scripts\Activate.ps1
  uvicorn src.kanban.main:app --reload
  ```
- A API estará disponível em `http://127.0.0.1:8000`.
- A documentação interativa da API (Swagger UI) estará em `http://127.0.0.1:8000/docs`. Use-a para testar os endpoints do backend.

## 4. Convenções do Código

- **Separação de Responsabilidades:** Mantenha a lógica da API estritamente em `src/kanban/` e a lógica da UI em `frontend/`. O frontend deve se comunicar com o backend apenas através de chamadas HTTP para a API.
- **Modelos de Dados:**
  - `models/` é para a estrutura do banco de dados (SQLAlchemy).
  - `schemas/` é para a "forma" dos dados que entram e saem da API (Pydantic).
- **Commits no Git:** Use mensagens de commit claras e descritivas, preferencialmente em português-brasil, seguindo o padrão de commits convencionais (ex: `feat:`, `fix:`, `docs:`, `refactor:`).
