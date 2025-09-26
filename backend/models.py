from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Kanban(Base):
    """
    Tabela: kanbans
    Representa um quadro Kanban completo (ex: "Projeto A", "Tarefas Pessoais")
    """
    __tablename__ = "kanbans"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    
    # Relacionamento: Um kanban tem muitas colunas
    colunas = relationship("Coluna", back_populates="kanban", cascade="all, delete-orphan")


class Coluna(Base):
    """
    Tabela: colunas
    Representa uma coluna dentro de um kanban (ex: "To Do", "In Progress", "Done")
    """
    __tablename__ = "colunas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    posicao = Column(Integer, nullable=False)  # Ordem das colunas no kanban
    kanban_id = Column(Integer, ForeignKey("kanbans.id"), nullable=False)
    
    # Relacionamentos
    kanban = relationship("Kanban", back_populates="colunas")  # Volta para o kanban pai
    cartoes = relationship("Cartao", back_populates="coluna", cascade="all, delete-orphan")  # Cartoes dentro desta coluna


class Cartao(Base):
    """
    Tabela: cartoes
    Representa um cartao individual dentro de uma coluna
    """
    __tablename__ = "cartoes"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)  # Pode ser nulo
    responsavel = Column(String, nullable=True)   # Pode ser nulo
    cor = Column(String, nullable=True)      # Pode ser nulo (ex: "#FF5733")
    coluna_id = Column(Integer, ForeignKey("colunas.id"), nullable=False)

    # Relacionamento: Volta para a coluna pai
    coluna = relationship("Coluna", back_populates="cartoes")
