import servidorService as servService

class ServidorController():
    
    def __init__(self):
        self.servidorService = servService.ServidorService()
    
    def gerente_de_requisicao(self, requisicao, con):
        print(self.dicionario_da_requisicao(requisicao))
        con.send(requisicao)
        
    def dicionario_da_requisicao(self, requisicao):
            
        request_vetor = requisicao.decode('utf8').split('\r')
        dict_request = { "comando" : request_vetor[0].split()[0],
                         "caminho" : request_vetor[0].split()[1],
                         "endereco": request_vetor[1],
                         "requisicao_completa" : requisicao}
        
        return dict_request
