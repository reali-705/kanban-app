# Kanban Pessoal - Um Gerenciador de Tarefas Local

Este projeto é um gerenciador de tarefas pessoal no estilo Kanban, desenvolvido com foco em aprendizado e uso prático. A proposta é criar uma aplicação desktop para Windows que seja simples, privada e totalmente autocontida, sem depender de serviços na nuvem.

O desenvolvimento serve como um exercício prático de habilidades full-stack, combinando um backend robusto com uma interface gráfica reativa.

## ✨ Proposta e Objetivos

-   **Privacidade em Primeiro Lugar:** Seus dados são seus. Tudo é armazenado localmente em um arquivo de banco de dados, garantindo total controle e privacidade.
-   **Simplicidade e Foco:** Uma ferramenta para organizar tarefas sem a complexidade e as distrações de soluções corporativas.
-   **Desenvolvimento e Aprendizado:** Servir como um projeto de portfólio para testar e aprimorar habilidades em desenvolvimento de software, desde a API até a interface do usuário.
-   **Escalabilidade:** Construído sobre uma base sólida e modular, permitindo que novas funcionalidades sejam adicionadas facilmente no futuro.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** [Python](https://www.python.org/) com [FastAPI](https://fastapi.tiangolo.com/)
-   **Frontend:** [Flet](https://flet.dev/) (para a interface gráfica em Python)
-   **Banco de Dados:** [SQLite](https://www.sqlite.org/index.html) (para armazenamento local)
-   **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) (para interação com o banco de dados)

## 🚀 Como Começar (Ambiente de Desenvolvimento)

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### 1. Pré-requisitos

-   [Python 3.8+](https://www.python.org/downloads/) instalado e adicionado ao PATH do sistema.
-   [Git](https://git-scm.com/downloads) instalado.

### 2. Clonar o Repositório

Abra um terminal (como o PowerShell) e clone este repositório:

```powershell
git clone https://github.com/reali-705/kanban-app.git
cd kanban-app
```

### 3. Configurar o Ambiente Virtual e Instalar Dependências

O projeto inclui um script PowerShell para automatizar a configuração. Execute-o:

```powershell
.\setup.ps1
```

Este comando irá:
- Criar um ambiente virtual chamado `.venv`.
- Ativar o ambiente.
- Instalar todas as dependências listadas em `requirements.txt`.

### 4. Executar o Servidor da API

Com o ambiente configurado, inicie o servidor de desenvolvimento do backend:

```powershell
# Ative o ambiente virtual (caso não esteja ativo): .\.venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload
```

O servidor estará rodando em `http://127.0.0.1:8000`.

### 5. Acessar a Documentação da API

Para testar os endpoints e ver a documentação interativa (Swagger UI), acesse:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

