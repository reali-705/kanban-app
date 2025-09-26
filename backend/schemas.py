from pydantic import BaseModel
from typing import List, Optional

# ==============================================================================
# Schemas para o modelo 'Cartao'
# ==============================================================================

# --- Schema Base para Cartao ---
# Contém os campos que são comuns tanto na criação quanto na leitura.
class CartaoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    responsavel: Optional[str] = None
    cor: Optional[str] = None

# --- Schema para Criação de Cartao ---
# Herda de CartaoBase e adiciona o campo necessário para criar um cartão.
class CartaoCreate(CartaoBase):
    coluna_id: int

# --- Schema para Leitura/Exibição de Cartao ---
# Este é o schema que será retornado pela API.
# Ele inclui os campos que são gerados pelo banco de dados, como o 'id'.
class Cartao(CartaoBase):
    id: int
    coluna_id: int

    class Config:
        orm_mode = True

# ==============================================================================
# Schemas para o modelo 'Coluna'
# ==============================================================================

# --- Schema Base para Coluna ---
class ColunaBase(BaseModel):
    nome: str
    posicao: int

# --- Schema para Criação de Coluna ---
class ColunaCreate(ColunaBase):
    kanban_id: int

# --- Schema para Leitura/Exibição de Coluna ---
# Importante: Este schema inclui uma lista de 'Cartao's.
class Coluna(ColunaBase):
    id: int
    kanban_id: int
    cartoes: List[Cartao] = []  # Mostra os cartões que pertencem a esta coluna.

    class Config:
        orm_mode = True

# ==============================================================================
# Schemas para o modelo 'Kanban'
# ==============================================================================

# --- Schema Base para Kanban ---
class KanbanBase(BaseModel):
    nome: str

# --- Schema para Criação de Kanban ---
# Neste caso, é igual ao base, pois só precisamos do nome para criar um Kanban.
class KanbanCreate(KanbanBase):
    pass

# --- Schema para Leitura/Exibição de Kanban ---
# Importante: Este schema inclui uma lista de 'Coluna's.
class Kanban(KanbanBase):
    id: int
    colunas: List[Coluna] = []  # Mostra as colunas que pertencem a este kanban.

    class Config:
        orm_mode = True
