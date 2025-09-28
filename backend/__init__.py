"""
Inicializador do pacote 'backend'.

Este arquivo torna o diretório 'backend' um pacote Python e expõe
componentes importantes de submódulos para simplificar as importações.
"""

# Expõe os componentes principais do database para importação direta a partir de 'backend'
from .database import ( # noqa: F401
    Base,
    SessionLocal,
    engine
)
from .models import ( # noqa: F401
    KanbanModelo,
    ColunaModelo,
    CartaoModelo
)
from .schemas import ( # noqa: F401
    KanbanCreateSchema,
    KanbanSchema,
    ColunaCreateSchema,
    ColunaSchema,
    CartaoCreateSchema,
    CartaoSchema
)
from .main import app, get_db  # noqa: F401

__all__ = [
    "Base", "SessionLocal", "engine",
    "app", "get_db",
    "KanbanModelo", "KanbanCreateSchema", "KanbanSchema",
    "ColunaModelo", "ColunaCreateSchema", "ColunaSchema",
    "CartaoModelo", "CartaoCreateSchema", "CartaoSchema"
]