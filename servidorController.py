import servidorService as servService

ERROR_MSG_SIZE = "ERROR: bad-request"
COMANDO = "comando"
CAMINHO = "caminho"
ENDERECO = "endereco"
REQUISICAO_COMPLETA = "requisicao_completa"

class ServidorController():
    
    def __init__(self, servConfig):
        self.servidorService = servService.ServidorService(servConfig)
        self.servidorConfigurator = servConfig

    def gerente_de_requisicao(self, requisicao, con, cliente):
        # Transforma requisicao em dicionario para facilitar utilizacao das informacoes
        dict_request = self.dicionario_da_requisicao(requisicao)
        
        # Imprime a requisicao da maneira que eh pedido no enunciado
        print(dict_request[REQUISICAO_COMPLETA])
        
        # Checa se é um comando get para o servidor não ser derrubado
        if dict_request[COMANDO] == "GET":
            print("Get requisitada por: ", cliente)
            caminho = dict_request[CAMINHO]
            # Checa se foi enviado algum caminho
            if caminho is not None:
                caminho_existe = self.servidorService.arquivo_existe(caminho)
                # Checa se o caminho existe
                if caminho_existe:
                    # Com o arquivo existindo, seu conteudo eh lido e enviado no body
                    # de uma response com statuscode ok 
                    fileToResponse, extension = self.servidorService.getArquivo(caminho)
                    self.response_ok(con,fileToResponse,extension)
                    return

        self.response_error(con)
        return

    def dicionario_da_requisicao(self, requisicao):
        request_vetor = requisicao.decode('utf8').split('\r')
        dict_request = { COMANDO : request_vetor[0].split()[0],
                         CAMINHO : request_vetor[0].split()[1],
                         ENDERECO : request_vetor[1],
                         REQUISICAO_COMPLETA : requisicao.decode('utf8')}
        
        return dict_request
    
    
    def response_ok(self, con, fileToResponse, extension):
        content_type = self.get_content_type(extension)
        # Configurando o header com as entradas pedidas no enunciado
        response_headers = {
        'Server' : 'Apache-Coyote/1.1',
        'Content-Type': content_type,
        'Content-Length': len(fileToResponse),
        'Date': 'close',
        }
        
        # Preenchendo o response OK
        response_headers_raw = ''.join('%s: %s\r\n' % (k, v) for k, v in response_headers.items())
        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK'
        r = '%s %s %s\r\n' % (response_proto, response_status, response_status_text)
        
        # Enviando
        con.sendall(r.encode())
        con.sendall(response_headers_raw.encode())
        con.sendall(b'\r\n')
        con.send(fileToResponse)
        #for part in fileToResponse:
            #con.send(part)
        
        return
    
    def response_error(self, con):
        #Configurando o header com as entradas pedidas no enunciado
        response_headers = {
        'Server' : 'Apache-Coyote/1.1',
        'Content-Type': 'text/html',
        'Content-Length': len(ERROR_MSG_SIZE),
        'Date': 'close',
        }
        
        # Preenchendo o response OK
        response_headers_raw = ''.join('%s: %s\r\n' % (k, v) for k, v in 					response_headers.items())
        response_proto = 'HTTP/1.1'
        response_status = '404'
        response_status_text = 'ERROR'
        r = '%s %s %s\r\n' % (response_proto, response_status, response_status_text)
        
        # Enviando
        con.sendall(r.encode())
        con.sendall(response_headers_raw.encode())
        con.sendall(b'\r\n')
        con.send(ERROR_MSG_SIZE.encode())
        
    def get_content_type(self, extension):
        content_type = "text/html"
        if( extension == ".js" ): 
            content_type = "text/javascript"
        elif( extension == ".png" ):
            content_type = "image/png"
        elif( extension == ".jpg" ):
            content_type = "image/jpeg"
        elif( extension == ".gif" ): 
            content_type = "image/gif"
        
        return content_type
