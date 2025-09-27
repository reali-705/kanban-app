"""
Ponto de entrada principal da aplicação FastAPI.

Este arquivo é responsável por criar a instância da aplicação,
criar as tabelas no banco de dados na inicialização e definir
os endpoints (rotas) da API.
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from . import (
    Base,
    SessionLocal,
    engine,
    KanbanModelo,
    KanbanCreateSchema,
    KanbanSchema,
    # ColunaModelo,
    # ColunaCreateSchema,
    # ColunaSchema,
    # CartaoModelo,
    # CartaoCreateSchema,
    # CartaoSchema
)

# Cria as tabelas no banco de dados (se não existirem) ao iniciar a aplicação.
Base.metadata.create_all(bind=engine)

# Instancia a aplicação FastAPI com metadados para a documentação.
app = FastAPI(
    title="API do Kanban Pessoal",
    description="Uma API para gerenciar quadros Kanban, colunas e cartões.",
    version="0.1.0",
)

# --- Dependência para obter a sessão do banco de dados ---
def get_db():
    """
    Cria e fornece uma sessão de banco de dados por requisição.
    Garante que a sessão seja sempre fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoints para Kanban ---

@app.post("/kanbans/", response_model=KanbanSchema)
def criar_kanban(kanban: KanbanCreateSchema, db: Session = Depends(get_db)):
    """
    Cria um novo quadro Kanban.
    """
    # Cria uma instância do modelo SQLAlchemy a partir dos dados do schema
    db_kanban = KanbanModelo(nome=kanban.nome)
    db.add(db_kanban)  # Adiciona o novo objeto à sessão
    db.commit()       # Confirma a transação, salvando no banco
    db.refresh(db_kanban) # Atualiza o objeto com os dados do banco (como o novo ID)
    return db_kanban

@app.get("/kanbans/", response_model=List[KanbanSchema])
def ler_todos_kanbans(db: Session = Depends(get_db)):
    """
    Retorna uma lista de todos os quadros Kanban.
    """
    kanbans = db.query(KanbanModelo).all()
    return kanbans

@app.get("/")
def boas_vindas():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": "Bem-vindo à API do Kanban!"}
