# Backend Kanban Pessoal

Este diretório contém toda a lógica da API, acesso ao banco de dados e regras de negócio do Kanban Pessoal.

## Estrutura

- **main.py:** Ponto de entrada da API FastAPI, onde os routers são incluídos.
- **schemas/**: Modelos de dados (Pydantic), modelos ORM (SQLAlchemy) e configuração do banco de dados.
- **routes/**: Rotas organizadas por recurso (kanban, coluna, cartão).
- **services/**: Lógica de negócio e manipulação dos dados.
- **kanban.db:** Banco de dados SQLite local.

## Convenções

- Separação clara entre modelos, schemas, rotas e serviços.
- Imports organizados para facilitar manutenção e expansão.
- Modularização para permitir testes e futuras integrações com o frontend.

## Testes

Os testes automatizados estão organizados no diretório [`tests/`](../tests/README.md), com ambiente isolado e marcadores personalizados.

[Voltar para a raiz do projeto](../README.md)