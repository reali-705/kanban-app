# Código-Fonte do Backend (`src/kanban`)

Este diretório contém o pacote principal da aplicação, onde toda a lógica do lado do servidor reside. Ele foi construído com [FastAPI](https://fastapi.tiangolo.com/) e segue uma arquitetura modular para garantir que o código seja organizado, fácil de manter e escalável.

## 📂 Estrutura de Diretórios

A separação de responsabilidades é um pilar fundamental deste projeto. A estrutura abaixo foi desenhada para isolar diferentes aspectos da aplicação, como a manipulação de requisições, a lógica de negócio e o acesso aos dados.

```
src/kanban/
├── main.py         # Ponto de entrada e inicialização da API
├── database.py     # Configuração da conexão com o banco de dados e dependência get_db
├── models/         # Modelos de dados do SQLAlchemy (tabelas)
├── routes/         # Manipulação de requisições HTTP (FastAPI Routers)
├── schemas/        # Schemas de validação de dados (Pydantic)
└── services/       # Lógica de Negócio (operações CRUD)
```

### Detalhamento da Arquitetura

A tabela a seguir detalha o propósito de cada módulo e diretório:

| Módulo/Diretório | Exemplos de Conteúdo | Propósito e Benefícios |
| :--- | :--- | :--- |
| **`main.py`** | `app = FastAPI()`, `app.include_router(...)` | **Responsabilidade:** Inicializar a aplicação FastAPI e incluir todos os roteadores modulares. **Benefícios:** Serve como um ponto de entrada único e claro para a aplicação. |
| **`database.py`** | `create_engine`, `SessionLocal`, `get_db` | **Responsabilidade:** Configurar a conexão com o banco de dados e fornecer a dependência `get_db` para gerenciar as sessões. **Benefícios:** Centraliza toda a configuração de acesso ao banco de dados. |
| **`/models`** | `kanban_modelo.py`, `coluna_modelo.py` | **Responsabilidade:** Definir a estrutura das tabelas do banco de dados usando o ORM do SQLAlchemy. **Benefícios:** Cria uma representação em Python das tabelas do banco de dados. |
| **`/routes`** | `kanbans_rotas.py`, `colunas_rotas.py` | **Responsabilidade:** Receber requisições HTTP e retornar respostas, usando `APIRouter`. **Benefícios:** Mantém o código de endpoints limpo e focado, facilitando a leitura e a localização de rotas. |
| **`/schemas`** | `pydantic.py` | **Responsabilidade:** Definir a "forma" dos dados da API com Pydantic para validação e serialização. **Benefícios:** Garante um contrato de dados claro e seguro entre cliente e servidor. |
| **`/services`** | `kanbans_servicos.py` | **Responsabilidade:** Executar a lógica de negócio (CRUD) e interagir com a camada de dados (`models`). **Benefícios:** Centraliza as regras de negócio, simplificando a manutenção e evitando duplicação de código. |

---

Em resumo, essa arquitetura fragmentada foi escolhida para:

  - **Facilitar a Leitura:** Encontrar o código relevante para uma tarefa é rápido e intuitivo.
  - **Simplificar a Manutenção:** Alterações em uma parte do sistema (ex: regra de negócio) têm menos chance de impactar outras (ex: endpoints).
  - **Promover a Escalabilidade:** Adicionar novas funcionalidades, como "Cartões", se torna um processo padronizado de criar novos arquivos de rota, serviço e esquema, sem alterar o código existente.

-----

[↩️ Voltar para a raiz do projeto](../../)