import servidorService as servService

class ServidorController():
    
    def __init__(self):
        self.servidorService = servService.ServidorService()
    
    def gerente_de_requisicao(self, requisicao, con):
        print(requisicao)
        con.send(requisicao)   
