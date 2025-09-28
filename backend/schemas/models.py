"""
Modelos ORM (Object-Relational Mapping) do SQLAlchemy.

Este arquivo define as classes Python que representam as tabelas no banco de dados.
Cada classe corresponde a uma tabela e seus atributos correspondem às colunas.
O ORM permite interagir com o banco de dados usando objetos Python em vez de SQL bruto.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base


class KanbanModelo(Base):
    """
    Tabela: kanbans
    Representa um quadro Kanban completo (ex: "Projeto A", "Tarefas Pessoais")
    """
    __tablename__ = "kanbans"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    
    # Relacionamento com as colunas (um-para-muitos).
    colunas = relationship("ColunaModelo", back_populates="kanban", cascade="all, delete-orphan")

class ColunaModelo(Base):
    """
    Tabela: colunas
    Representa uma coluna dentro de um kanban (ex: "To Do", "In Progress", "Done")
    """
    __tablename__ = "colunas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    posicao = Column(Integer, nullable=False)
    kanban_id = Column(Integer, ForeignKey("kanbans.id"), nullable=False)
    
    # Relacionamentos de volta para o Kanban e para os Cartões.
    kanban = relationship("KanbanModelo", back_populates="colunas")
    cartoes = relationship("CartaoModelo", back_populates="coluna", cascade="all, delete-orphan")

class CartaoModelo(Base):
    """
    Tabela: cartoes
    Representa um cartao individual dentro de uma coluna
    """
    __tablename__ = "cartoes"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    responsavel = Column(String, nullable=True)
    cor = Column(String, nullable=True)
    coluna_id = Column(Integer, ForeignKey("colunas.id"), nullable=False)

    # Relacionamento de volta para a Coluna.
    coluna = relationship("ColunaModelo", back_populates="cartoes")
