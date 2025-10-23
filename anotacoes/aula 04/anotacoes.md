ORM:
    - Abstração de banco de dados: Mudar tipo de banco de dados sem mudar muito código
    - Segurança: Prevenção e esape de SQL injection
    - Eficiência no desenvolvimento: Não preocupar com detalhes de linguagens SQL diferentes

MODELS:
    - Cria os campos que tem na tabela e cria restrições do bagulho


SESSÃO:
    - Objetivo da sessão é ser um lugar transitivo, entre a operação e o que de fato vai para o banco de dados

MIGRAÇÕES:
    - É difícil o banco de dados acompanhar o código a medida que alterações são feitas
    - Banco de dados evolutivo
    -   O banco acompanha as alterações do código
    -   Reverter alterações no schema do banco

    ALEMBIC:
        - poetry add alembic
        - alembic init migrations
        - alembic revision --autogenerate -m "create users table"
        Vai criar um arquivo .db, que pode ser verificado
        - python3 -m sqlite3 database.db
        Aplica alterações
        - alembic upgrade head
    

    cria um arquivo.py no migrations/versions que é a versão do banco de dados.


  - Basicamente, tudo que mudar no modelo, vai mudar no banco também



07 - O método "scalar" da session tem o objetivo de:

session.scalar(select(User).where(User.username == 'Quiz'))

    Executar uma query no banco de dados
    Retornar somente um resultado do banco
    Converter o resultado da query em um objeto do modelo
 X  Todas as alternativas estão corretas