"""
Configuração dos fixtures e ambiente de teste para o backend Kanban.

Este arquivo prepara o banco de dados temporário, configura as dependências
do FastAPI para usar o banco de teste e garante o isolamento entre os testes.
"""

import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from kanban.config import Settings
from kanban.database import get_db, Base
from kanban.main import app

# Sobrescreve as configurações específicas para o banco de teste
test_settings = Settings(
    _env_file=".env.test", _env_file_encoding="utf-8", extra="ignore"
)

# Cria engine e sessão para o banco de teste
engine_test = create_engine(
    test_settings.DATABASE_URL, connect_args={"check_same_thread": False}
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
    with TestClient(app) as test_cliente:
        yield test_cliente


def pytest_sessionfinish():
    """
    Remove o arquivo do banco de teste ao final da sessão de testes.
    """
    engine_test.dispose()

    db_path = test_settings.DATABASE_URL.rsplit("///", 1)[-1]
    if os.path.exists(db_path):
        os.remove(db_path)
