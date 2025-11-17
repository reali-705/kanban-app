"""
Schemas Pydantic para validação e serialização de dados da API.

Define a "forma" dos dados que entram e saem da API, garantindo um
contrato de dados claro e seguro entre o cliente e o servidor.
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


# --- Schemas para Cartao ---
class CartaoBaseSchema(BaseModel):
    """Schema base para um cartão, contendo os campos compartilhados."""

    titulo: str = Field(..., min_length=1, description="O título do cartão.")
    descricao: Optional[str] = Field(
        None, description="A descrição detalhada do cartão."
    )
    responsavel: Optional[str] = Field(
        None, description="A pessoa ou equipe responsável pelo cartão."
    )
    cor: Optional[str] = Field(
        None, description="A cor de destaque do cartão (ex: '#FFFFFF')."
    )


class CartaoCreateSchema(CartaoBaseSchema):
    """Schema usado para a criação de um novo cartão."""

    coluna_id: int


class CartaoSchema(CartaoBaseSchema):
    """Schema para a representação completa de um cartão, incluindo seu ID."""

    id: int
    coluna_id: int

    model_config = ConfigDict(from_attributes=True)


# --- Schemas para Coluna ---
class ColunaBaseSchema(BaseModel):
    """Schema base para uma coluna, contendo os campos compartilhados."""

    nome: str = Field(..., min_length=1, description="O nome da coluna.")
    posicao: int = Field(..., description="A posição da coluna no quadro Kanban.")


class ColunaCreateSchema(ColunaBaseSchema):
    """Schema usado para a criação de uma nova coluna."""

    kanban_id: int


class ColunaSchema(ColunaBaseSchema):
    """Schema para a representação completa de uma coluna, incluindo seus cartões."""

    id: int
    kanban_id: int
    cartoes: List[CartaoSchema] = []

    model_config = ConfigDict(from_attributes=True)


# --- Schemas para Kanban ---
class KanbanBaseSchema(BaseModel):
    """Schema base para um quadro Kanban."""

    nome: str = Field(..., min_length=1, description="O nome do quadro Kanban.")


class KanbanCreateSchema(KanbanBaseSchema):
    """Schema usado para a criação de um novo quadro Kanban."""


class KanbanSchema(KanbanBaseSchema):
    """Schema para a representação completa de um quadro Kanban, incluindo suas colunas."""

    id: int
    colunas: List[ColunaSchema] = []
    model_config = ConfigDict(from_attributes=True)
