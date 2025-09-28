def test_criar_kanban(cliente):
    payload = {"nome": "Meu Kanban de Teste"}
    resposta = cliente.post("/kanbans/", json=payload)
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["nome"] == "Meu Kanban de Teste"
    assert "id" in dados

def test_ler_kanbans_vazio(cliente):
    resposta = cliente.get("/kanbans/")
    assert resposta.status_code == 200
    assert resposta.json() == []

def test_ler_kanbans_com_registro(cliente):
    cliente.post("/kanbans/", json={"nome": "Kanban 1"})
    resposta = cliente.get("/kanbans/")
    assert resposta.status_code == 200
    lista = resposta.json()
    assert len(lista) == 1
    assert lista[0]["nome"] == "Kanban 1"

def test_criar_kanban_nome_nao_string(cliente):
    payload = {"nome": 123}
    resposta = cliente.post("/kanbans/", json=payload)
    assert resposta.status_code == 422  # Erro de validação do FastAPI

def test_criar_kanban_campo_extra(cliente):
    payload = {"nome": "Kanban Extra", "cor": "azul"}
    resposta = cliente.post("/kanbans/", json=payload)
    assert resposta.status_code == 200  # FastAPI ignora campos extras por padrão
    dados = resposta.json()
    assert dados["nome"] == "Kanban Extra"
    assert "cor" not in dados

def test_criar_kanban_sem_nome(cliente):
    payload = {}
    resposta = cliente.post("/kanbans/", json=payload)
    assert resposta.status_code == 422  # Campo obrigatório faltando