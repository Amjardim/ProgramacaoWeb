#Antonio Jardim - 1610422 & Felipe Metson
import os

class ServerConfigurator():
    
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.filelist = ["arquivo.html","arquivo.js","arquivo.jpg","arquivo.png","arquivo.gif"]
        self.path_dir = "./arquivo"
        self.pag_erro = "erro.html"
        self.package_size = 1024
        
    def get_host(self):
        return self.host
        
    def get_port(self):
        return self.port
        
    def get_filelist(self):
        return self.filelist
    
    def get_pathdir(self):
        return self.path_dir
    
    def get_pag_erro(self):
        return self.pag_erro
        
    def get_package_size(self):
        return self.package_size
