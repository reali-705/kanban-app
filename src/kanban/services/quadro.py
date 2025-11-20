"""
Módulo de Serviços para a entidade Quadro.

Este arquivo contém a lógica de negócio e as operações de banco de dados
(CRUD - Create, Read, Update, Delete) relacionadas aos quadros Kanban.

A camada de serviço atua como um intermediário entre a camada de rotas (API)
e a camada de Modelos (banco de dados), garantindo que as rotas permaneçam
limpas e focadas em lidar com requisições HTTP.
"""

from typing import List
from sqlalchemy.orm import Session

import kanban.models as Modelos
import kanban.schemas as Schemas


def criar(db: Session, quadro: Schemas.QuadroCreate) -> Modelos.Quadro:
    """
    Cria um novo quadro Kanban no banco de dados.
    Confirma a transação e retorna o objeto do quadro criado com o ID gerado pelo banco.

    Args:
        db: A sessão do banco de dados.
        quadro: O schema Pydantic com os dados para a criação do quadro.

    Returns:
        O objeto modelo SQLAlchemy do quadro recém-criado.
    """

    db_quadro = Modelos.Quadro(**quadro.model_dump())
    db.add(db_quadro)
    db.commit()
    db.refresh(db_quadro)
    return db_quadro


def ler_todos(db: Session) -> List[Modelos.Quadro]:
    """
    Retorna uma lista de todos os quadros Kanban do banco de dados.

    Args:
        db: A sessão do banco de dados.

    Returns:
        Uma lista de objetos modelo SQLAlchemy de quadros.
    """
    return db.query(Modelos.Quadro).all()
