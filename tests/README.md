# Testes Automatizados com Pytest

Este diretório é dedicado à garantia de qualidade do código do backend. Utilizamos o framework [Pytest](https://pytest.org/) para escrever e executar testes de forma eficiente, garantindo que a API se comporte como esperado e que novas alterações não introduzam bugs (regressão).

Nossa estratégia de testes é dividida em categorias para cobrir diferentes aspectos da aplicação, como testes de unidade, integração e de API.

## 📂 Estrutura e Organização

Os testes são organizados em subdiretórios que refletem o tipo de teste que está sendo executado, facilitando a navegação e a execução de conjuntos específicos de testes.

```
tests/
├── conftest.py              # Fixtures e configurações globais do Pytest
├── test_api/                # Testes de ponta-a-ponta para os endpoints da API
│   └── test_kanbans_api.py
└── test_unit/               # Testes de unidades para funções ou classes isoladas
    └── test_sample_unit.py
```

## ⚙️ Configuração Central com `pytest.ini`

O coração da nossa configuração de testes é o arquivo `pytest.ini`, localizado na raiz do projeto. Ele serve para centralizar as configurações do Pytest, garantindo que os testes rodem de maneira consistente para todos os desenvolvedores.

As duas seções mais importantes neste arquivo são:

1.  **`testpaths`**: Indica ao Pytest onde ele deve procurar por testes. No nosso caso, ele está configurado para olhar diretamente para este diretório (`tests`).
2.  **`markers`**: Aqui nós registramos nossos "marcadores" personalizados. Um marcador é como uma etiqueta que podemos colocar em nossos testes para categorizá-los.

**Exemplo do `pytest.ini`:**

```ini
[pytest]
testpaths = tests
addopts = -v --strict-markers

markers =
    unit: Testes de unidade.
    integration: Testes de integração.
    api: Testes de API.
    kanban: Testes do objeto Kanban.
    coluna: Testes do objeto Coluna.
```

## 🏷️ Marcando os Testes (`@pytest.mark`)

Com os marcadores registrados no `pytest.ini`, podemos agora "etiquetar" nossas funções de teste diretamente no código Python usando o decorador `@pytest.mark.<nome_do_marcador>`. Isso nos dá um controle granular sobre quais testes executar.

Um mesmo teste pode ter múltiplos marcadores.

**Exemplo prático em um arquivo de teste:**

```python
import pytest

# Este teste pertence à categoria 'api' e está relacionado ao 'kanban'
@pytest.mark.api
@pytest.mark.kanban
def test_criar_kanban_com_sucesso(cliente):
    # ... lógica do teste ...
    response = cliente.post("/kanbans/", json={"nome": "Meu Kanban"})
    assert response.status_code == 200

# Este teste é uma unidade e se relaciona à 'coluna'
@pytest.mark.unit
@pytest.mark.coluna
def test_validacao_nome_coluna():
    # ... lógica do teste ...
    assert True
```

## ⚡ Executando Testes de Forma Seletiva

A grande vantagem dessa estrutura é a capacidade de rodar apenas os testes que você precisa, economizando tempo. Abra o terminal na raiz do projeto e use os seguintes comandos:

| Comando | Descrição |
| :--- | :--- |
| `pytest` | Executa **TODOS** os testes encontrados no diretório `tests`. |
| `pytest -m api` | Executa **APENAS** os testes marcados com `@pytest.mark.api`. |
| `pytest -m "api and kanban"` | Executa apenas os testes que possuem **AMBOS** os marcadores, `api` E `kanban`. |
| `pytest -m "kanban or coluna"` | Executa os testes que possuem o marcador `kanban` **OU** o marcador `coluna`. |
| `pytest -m "not unit"` | Executa todos os testes, **EXCETO** aqueles marcados como `unit`. |

Essa flexibilidade é extremamente poderosa para focar em uma parte específica do sistema durante o desenvolvimento ou para criar pipelines de integração contínua mais eficientes.

-----

[↩️ Voltar para a raiz do projeto](https://www.google.com/search?q=../)