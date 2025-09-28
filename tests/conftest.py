"""
Configuração dos fixtures e ambiente de teste para o backend Kanban.

Este arquivo prepara o banco de dados temporário, configura as dependências
do FastAPI para usar o banco de teste e garante o isolamento entre os testes.
"""

import os
import pytest
from backend import app, get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

# Caminho fixo para o banco de dados de teste
PATH_TESTE_DB = "tests/teste.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{PATH_TESTE_DB}"

# Cria engine e sessão para o banco de teste
engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

def get_db_test():
    """
    Dependência sobrescrita do FastAPI para fornecer sessões do banco de teste.
    """
    try:
        db_test = SessionLocalTest()
        yield db_test
    finally:
        db_test.close()

# Redireciona todas as dependências do backend para o banco de teste
app.dependency_overrides[get_db] = get_db_test

@pytest.fixture(scope="function", autouse=True)
def preparar_db_temporario():
    """
    Cria e remove as tabelas do banco de teste antes e depois de cada teste,
    garantindo ambiente limpo e isolado.
    """
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)

@pytest.fixture(scope="function")
def cliente():
    """
    Fornece um cliente HTTP para simular requisições à API durante os testes.
    """
    with TestClient(app) as cliente:
        yield cliente

def pytest_sessionfinish(session, exitstatus):
    """
    Remove o arquivo do banco de teste ao final da sessão de testes.
    """
    engine_test.dispose()
    if os.path.exists(PATH_TESTE_DB):
        os.remove(PATH_TESTE_DB)