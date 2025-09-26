"""
Schemas Pydantic para validação e serialização de dados da API.

Define a "forma" dos dados que entram e saem da API, garantindo um
contrato de dados claro e seguro entre o cliente e o servidor.
"""
from pydantic import BaseModel
from typing import List, Optional

# --- Schemas para Cartao ---
class CartaoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    responsavel: Optional[str] = None
    cor: Optional[str] = None

class CartaoCreate(CartaoBase):
    coluna_id: int

class Cartao(CartaoBase):
    id: int
    coluna_id: int

    class Config:
        orm_mode = True

# --- Schemas para Coluna ---
class ColunaBase(BaseModel):
    nome: str
    posicao: int

class ColunaCreate(ColunaBase):
    kanban_id: int

class Coluna(ColunaBase):
    id: int
    kanban_id: int
    cartoes: List[Cartao] = []

    class Config:
        orm_mode = True

# --- Schemas para Kanban ---
class KanbanBase(BaseModel):
    nome: str

class KanbanCreate(KanbanBase):
    pass

class Kanban(KanbanBase):
    id: int
    colunas: List[Coluna] = []

    class Config:
        orm_mode = True
