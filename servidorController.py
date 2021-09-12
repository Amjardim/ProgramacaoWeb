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
        dict_request = self.dicionario_da_requisicao(requisicao)
        print(dict_request[self.REQUISICAO_COMPLETA])
        
        if dict_request[self.COMANDO] == "GET":
            print("Get requisitada por: ", cliente)
            caminho = dict_request[self.CAMINHO]
            if caminho is not None:
                caminho_existe = self.servidorService.arquivo_existe(caminho)
                if caminho_existe:
                    fileToResponse = self.servidorService.getArquivo(caminho)
                    self.response_ok(con,fileToResponse)
                    return
        
        con.send("bad-request".encode())

                
        #con.send(requisicao)
        
    def dicionario_da_requisicao(self, requisicao):
        request_vetor = requisicao.decode('utf8').split('\r')
        dict_request = { self.COMANDO : request_vetor[0].split()[0],
                         self.CAMINHO : request_vetor[0].split()[1],
                         self.ENDERECO : request_vetor[1],
                         self.REQUISICAO_COMPLETA : requisicao.decode('utf8')}
        
        return dict_request
    
    
    def response_ok(self, con, fileToResponse):
        response_headers = {
        'Server' : 'Apache-Coyote/1.1',
        'Content-Type': 'text/html',
        'Content-Length': len(fileToResponse),
        'Date': 'close',
        }

        response_headers_raw = ''.join('%s: %s\r\n' % (k, v) for k, v in response_headers.items())
        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK' # this can be random
        r = '%s %s %s\r\n' % (response_proto, response_status, response_status_text)
        con.sendall(r.encode())
        con.sendall(response_headers_raw.encode())
        con.sendall(b'\r\n') # to separate headers from body
        con.send(fileToResponse)
        
        
