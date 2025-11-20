"""
Roteamento para operações relacionadas a Quadros.

Este módulo define os endpoints da API para criar e ler quadros Kanban.
A lógica de negócio é delegada para a camada de serviços.
"""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from kanban.database import get_db
import kanban.services.quadro as Quadro
import kanban.schemas as Schemas

rotas_quadros = APIRouter()


@rotas_quadros.post("/quadros/", response_model=Schemas.Quadro, tags=["Quadros"])
def criar(quadro: Schemas.QuadroCreate, db: Session = Depends(get_db)):
    """
    ### Cria um novo quadro Kanban.

    Recebe os dados de um novo quadro e os repassa para a camada de serviço
    para criação no banco de dados.
    """
    return Quadro.criar(db=db, quadro=quadro)


@rotas_quadros.get("/quadros/", response_model=List[Schemas.Quadro], tags=["Quadros"])
def ler_todos(db: Session = Depends(get_db)):
    """
    ### Retorna uma lista de todos os quadros Kanban.

    Solicita à camada de serviço a lista completa de quadros existentes.
    """
    return Quadro.ler_todos(db=db)
