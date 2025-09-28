# Testes Automatizados Kanban Pessoal

Este diretório contém todos os testes automatizados do projeto Kanban Pessoal, organizados para facilitar manutenção e expansão.

## Estrutura

- **unit/**: Testes de unidade para funções e modelos isolados.
- **integration/**: Testes de integração entre componentes do backend.
- **api/**: Testes de API simulando requisições HTTP aos endpoints.
- **conftest.py:** Configuração do ambiente de testes, incluindo banco SQLite temporário e fixtures.
- **pytest.ini:** Configuração de marcadores e argumentos padrão para o pytest.

## Convenções

- Uso de marcadores para selecionar testes por nível e objeto.
- Ambiente de testes isolado, garantindo que cada execução seja independente.
- Facilidade para rodar apenas um tipo de teste usando comandos como:
  ```powershell
  pytest -m "unit and kanban"
  ```

[Voltar para a raiz do projeto](../README.md)