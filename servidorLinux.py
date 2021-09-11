#Antonio Jardim - 1610422 & Felipe Metson
from genericpath import isfile
from sys import argv, path, stderr
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, IPPROTO_TCP, AI_ADDRCONFIG
import os
from time import sleep
import sys

def startServer():
    bufferSize = 1024
    host = '127.0.0.1'

    if len(argv) > 1 and (argv[1]==8080 or argv[1]==80): 
        port = int(argv[1])
    else:
        port = 8080

    tcpSocket = criaSocket()
    
    origem = (host, port)

    bindSocket(tcpSocket, origem)
    
    listen(tcpSocket)

    print("Servidor pronto")

    while(True):
        con, cliente = tcpSocket.accept()
        pid = os.fork()
        if pid == 0:
            tcpSocket.close()
            print("Servidor connectado com ", cliente)
            requisicao = con.recv(bufferSize)
            if not path_arquivo:
                break
            
            if requisicao.contains("arquivo/"):
                path_arquivo = requisicao.extrairCaminho()
                arquivo = get(path_arquivo)
                con.send(arquivo)                
            print(path_arquivo)
            con.send(path_arquivo)                
            print("Conexao terminada com ", cliente)
            con.close()
            exit()
        else:
            con.close()
    return

def listen(tcpSocket):
    try:
        tcpSocket.listen(0)
    except:
        print("Erro ao comecar a escutar a porta", file=stderr)
        os.abort()
    print("Iniciando o servico")
    return

def bindSocket(tcpSocket, origem):
    try:
        e = tcpSocket.bind(origem)
    except:
        print(sys.exc_info()[0])
        print("Erro ao dar bind no socket do servidor", origem, file=stderr)
        os.abort()
    return

def criaSocket():
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    if not tcpSocket:
        print("Nao consegui criar o socket")
        os.abort()
    return tcpSocket

def get(path_arquivo):
    if os.path.exists(path_arquivo):
        return 


def getArquivo():

startServer()
