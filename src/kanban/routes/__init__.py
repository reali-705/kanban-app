"""
Pacote de rotas para a aplicação Kanban.
"""

from .quadro import rotas_quadros as quadros
from .coluna import rotas_colunas as colunas
from .cartao import rotas_cartoes as cartoes

__all__ = ["quadros", "colunas", "cartoes"]
