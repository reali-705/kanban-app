# Backend da Aplicação Kanban

Este diretório contém toda a lógica da aplicação do lado do servidor. Ele foi construído com [FastAPI](https://fastapi.tiangolo.com/) e segue uma arquitetura modular para garantir que o código seja organizado, fácil de manter e escalável.

## 📂 Estrutura de Diretórios do Backend

A separação de responsabilidades é um pilar fundamental deste projeto. A estrutura abaixo foi desenhada para isolar diferentes aspectos da aplicação, como a manipulação de requisições, a lógica de negócio e o acesso aos dados.

```
backend/
├── main.py       # Ponto de entrada e inicialização da API
├── routers/      # Manipulação de requisições HTTP (FastAPI Routers)
├── services/     # Lógica de Negócio e Interação com o DB (CRUD)
└── schemas/      # Estrutura de Dados e Conexão com o DB
```

### Detalhamento da Arquitetura

A tabela a seguir detalha o propósito de cada diretório, o que você encontrará dentro deles e os benefícios desta abordagem.

| Diretório | Exemplos de Conteúdo | Propósito e Benefícios |
| :--- | :--- | :--- |
| **`/routers`** | `kanbans_router.py`, `colunas_router.py` | **Responsabilidade:** Receber requisições HTTP e retornar respostas. **Benefícios:** Mantém o código de endpoints limpo e focado, facilitando a **leitura** e a localização de rotas específicas. |
| **`/services`** | `kanbans_service.py`, `colunas_service.py` | **Responsabilidade:** Executar a lógica de negócio (criar, ler, atualizar, deletar - CRUD) e interagir com a camada de dados. **Benefícios:** Centraliza as regras de negócio, o que simplifica a **manutenção** e evita duplicação de código. |
| **`/schemas`** | `models.py`, `schemas.py`, `database.py` | **Responsabilidade:** Definir a estrutura dos dados (modelos SQLAlchemy), a validação de dados (esquemas Pydantic) e a configuração da conexão com o banco de dados. **Benefícios:** Garante a consistência dos dados e prepara o projeto para **escalabilidade**, permitindo a fácil modificação ou adição de novas entidades. |
| **`main.py`** | `app = FastAPI()`, `app.include_router(...)` | **Responsabilidade:** Inicializar a aplicação FastAPI e incluir todos os routers. **Benefícios:** Serve como um ponto de entrada único e claro para a aplicação. |
---

Em resumo, essa arquitetura fragmentada foi escolhida para:

  - **Facilitar a Leitura:** Encontrar o código relevante para uma tarefa é rápido e intuitivo.
  - **Simplificar a Manutenção:** Alterações em uma parte do sistema (ex: regra de negócio) têm menos chance de impactar outras (ex: endpoints).
  - **Promover a Escalabilidade:** Adicionar novas funcionalidades, como "Cartões", se torna um processo padronizado de criar novos arquivos de rota, serviço e esquema, sem alterar o código existente.

-----

[↩️ Voltar para a raiz do projeto](../)