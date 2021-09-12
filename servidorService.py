import os
import arquivo as Arquivo

class ServidorService():
    
    def __init__(self, servConfig):
        self.servidorConfigurator = servConfig

    def arquivo_existe(self,path_arquivo):
        return (( os.path.exists(os.path.abspath("."+path_arquivo)) and
               ( path_arquivo.split('/')[-1] in self.servidorConfigurator.get_filelist()) ))
    
    def getArquivo(self, path_arquivo):
        # Le e retorna arquivo inteiro
        os_prepared_path = "."+path_arquivo
        f = open(os_prepared_path,"rb")
        size = os.path.getsize(os_prepared_path)
        fileToResponse = f.read(size)
        f.close()
        return fileToResponse
