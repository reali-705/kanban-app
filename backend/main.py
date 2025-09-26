from fastapi import FastAPI
from .database import engine, Base

# Importa os modelos para que o SQLAlchemy saiba sobre eles
from . import models

# --- Criação das Tabelas no Banco de Dados ---
# Esta linha é crucial. Ela pega todos os modelos que herdam de 'Base'
# (em models.py) e os cria como tabelas no banco de dados conectado ao 'engine'.
# Isso só precisa ser feito uma vez. Se as tabelas já existirem, nada acontece.
Base.metadata.create_all(bind=engine)

# --- Instância da Aplicação FastAPI ---
app = FastAPI(
    title="API do Kanban Pessoal",
    description="Uma API para gerenciar quadros Kanban, colunas e cartões.",
    version="0.1.0",
)

# --- Endpoint Raiz ---
# Este é um endpoint de teste para verificar se a API está online.
@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna uma mensagem de boas-vindas.
    Útil para verificar rapidamente se o servidor está no ar.
    """
    return {"message": "Bem-vindo à API do Kanban!"}
