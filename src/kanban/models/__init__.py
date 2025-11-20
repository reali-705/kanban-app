"""
## Catálogo de Modelos ORM (SQLAlchemy) da Aplicação.

Este módulo centraliza e exporta os modelos de dados que mapeiam
diretamente as tabelas do banco de dados. Cada classe aqui representa
uma tabela e define sua estrutura, colunas e relacionamentos.

---

### Modelos de Tabela Exportados:

- **`Quadro`**: Mapeia a tabela `quadros`.
Define a estrutura de um quadro Kanban e seu relacionamento um-para-muitos com as colunas.

- **`Coluna`**: Mapeia a tabela `colunas`.
Define a estrutura de uma coluna, e seu relacionamento um-para-muitos com os cartões.

- **`Cartao`**: Mapeia a tabela `cartoes`.
Define a estrutura de um cartão de tarefa e a qual coluna ele pertence.
"""

from .cartao import Cartao
from .coluna import Coluna
from .quadro import Quadro

__all__ = [
    "Cartao",
    "Coluna",
    "Quadro",
]
