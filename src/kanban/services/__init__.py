"""
Pacote de Serviços para a entidade Quadro.
"""

from .quadro import (
    criar as criar_quadro,
    ler_todos as ler_todos_quadros,
)

__all__ = [
    "criar_quadro",
    "ler_todos_quadros",
]
