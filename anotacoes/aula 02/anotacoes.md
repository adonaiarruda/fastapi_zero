Uvicorn
    - O Uvicorn é o "servidor da aplicação" -> Servidor ASGI
    - Que serve o framework fast api
    - Fazer a cola entra as chamadas de rede e repassar para o código puro

Outra forma de servir a aplicação
    - uvicorn src.fastapi_zero.app:app
  
Rede Local (LAN)
    - Até esse momento, estamos usando ainda o "loopback", o nosso pc é o cliente e o servidor ao mesmo tempo. O que não é muito prático ainda, pois queremos fazer uma aplicação para diversos clientes.
    - fastapi dev fast_zero/app.py --host 0.0.0.0
      - Vai abrir a aplicação para rede local


    Descobrir ip local
        >>> import socket
        >>> s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        >>> s.connect(("8.8.8.8", 80))
        >>> s.getsockname()[0]

Classes de IP:
    - Classe A
    - Classe B
    - Classe C

Modelo da WEB
    - URL: Localizador Uniforme de Recursos. Um endereço de rede pelo qual podemos nos comunicar com um computador na rede.
    - HTTP: um protocolo que especifica como deve ocorrer a comunicação entre dispositivos.
    - HTML: a linguagem usada para criar e estruturar páginas na web.
URL:
    - Protocolo + endereço + porta / caminho / recurso ? filtro do recurso (query string) # fragmento do recurso

HTTP:
    - HTTP, ou Hypertext Transfer Protocol (Protocolo de Transferência de Hipertexto), é o protocolo fundamental na web para a transferência de dados e comunicação entre clientes e servidores. Ele baseia-se no modelo de requisição-resposta: onde o cliente faz uma requisição ao servidor, que responde a essa requisição. Essas requisições e respostas são formatadas conforme as regras do protocolo HTTP.

Verbos HTTP:
    - GET: utilizado para recuperar recursos. Quando queremos solicitar um dado já existente no servidor.
  (só solicitar informação, é tudo bem ser só um GET)
    - POST: permite criar um novo recurso. Por exemplo, enviar dados para registrar um novo usuário.
    - PUT: Atualiza um recurso existente. Como, por exemplo, atualizar as informações de um usuário existente.
    - DELETE: Exclui um recurso. Por exemplo, remover um usuário específico do sistema.

HTTP - códigos de resposta

    - 1xx: informativo — utilizada para enviar informações para o cliente de que sua requisição foi recebida e está sendo processada.
    - 2xx: sucesso — Indica que a requisição foi bem-sucedida (por exemplo, 200 OK, 201 Created).
    - 3xx: redirecionamento — Informa que mais ações são necessárias para completar a requisição (por exemplo, 301 Moved Permanently, 302 Found).
    - 4xx: erro no cliente — Significa que houve um erro na requisição feita pelo cliente (por exemplo, 400 Bad Request, 404 Not Found). (422 Unprocessable Content, mais comum, problema na validação do código de entrada)
    - 5xx: erro no servidor — Indica um erro no servidor ao processar a requisição válida do cliente (por exemplo, 500 Internal Server Error, 503 Service Unavailable).
  - Documentação dos códigos:
    - https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
    - https://http.cat/

API REST: 
    - Pra ser REST precisa ser HTML
    - Se trafegar JSON, NÃO É uma API REST
    - JSON|HTML: è o tipo de objeto trafegado



Example using PDB:
Python

import pdb

def my_function():
    print("Inside my_function")
    pdb.set_trace()  # Breakpoint 1
    print("After breakpoint 1")
    pdb.set_trace()  # Breakpoint 2
    print("After breakpoint 2")

my_function()


c -> continue
n -> next (step over)



HOOKS:
    - Eventos para fazer alguma operação antes ou depois de alguma operação
    - Roubar nos testes

PYDANTIC SETTINGS
    - Para não colocar configurações hard coded
    - Credentciais de banco de dados são independentes de código
https://12factor.net/pt_br/



Crie o .env:
    - nano .env