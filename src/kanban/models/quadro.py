"""
Módulo de Modelo ORM para a entidade Quadro.

Este arquivo define a classe `Quadro`, que mapeia para a tabela "quadros"
no banco de dados usando o ORM do SQLAlchemy. Cada instância desta classe
representa um registro (uma linha) na tabela.
"""

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from kanban.database import Base


class Quadro(Base):
    """
    Representa um quadro Kanban na tabela `quadros`.

    Um quadro é o contêiner principal que agrupa várias colunas.

    ### Atributos da Tabela:
    - **id** (`int`): Chave primária, identificador único do quadro.
    - **delete** (`bool`): Indicador lógico para exclusão suave do quadro.
    - **nome** (`str`): O nome do quadro (ex: "Projeto A", "Tarefas Pessoais").

    ### Relacionamentos:
    - **colunas** (`List[Coluna]`):
      Um relacionamento um-para-muitos com a tabela `colunas`.
      Quando um quadro é excluído, todas as suas colunas associadas
      também são excluídas (`cascade="all, delete-orphan"`).
    """

    __tablename__ = "quadros"

    id = Column(Integer, primary_key=True, index=True)
    delete = Column(Boolean, default=False)
    nome = Column(String, nullable=False)

    colunas = relationship(
        "Coluna", back_populates="quadro", cascade="all, delete-orphan"
    )
