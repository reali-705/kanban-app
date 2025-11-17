"""
Roteamento para operações relacionadas a Kanbans.
"""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from kanban.database import get_db
from kanban.schemas.models import KanbanModelo
from kanban.schemas.pydantic import KanbanCreateSchema, KanbanSchema

router = APIRouter()


@router.post("/kanbans/", response_model=KanbanSchema, tags=["Kanbans"])
def criar_kanban(kanban: KanbanCreateSchema, db: Session = Depends(get_db)):
    """Cria um novo quadro Kanban."""
    # Cria uma instância do modelo SQLAlchemy a partir dos dados do schema
    db_kanban = KanbanModelo(nome=kanban.nome)
    db.add(db_kanban)  # Adiciona o novo objeto à sessão
    db.commit()  # Confirma a transação, salvando no banco
    db.refresh(db_kanban)  # Atualiza o objeto com os dados do banco (como o novo ID)
    return db_kanban


@router.get("/kanbans/", response_model=List[KanbanSchema], tags=["Kanbans"])
def ler_todos_kanbans(db: Session = Depends(get_db)):
    """Retorna uma lista de todos os quadros Kanban."""
    kanbans = db.query(KanbanModelo).all()
    return kanbans
