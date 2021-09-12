import os

class ServidorService():
        
    def arquivo_existe(self,path_arquivo):
        return os.path.exists(os.path.abspath("."+path_arquivo))
    
    def getArquivo(self, path_arquivo):
        os_prepared_path = "."+path_arquivo
        f = open(os_prepared_path,"rb")
        size = os.path.getsize(os_prepared_path)
        fileToResponse = f.read(size)
        return fileToResponse
