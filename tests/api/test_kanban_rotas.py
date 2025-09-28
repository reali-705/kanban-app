"""
Testes automatizados para as rotas do recurso Kanban.

Este arquivo cobre os principais cenários de uso da API Kanban,
incluindo criação, leitura e validação dos dados enviados.
"""

import pytest

def test_ler_kanbans_vazio(cliente):
    """Verifica se a lista de kanbans está vazia ao iniciar o banco."""
    resposta = cliente.get("/kanbans/")
    assert resposta.status_code == 200
    assert resposta.json() == []

def test_ler_kanbans_com_registro(cliente):
    """Testa se um kanban criado aparece na listagem."""
    cliente.post("/kanbans/", json={"nome": "Kanban 1"})
    resposta = cliente.get("/kanbans/")
    assert resposta.status_code == 200
    lista = resposta.json()
    assert len(lista) == 1
    assert lista[0]["nome"] == "Kanban 1"

@pytest.mark.parametrize(
    "payload, status_code, expected_keys, unexpected_keys",
    [
        # Teste com nome válido
        ({"nome": "Meu Kanban de Teste"}, 200, ["nome", "id"], []),
        # Teste com campo extra
        ({"nome": "Kanban Extra", "cor": "azul"}, 200, ["nome", "id"], ["cor"]),
        # Teste com nome vazio
        ({"nome": ""}, 422, [], []),
        # Teste com nome não string
        ({"nome": 123}, 422, [], []),
        # Teste sem nome
        ({}, 422, [], []),
    ]
)
def test_criar_kanban_parametrizado(cliente, payload, status_code, expected_keys, unexpected_keys):
    """
    Testa a criação de kanban com diferentes cenários de dados enviados.
    Valida resposta da API e presença/ausência de chaves esperadas.
    """
    resposta = cliente.post("/kanbans/", json=payload)
    assert resposta.status_code == status_code
    if status_code == 200:
        dados = resposta.json()
        for key in expected_keys:
            assert key in dados
        for key in unexpected_keys:
            assert key not in dados