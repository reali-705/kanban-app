"""
## Catálogo de Schemas Pydantic da Aplicação Kanban.

Este módulo centraliza e exporta os principais schemas Pydantic, que atuam
como os contratos de dados da API.

---

### Schemas Exportados:
Usados para validar dos dados que entram e saem da aplicação, garantindo
uma estrutura consistente e segura.

#### Contrato de Entrada:
- **`QuadroCreate`**: Define os dados necessários para criar um novo quadro.
- **`ColunaCreate`**: Define os dados para criar uma nova coluna, exigindo o `quadro_id`.
- **`CartaoCreate`**: Define os dados para criar um novo cartão, exigindo a `coluna_id`.

#### Contrato de Saída:
- **`Quadro`**: Representa um quadro completo.
- **`Coluna`**: Representa uma coluna completa.
- **`Cartao`**: Representa um cartão completo.
"""

from .cartao import CartaoCreate, Cartao
from .coluna import ColunaCreate, Coluna
from .quadro import QuadroCreate, Quadro

__all__ = [
    "CartaoCreate",
    "Cartao",
    "ColunaCreate",
    "Coluna",
    "QuadroCreate",
    "Quadro",
]
