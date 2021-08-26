#Antonio Jardim - 1610422 & Felipe Metson
from genericpath import isfile
from sys import argv, path, stderr
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, IPPROTO_TCP, AI_ADDRCONFIG
from posix import abort
import os
from time import sleep

#Implemente um servidor Web. O servidor deve escutar a porta 80 ou 8080 e aceitar requisições GET.
def ThreadedServer():
    bufferSize = 1024
    host = ''

    if len(argv) > 1 and (argv[1]==8080 or argv[1]==80): 
        port = int(argv[1])
    else:
        port = 80

    #Socket - Pelo kernel, socket é um ponto de comunicação
    #Para a aplicação, socket é um descritor de arquivo, no qual a aplicação pode ler e/ou escrever
    #Tenta criar o socket
    tcpSocket = criaSocket()
    origem = (host, port)
    #Tenta ouvir o socket criado
    listen(tcpSocket)
    #Tenta dar um bind no socket criado
    bindSocket(tcpSocket, origem)
    print("Servidor pronto")

    while(True):
        con, cliente = tcpSocket.accept()
        cliente.settimeout(60)
        pid = fork()
        if pid == 0:
            #esse é o filho
            tcpSocket.close()
            print("Servidor connectado com ", cliente)
            #inclua dentro do servidor um delay para testar conexões simultâneas
            sleep(5)
            while True:
                path_arquivo = con.recv(bufferSize)

                #FAZER ISSO
                if path_arquivos :
                    percorre_arquivos()
                if exists:
                    break
                else:
                    print('Erro 404')

                print(cliente, path_arquivo)
                con.send(path_arquivo)
                #con.sendfile(get(path_arquivo))
                
            print("Conexão terminada com ", cliente)
            con.close()
            exit()
        else:
            #esse é o pai
            con.close()
    return

def listen(tcpSocket):
    try:
        tcpSocket.listen(0)
    except:
        print("Erro ao começar a escutar a porta", file=stderr)
        abort()
    print("Iniciando o serviço")
    return

def bindSocket(tcpSocket, origem):
    try:
        tcpSocket.bind(origem)
    except:
        print("Erro ao dar bind no socket do servidor", origem, file=stderr)
        abort()
    return

def criaSocket():
    #AF_INET Ipv4Address, SOCK_STREAM Byte-stream socket (TCP)
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    if not tcpSocket:
        print("Não consegui criar o socket")
        abort()
    return tcpSocket

#FAZER ISSO
def get(path_arquivo):
    #ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    #path = ROOT_DIR + path_arquivo
    if os.path.exists(path_arquivo):
        return 
