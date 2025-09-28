"""
Inicializador do pacote 'backend'.

Este arquivo torna o diretório 'backend' um pacote Python e expõe
componentes importantes de submódulos para simplificar as importações.
"""

# Expõe os componentes principais do database para importação direta a partir de 'backend'
from .main import app, get_db  # noqa: F401
from .schemas import (  # noqa: F401
    Base,
    SessionLocal,
    engine,
    KanbanModelo,
    KanbanCreateSchema,
    KanbanSchema,
    ColunaModelo,
    ColunaCreateSchema,
    ColunaSchema,
    CartaoModelo,
    CartaoCreateSchema,
    CartaoSchema
)
