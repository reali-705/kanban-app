"""
Módulo de Modelo ORM para a entidade Coluna.

Este arquivo define a classe `Coluna`, que mapeia para a tabela "colunas"
no banco de dados usando o ORM do SQLAlchemy. Cada instância desta classe
representa um registro (uma linha) na tabela.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from kanban.database import Base


class Coluna(Base):
    """
    Representa uma coluna dentro de um quadro na tabela `colunas`.

    Uma coluna é um estágio do fluxo de trabalho (ex: "A Fazer", "Em Progresso").

    ### Atributos da Tabela:
    - **id** (`int`): Chave primária, identificador único da coluna.
    - **nome** (`str`): O nome da coluna.
    - **posicao** (`int`): A ordem da coluna dentro do quadro.
    - **quadro_id** (`int`): Chave estrangeira que referencia `quadros.id`.

    ### Relacionamentos:
    - **quadro** (`Quadro`):
      Um relacionamento de volta para o `Quadro` ao qual esta coluna pertence.
    - **cartoes** (`List[Cartao]`):
      Um relacionamento um-para-muitos com a tabela `cartoes`.
      Quando uma coluna é excluída, todos os seus cartões associados
      também são excluídos (`cascade="all, delete-orphan"`).
    """

    __tablename__ = "colunas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    posicao = Column(Integer, nullable=False)
    quadro_id = Column(Integer, ForeignKey("quadros.id"), nullable=False)

    quadro = relationship("Quadro", back_populates="colunas")
    cartoes = relationship(
        "Cartao", back_populates="coluna", cascade="all, delete-orphan"
    )
