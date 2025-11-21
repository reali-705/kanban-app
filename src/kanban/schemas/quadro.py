"""
Módulo de Schemas Pydantic para a entidade Quadro.

Este arquivo define os modelos de dados Pydantic que governam a
validação e serialização dos dados de 'Quadro' na API. Eles atuam
como um contrato de dados, garantindo que os dados que entram e saem
da aplicação sigam uma estrutura predefinida e segura.
"""

from typing import List

from pydantic import BaseModel, ConfigDict, Field

from .coluna import Coluna


class Base(BaseModel):
    """
    **Schema base para um Quadro.**

    Contém todos os campos que são compartilhados entre a criação e a
    leitura de um quadro, servindo como uma única fonte da verdade.
    """

    nome: str = Field(..., min_length=1, description="O nome do quadro Quadro.")


class QuadroCreate(Base):
    """
    **Schema para a criação de um novo Quadro (contrato de entrada).**

    Usado para validar os dados enviados pelo cliente em uma requisição POST.
    Atualmente, herda todos os campos de `QuadroBase` sem adicionar novos.
    """


class Quadro(Base):
    """
    **Schema para a representação de um Quadro (contrato de saída).**

    Usado como `response_model` para formatar os dados que a API envia
    ao cliente. Herda de `QuadroBase` e inclui campos gerados pelo servidor,
    como o `id`, e a lista de colunas aninhadas.
    """

    id: int
    delete: bool
    colunas: List[Coluna] = []
    model_config = ConfigDict(from_attributes=True)
