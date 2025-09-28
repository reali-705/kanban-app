"""
Schemas Pydantic para validação e serialização de dados da API.

Define a "forma" dos dados que entram e saem da API, garantindo um
contrato de dados claro e seguro entre o cliente e o servidor.
"""
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

# --- Schemas para Cartao ---
class CartaoBaseSchema(BaseModel):
    titulo: str = Field(..., min_length=1)
    descricao: Optional[str] = None
    responsavel: Optional[str] = None
    cor: Optional[str] = None

class CartaoCreateSchema(CartaoBaseSchema):
    coluna_id: int

class CartaoSchema(CartaoBaseSchema):
    id: int
    coluna_id: int

    model_config = ConfigDict(from_attributes=True)

# --- Schemas para Coluna ---
class ColunaBaseSchema(BaseModel):
    nome: str = Field(..., min_length=1)
    posicao: int

class ColunaCreateSchema(ColunaBaseSchema):
    kanban_id: int

class ColunaSchema(ColunaBaseSchema):
    id: int
    kanban_id: int
    cartoes: List[CartaoSchema] = []

    model_config = ConfigDict(from_attributes=True)

# --- Schemas para Kanban ---
class KanbanBaseSchema(BaseModel):
    nome: str = Field(..., min_length=1)

class KanbanCreateSchema(KanbanBaseSchema):
    pass

class KanbanSchema(KanbanBaseSchema):
    id: int
    colunas: List[ColunaSchema] = []

    model_config = ConfigDict(from_attributes=True)
