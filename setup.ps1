
# Início do processo de configuracao do ambiente do projeto Kanban-app
Write-Host "Iniciando a configuracao do ambiente virtual do projeto Kanban-app..." -ForegroundColor Green

# Passo 1: Verifica se o Python esta instalado no sistema
Write-Host "Verificando se o Python esta instalado..."
$python_path = Get-Command python -ErrorAction SilentlyContinue
if (-not $python_path) {
    Write-Host "ERRO: Python nao encontrado no seu sistema." -ForegroundColor Red
    Write-Host "Por favor, instale o Python 3.8+ a partir do site oficial: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Depois da instalacao, certifique-se de que ele foi adicionado ao PATH do sistema e execute este script novamente."
    exit 1
} else {
    Write-Host "Python encontrado em: $($python_path.Source)" -ForegroundColor Green
}

# Passo 2: Define o nome da pasta do ambiente virtual
$venv_dir = ".venv"

# Passo 3: Cria o ambiente virtual, caso ainda nao exista
if (-not (Test-Path $venv_dir)) {
    Write-Host "Ambiente virtual nao encontrado. Criando o ambiente '$venv_dir'..." -ForegroundColor Yellow
    python -m venv $venv_dir
    if ($?) {
        Write-Host "Ambiente virtual criado com sucesso." -ForegroundColor Green
    } else {
        Write-Host "Falha ao criar o ambiente virtual." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "O ambiente virtual ja existe. Prosseguindo com a configuracao." -ForegroundColor Cyan
}

# Passo 4: Ativa o ambiente virtual para a sessao atual do PowerShell
Write-Host "Ativando o ambiente virtual..." -ForegroundColor Yellow
. ".\$venv_dir\Scripts\Activate.ps1"

if ($?) {
    Write-Host "Ambiente virtual ativado." -ForegroundColor Green
} else {
    Write-Host "Falha ao ativar o ambiente virtual." -ForegroundColor Red
    exit 1
}

# Passo 5: Instala as dependencias do projeto listadas no requirements.txt
Write-Host "Instalando as dependencias do projeto (requirements.txt)..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($?) {
    Write-Host "Dependencias instaladas com sucesso." -ForegroundColor Green
    Write-Host "Para ativar o ambiente virtual manualmente em futuras sessoes, execute: .\$venv_dir\Scripts\Activate.ps1" -ForegroundColor Cyan
} else {
    Write-Host "Falha ao instalar as dependencias." -ForegroundColor Red
    exit 1
}