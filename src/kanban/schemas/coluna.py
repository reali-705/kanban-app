"""
Módulo de Schemas Pydantic para a entidade Coluna.

Este arquivo define os modelos de dados Pydantic que governam a
validação e serialização dos dados de 'Coluna' na API. Eles atuam
como um contrato de dados, garantindo que os dados que entram e saem
da aplicação sigam uma estrutura predefinida e segura.
"""

from typing import List

from pydantic import BaseModel, ConfigDict, Field

from .cartao import Cartao


class Base(BaseModel):
    """
    **Schema base para uma Coluna.**

    Contém todos os campos que são compartilhados entre a criação e a
    leitura de uma coluna, servindo como uma única fonte da verdade.
    """

    nome: str = Field(..., min_length=1, description="O nome da coluna.")
    posicao: int = Field(..., description="A posição da coluna no quadro Kanban.")


class ColunaCreate(Base):
    """
    **Schema para a criação de uma nova Coluna (contrato de entrada).**

    Usado para validar os dados enviados pelo cliente em uma requisição POST.
    Herda os campos de `ColunaBase` e adiciona o `quadro_id` para
    saber a qual quadro a nova coluna pertence.
    """

    quadro_id: int


class Coluna(Base):
    """
    **Schema para a representação de uma Coluna (contrato de saída).**

    Usado como `response_model` para formatar os dados que a API envia
    ao cliente. Herda de `ColunaBase` e inclui campos gerados pelo servidor,
    como o `id`, e a lista de cartões aninhados.
    """

    id: int
    quadro_id: int
    cartoes: List[Cartao] = []

    model_config = ConfigDict(from_attributes=True)
