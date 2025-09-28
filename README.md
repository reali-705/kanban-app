# Testes Automatizados com Pytest

Este diretório é dedicado à garantia de qualidade do código do backend. Utilizamos o framework [Pytest](https://pytest.org/) para escrever e executar testes de forma eficiente, garantindo que a API se comporte como esperado e que novas alterações não introduzam bugs (regressão).

Nossa estratégia de testes é dividida em categorias para cobrir diferentes aspectos da aplicação.

## 📂 Estrutura e Organização

Os testes são organizados em subdiretórios que refletem o tipo de teste, facilitando a navegação e a execução de conjuntos específicos.

```
tests/
├── conftest.py              # Fixtures e configurações globais do Pytest
├── api/                     # Testes de ponta-a-ponta para os endpoints da API
├── integration/             # Testes de integração entre múltiplos componentes
└── unit/                    # Testes de unidades para funções ou classes isoladas
```

### O Papel do `conftest.py`

O arquivo `conftest.py` é um arquivo especial do Pytest que nos permite compartilhar "fixtures" entre múltiplos arquivos de teste. Uma **fixture** é uma função que prepara um ambiente ou dados necessários para um ou mais testes.

Por exemplo, em vez de criar uma nova conexão com o banco de dados de teste em cada arquivo, nós definimos uma fixture no `conftest.py`. O Pytest então injeta essa fixture automaticamente em qualquer função de teste que a solicite. Isso torna os testes mais limpos, mais rápidos e evita a duplicação de código de configuração.

## ⚙️ Configuração Central com `pytest.ini`

O arquivo `pytest.ini`, localizado na raiz do projeto, centraliza as configurações do Pytest.

**Exemplo do `pytest.ini`:**

```ini
[pytest]
testpaths = tests
addopts = -v -x --strict-markers

markers =
    unit: Testes de unidade.
    integration: Testes de integração.
    api: Testes de API.
    kanban: Testes do objeto Kanban.
    coluna: Testes do objeto Coluna.
```

### Entendendo as Opções (`addopts`)

A linha `addopts` adiciona argumentos de linha de comando padrão a cada execução do Pytest:

  * `-v` (`--verbose`): Aumenta a verbosidade. Em vez de pontos, mostra o nome completo de cada teste e se ele passou ou falhou, fornecendo uma saída mais detalhada.
  * `-x` (`--exitfirst`): Parar na primeira falha. Assim que um teste falha, o Pytest interrompe a execução imediatamente. É útil para depurar, pois foca a atenção no primeiro erro que ocorreu.
  * `--strict-markers`: Garante que todos os marcadores usados no código (`@pytest.mark.<nome>`) estejam registrados na seção `markers` do `pytest.ini`. Isso evita erros de digitação e mantém a consistência das categorias de teste.

## 🏷️ Marcando os Testes (`@pytest.mark`)

Com os marcadores registrados, podemos "etiquetar" nossas funções de teste usando o decorador `@pytest.mark.<nome_do_marcador>`. Um mesmo teste pode receber múltiplos marcadores.

**Exemplo prático e genérico:**

```python
import pytest

# Teste com múltiplos marcadores
@pytest.mark.api
@pytest.mark.kanban
def test_funcao_a():
    # ... lógica do teste ...
    pass

# Teste com um único marcador
@pytest.mark.unit
def test_funcao_b():
    # ... lógica do teste ...
    pass
```

## ⚡ Executando Testes de Forma Seletiva

Para executar subconjuntos de testes, você pode usar a opção `-m` (marker) no terminal. O Pytest aceita os operadores lógicos `and`, `or` e `not` para criar expressões complexas e filtrar exatamente o que você precisa.

| Comando | Descrição |
| :--- | :--- |
| `pytest` | Executa **TODOS** os testes encontrados no diretório `tests`. |
| `pytest -m api` | Executa **APENAS** os testes marcados com `@pytest.mark.api`. |
| `pytest -m "api and kanban"` | Executa apenas os testes que possuem **AMBOS** os marcadores, `api` E `kanban`. |
| `pytest -m "kanban or coluna"` | Executa os testes que possuem o marcador `kanban` **OU** o marcador `coluna`. |
| `pytest -m "not unit"` | Executa todos os testes, **EXCETO** aqueles marcados como `unit`. |

---

[↩️ Voltar para a raiz do projeto](../)