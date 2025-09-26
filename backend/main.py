"""
Ponto de entrada principal da aplicação FastAPI.

Este arquivo é responsável por criar a instância da aplicação,
criar as tabelas no banco de dados na inicialização e definir
os endpoints (rotas) da API.
"""

from fastapi import FastAPI
from .database import engine, Base
from . import models  # noqa: F401

# Cria as tabelas no banco de dados (se não existirem) ao iniciar a aplicação.
Base.metadata.create_all(bind=engine)

# Instancia a aplicação FastAPI com metadados para a documentação.
app = FastAPI(
    title="API do Kanban Pessoal",
    description="Uma API para gerenciar quadros Kanban, colunas e cartões.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": "Bem-vindo à API do Kanban!"}
