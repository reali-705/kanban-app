"""
Módulo de Modelo ORM para a entidade Cartão.

Este arquivo define a classe `Cartao`, que mapeia para a tabela "cartoes"
no banco de dados usando o ORM do SQLAlchemy. Cada instância desta classe
representa um registro (uma linha) na tabela.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from kanban.database import Base


class Cartao(Base):
    """
    Representa um cartão de tarefa individual na tabela `cartoes`.

    Um cartão é a unidade de trabalho que se move através das colunas.

    ### Atributos da Tabela:
    - **id** (`int`): Chave primária, identificador único do cartão.
    - **titulo** (`str`): O título do cartão.
    - **descricao** (`Optional[str]`): A descrição detalhada da tarefa.
    - **responsavel** (`Optional[str]`): A pessoa ou equipe responsável.
    - **cor** (`Optional[str]`): Uma cor para destaque visual.
    - **coluna_id** (`int`): Chave estrangeira que referencia `colunas.id`.

    ### Relacionamentos:
    - **coluna** (`Coluna`):
      Um relacionamento de volta para a `Coluna` à qual este cartão pertence.
    """

    __tablename__ = "cartoes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    responsavel = Column(String, nullable=True)
    cor = Column(String, nullable=True)
    coluna_id = Column(Integer, ForeignKey("colunas.id"), nullable=False)

    coluna = relationship("Coluna", back_populates="cartoes")
