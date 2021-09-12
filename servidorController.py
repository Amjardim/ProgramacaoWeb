import servidorService as servService
import arquivo as Arquivo

class ServidorController():
    
    def __init__(self, servConfig):
        self.servidorService = servService.ServidorService()
        self.servidorConfigurator = servConfig
        self.COMANDO = "comando"
        self.CAMINHO = "caminho"
        self.ENDERECO = "endereco"
        self.REQUISICAO_COMPLETA = "requisicao_completa"
        
    def gerente_de_requisicao(self, requisicao, con, cliente):
        # Transforma requisicao em dicionario para facilitar utilizacao das informacoes
        dict_request = self.dicionario_da_requisicao(requisicao)
        
        # Imprime a requisicao da maneira que eh pedido no enunciado
        print(dict_request[self.REQUISICAO_COMPLETA])
        
        # Checa se é um comando get para o servidor não ser derrubado
        if dict_request[self.COMANDO] == "GET":
            print("Get requisitada por: ", cliente)
            caminho = dict_request[self.CAMINHO]
            # Checa se foi enviado algum caminho
            if caminho is not None:
                caminho_existe = self.servidorService.arquivo_existe(caminho)
                # Checa se o caminho existe
                if caminho_existe:
                    # Com o arquivo existindo, seu conteudo eh lido e enviado no body
                    # de uma response com statuscode ok 
                    fileToResponse = self.servidorService.getArquivo(caminho)
                    self.response_ok(con,fileToResponse)
                    return

        # (TODO) aqui precisamos configurar a tela de error(bad request)
        con.send("bad-request".encode())

    def dicionario_da_requisicao(self, requisicao):
        request_vetor = requisicao.decode('utf8').split('\r')
        dict_request = { self.COMANDO : request_vetor[0].split()[0],
                         self.CAMINHO : request_vetor[0].split()[1],
                         self.ENDERECO : request_vetor[1],
                         self.REQUISICAO_COMPLETA : requisicao.decode('utf8')}
        
        return dict_request
    
    
    def response_ok(self, con, fileToResponse):
        # Configurando o header com as entradas pedidas no enunciado
        response_headers = {
        'Server' : 'Apache-Coyote/1.1',
        'Content-Type': 'text/html',
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
        
        
