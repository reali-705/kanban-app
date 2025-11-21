"""
Módulo de Configuração Centralizado.

Este arquivo define e carrega as configurações da aplicação a partir de
variáveis de ambiente e do arquivo .env, utilizando Pydantic Settings
para validação e tipagem.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    **Configurações da aplicação carregadas de variáveis de ambiente.**

    Define as variáveis que a aplicação espera encontrar no ambiente ou
    no arquivo .env.
    """

    # O valor padrão aqui serve como fallback caso a variável não seja definida no .env
    DATABASE_URL: str = "sqlite:///./kanban.db"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Instância única que será usada em toda a aplicação
settings = Settings()
