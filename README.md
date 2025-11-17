# Kanban Pessoal - Um Gerenciador de Tarefas Local

Este projeto é um gerenciador de tarefas pessoal no estilo Kanban, desenvolvido com foco em aprendizado e uso prático. A proposta é criar uma aplicação desktop para Windows que seja simples, privada e totalmente autocontida, sem depender de serviços na nuvem.

O desenvolvimento serve como um exercício prático de habilidades full-stack, combinando um backend robusto com uma interface gráfica reativa.

## ✨ Proposta e Objetivos

- **Privacidade em Primeiro Lugar:** Seus dados são seus. Tudo é armazenado localmente em um arquivo de banco de dados, garantindo total controle e privacidade.
- **Simplicidade e Foco:** Uma ferramenta para organizar tarefas sem a complexidade e as distrações de soluções corporativas.
- **Desenvolvimento e Aprendizado:** Servir como um projeto de portfólio para testar e aprimorar habilidades em desenvolvimento de software, desde a API até a interface do usuário.
- **Escalabilidade:** Construído sobre uma base sólida e modular, permitindo que novas funcionalidades sejam adicionadas facilmente no futuro.

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando um conjunto de bibliotecas Python modernas para garantir um desenvolvimento robusto e eficiente.

| Biblioteca | Versão | Descrição | Diretório de Uso |
| :--- | :--- | :--- | :--- |
| **fastapi** | 0.117.1 | Um framework web moderno e de alta performance para construir APIs com Python. | [`/src/kanban/`](/src/kanban/) |
| **flet** | 0.28.3 | Permite criar aplicações web, desktop e mobile interativas em Python. | [`/frontend/`](/frontend/) |
| **uvicorn** | 0.37.0 | Um servidor web ASGI (Asynchronous Server Gateway Interface) para Python. | Usado para rodar a API |
| **SQLAlchemy** | 2.0.43 | Um toolkit SQL e Object Relational Mapper (ORM) para Python. | [`/src/kanban/database.py`](/src/kanban/database.py) |
| **pytest** | 8.4.2 | Um framework que torna a construção de testes simples e escaláveis. | [`/tests/`](/tests/) |

## 📂 Estrutura de Diretórios

O projeto está organizado da seguinte forma para separar as responsabilidades e facilitar a manutenção:

```
kanban-app/
├── src/                # Código-fonte da aplicação
│   └── kanban/         # Lógica central da aplicação (API)
│       ├── main.py     # Ponto de entrada e inicialização da API
│       ├── database.py # Configuração da conexão com o banco de dados
│       ├── models/     # Modelos de dados do SQLAlchemy
│       ├── routes/     # Manipulação de requisições HTTP (FastAPI Routers)
│       ├── schemas/    # Schemas de validação de dados (Pydantic)
│       └── services/   # Lógica de Negócio (CRUD)
├── frontend/           # Interface Gráfica com Flet (a ser implementada)
├── tests/              # Testes automatizados (Unit, Integration, API)
├── .vscode/            # Configurações do ambiente de desenvolvimento (Tasks, Launch)
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── pyproject.toml      # Arquivo de configuração central do projeto e dependências
├── setup.ps1           # Script PowerShell para setup inicial
└── LICENSE             # Licença MIT (Direitos Autorais)
```

  * [`/src/kanban/`](/src/kanban/): Contém toda a lógica da API, incluindo a configuração do servidor com FastAPI, a conexão com o banco de dados via SQLAlchemy, os modelos de dados e as rotas da aplicação.
  * [`/tests/`](/tests/): Inclui todos os testes automatizados do projeto, escritos com Pytest, para garantir a qualidade e o funcionamento correto da API e de suas funcionalidades.

## 🛠️ Como Começar (Ambiente Automatizado)

Para configurar e executar o projeto de forma rápida, você pode usar os scripts e configurações de automação incluídos.

### 1\. Configuração Inicial

Primeiro, clone o repositório para a sua máquina local.

```bash
git clone https://github.com/reali-705/kanban-app.git
cd kanban-app
code .
```

### 2\. Setup Automatizado com PowerShell

O projeto inclui um script `setup.ps1` que automatiza a criação do ambiente virtual e a instalação de todas as dependências. Para executá-lo, abra o PowerShell no diretório do projeto e digite:

```powershell
.\setup.ps1
```

<small>*Observação: Pode ser necessário alterar a política de execução de scripts do PowerShell com o comando `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.*</small>

Este comando irá:

  - Criar um ambiente virtual chamado `.venv`.
  - Ativar o ambiente.
  - Instalar o projeto em modo editável e todas as dependências (principais e de desenvolvimento) listadas no `pyproject.toml`.

### 3\. Usando Atalhos do VS Code (`tasks.json`)

Se você utiliza o Visual Studio Code, pode usar os atalhos configurados no arquivo `.vscode/tasks.json` para agilizar o desenvolvimento:

#### **Rodando os Testes**

Para garantir a qualidade e a integridade do código, você pode executar a suíte de testes automatizados.

  * **Configure um atalho** de sua preferência no VS Code para a tarefa **"Run Pytest"**.
  * Abra o menu de atalhos (`File > Preferences > Keyboard Shortcuts`), procure por `Tasks: Run Task` e adicione um atalho para a tarefa "Run Pytest".
  * Ao usar o atalho, todos os testes na pasta [`/tests`](/tests/) serão executados.

#### **Iniciando a API**

Para colocar o servidor do backend no ar:

  * Use o atalho padrão `Ctrl+Shift+B`.
  * Isso executará a tarefa **"Run API"**, que ativa o ambiente virtual e inicia o servidor Uvicorn automaticamente.

Após a inicialização, a API estará rodando em:
**`http://127.0.0.1:8000`**

Você pode interagir com a API e visualizar a documentação interativa gerada automaticamente pelo FastAPI acessando as seguintes URLs no seu navegador:

  - **Swagger UI:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
  - **ReDoc:** [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)

## ✒️ Autoria

Este projeto foi desenvolvido por [**Alessandro Reali**](https://github.com/reali-705).