# Orientações para o Agente de IA - Projeto Kanban Pessoal

## 1. Visão Geral do Projeto

Este é um gerenciador de tarefas pessoal no estilo Kanban, projetado para ser um executável para Windows. O objetivo é criar uma aplicação autocontida, onde cada executável gerencia seu próprio estado e dados.

- **Linguagem Principal:** Python
- **Backend:** FastAPI (API RESTful)
- **Frontend:** Flet (para a interface gráfica)
- **Banco de Dados:** SQLite (local, gerenciado pelo backend)

## 2. Arquitetura e Estrutura de Arquivos

A arquitetura é modular para separar claramente as responsabilidades:

- `backend/`: Contém toda a lógica da API, acesso ao banco de dados e regras de negócio.
  - `main.py`: Ponto de entrada da API FastAPI, onde as rotas são definidas.
  - `database.py`: Configuração da conexão com o banco de dados SQLite e sessões do SQLAlchemy.
  - `models.py`: Define as tabelas do banco de dados usando o ORM do SQLAlchemy.
  - `schemas.py`: Define os modelos de dados da API (validação e serialização) usando Pydantic.
- `frontend/`: Conterá o código da interface do usuário com Flet. (A ser desenvolvido posteriormente).
- `requirements.txt`: Lista de todas as dependências Python do projeto.
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
    - Instalar todas as dependências listadas em `requirements.txt`.

**Gerenciamento de Dependências:**
- Para adicionar uma nova dependência:
  ```powershell
  # Ative o ambiente virtual primeiro: .\.venv\Scripts\Activate.ps1
  pip install nome_do_pacote
  ```
- Após instalar um novo pacote, **sempre** atualize o `requirements.txt`:
  ```powershell
  pip freeze > requirements.txt
  ```

**Executando o Backend:**
- Para iniciar o servidor da API em modo de desenvolvimento (com recarregamento automático):
  ```powershell
  # Ative o ambiente virtual primeiro
  uvicorn backend.main:app --reload
  ```
- A API estará disponível em `http://127.0.0.1:8000`.
- A documentação interativa da API (Swagger UI) estará em `http://127.0.0.1:8000/docs`. Use-a para testar os endpoints do backend.

## 4. Convenções do Código

- **Separação de Responsabilidades:** Mantenha a lógica da API estritamente no `backend/` e a lógica da UI no `frontend/`. O frontend deve se comunicar com o backend apenas através de chamadas HTTP para a API.
- **Modelos de Dados:**
  - `models.py` é para a estrutura do banco de dados (SQLAlchemy).
  - `schemas.py` é para a "forma" dos dados que entram e saem da API (Pydantic).
- **Commits no Git:** Use mensagens de commit claras e descritivas, preferencialmente em inglês, seguindo o padrão de commits convencionais (ex: `feat:`, `fix:`, `docs:`, `refactor:`).
