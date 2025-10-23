# Anotações das aulas


## Aula 1 - Configurando o ambiente
url: https://fastapidozero.dunossauro.com/4.0/01/#__tabbed_1_2
comandos instalar poetry e pipx (pip com executáveis):
    sudo apt install pipx
    ensurepath pipx
    pipx install poetry
    export PATH="$HOME/.local/bin:$PATH"

Executando poetry:
    poetry self add poetry-plugin-shell
    poetry new fastapi_zero
    cd fastapi_zero
    poetry python install 3.13 # Estbaliza versão do python no poetry
    poetry python list  # Checa as versões
    poetry env use 3.13
    poetry env info # Verifica versão utilizada

Instalando poetry
    poetry install # Esse comando gera o lock, já tendo as bibiotecas, ele baixa tudo
    poetry add 'fastapi[standard]'
    poetry env info --path # Só para saber o path do .env para incluir no interpretador
    poetry shell # Abre ambiente virtual
    ou usar poetry run

Executando hello world do fast api
    poetry install

    python3 -i src/fastapi_zero/app.py
    ou
    fastapi dev src/fastapi_zero/app.py
    ou
    usar poetry run src/fastapi_zero/app.py # fora do ambiente virtual

    obs:
        Sempre que usarmos o fastapi para inicializar a aplicação no shell, ele faz uma chamada interna para inicializar o uvicorn. 
        poderia ser: uvicorn fast_zero.app:app

Endpoints do fast api
    - http://127.0.0.1:8000/ # get root
    - http://127.0.0.1:8000/docs # Swagger (Executável)
    - http://127.0.0.1:8000/redoc # REDOC (endpoints e resposta mais detalhada)

Instalando ferramentas
    poetry add --group dev pytest pytest-cov taskipy ruff

    Sobre as ferramentas:
        - taskipy: ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc. (É o makefile mais pythonico)
        - pytest: ferramenta para escrever e executar testes.
        - ruff: Uma ferramenta que tem duas funções no nosso código:
          - Um analisador estático de código (um linter), para dizer se não estamos infringindo alguma boa prática de programação;  
          - Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.
  
ruff:
    O linter do ruff
        Durante a análise estática do código, queremos buscar por coisas específicas. No Ruff, precisamos dizer exatamente o que ele deve analisar.

        I (Isort): ordenação de imports em ordem alfabética
        F (Pyflakes): procura por alguns erros em relação a boas práticas de código
        E (pycodestyle): erros de estilo de código
        W (pycodestyle): avisos sobre estilo de código
        PL (Pylint): "erros" em relação a boas práticas de código
        PT (flake8-pytest): boas práticas do Pytest

    comandos:
        - ruff check . # Checa se ta tudo bem no linter
        - ruff format . # formata problema resolvíveis de formatação (definido no ruff.format)
pytest:
    - pytest
    - pytest --cov=src/fastapi_zero -vv # Verifica cobertura de código do teste
    - coverage html # Exporta relatório de cobertura em html

Taskypiy:
    - task tun # para rodar o servidor
    - task test # para testar o servidor
Commitar:
    - pipx run ignr -p python > .gitignore
    - git init .
    - gh repo create