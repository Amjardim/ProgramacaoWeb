#Antonio Jardim - 1610422 & Felipe Metson
from genericpath import isfile
from sys import argv, path, stderr
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, IPPROTO_TCP, AI_ADDRCONFIG
import os
from time import sleep
import sys

from Configurator import arquivo as Arquivo
from Controller import servidorController as ServController

class Servidor():
    
    def __init__(self):
        self.serverConfig = Arquivo.ServerConfigurator()
        self.serverController = ServController.ServidorController(self.serverConfig)
        
    def startServer(self):
        tcpSocket = self.criaSocket()
        origem = (self.serverConfig.get_host(), self.serverConfig.get_port())

        self.bindSocket(tcpSocket, origem)
        
        self.listen(tcpSocket)

        print("Servidor pronto")

        while(True):
            con, cliente = tcpSocket.accept()
            pid = os.fork()
            if pid == 0:
                tcpSocket.close()
                print("Servidor connectado com ", cliente)
                while(True):
                    requisicao = con.recv(self.serverConfig.get_package_size())
                    if not requisicao:
                        break
                    else:
                        self.serverController.gerente_de_requisicao(requisicao, con,cliente)
                sleep(10)
                con.close()
                print("Conexao terminada com ", cliente)

                exit()
            else:
                con.close()
                
        return

    def listen(self,tcpSocket):
        try:
            tcpSocket.listen(4)
        except:
            print("Erro ao comecar a escutar a porta", file=stderr)
            os.abort()
        print("Iniciando o servico")
        return

    def bindSocket(self,tcpSocket, origem):
        try:
            e = tcpSocket.bind(origem)
        except:
            print(sys.exc_info()[0])
            print("Erro ao dar bind no socket do servidor", origem, file=stderr)
            os.abort()
        return

    def criaSocket(self):
        tcpSocket = socket(AF_INET, SOCK_STREAM)
        if not tcpSocket:
            print("Nao consegui criar o socket")
            os.abort()
        return tcpSocket


servidor = Servidor()
servidor.startServer()
