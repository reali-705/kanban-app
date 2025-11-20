"""
Módulo de Schemas Pydantic para a entidade Cartão.

Este arquivo define os modelos de dados Pydantic que governam a
validação e serialização dos dados de 'Cartão' na API. Eles atuam
como um contrato de dados, garantindo que os dados que entram e saem
da aplicação sigam uma estrutura predefinida e segura.
"""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CartaoBase(BaseModel):
    """
    **Schema base para um Cartão.**

    Contém todos os campos que são compartilhados entre a criação e a
    leitura de um cartão.
    """

    titulo: str = Field(..., min_length=1, description="O título do cartão.")
    descricao: Optional[str] = Field(
        None, description="A descrição detalhada do cartão."
    )
    responsavel: Optional[str] = Field(
        None, description="A pessoa ou equipe responsável pelo cartão."
    )
    cor: Optional[str] = Field(
        None, description="A cor de destaque do cartão (ex: '#FFFFFF')."
    )


class CartaoCreate(CartaoBase):
    """
    **Schema para a criação de um novo Cartão (contrato de entrada).**

    Usado para validar os dados enviados pelo cliente em uma requisição POST.
    Herda os campos de `CartaoBase` e adiciona os campos necessários
    apenas no momento da criação. Não inclui o `id`, pois ele ainda não
    existe e será gerado pelo banco de dados.
    """

    coluna_id: int


class Cartao(CartaoBase):
    """
    **Schema para a representação de um Cartão (contrato de saída).**

    Usado como `response_model` para formatar os dados que a API envia
    ao cliente. Herda os campos de `CartaoBase` e inclui os campos que
    são gerados e controlados pelo servidor, como o `id`.
    """

    id: int
    coluna_id: int

    model_config = ConfigDict(from_attributes=True)
