Antonio Jardim - 1610422 & Felipe Metson 1520302

INF1407 - Programação para Web - Trabalho 1 - Relatório:
•	Colocando Servidor para funcionar:
	Organizamos o servidor com a seguinte arquitetura: servidorLinux.py é o arquivo principal tendo um servidorController.py que lida com as requisições e o servidorLinux.py que lida com as regras de negocio estabelecidas. O arquivo.py carrega as configurações dos arquivos.
	No terminal mover até pasta onde estão os arquivos do programa. Executar o comando:
	python3 servidorLinux.py
	E acessar quaisquer dos arquivos através do browser de sua preferência:
	localhosthost:8080/arquivo/arquivo.html
	localhosthost:8080/arquivo/arquivo.jpeg
	localhosthost:8080/arquivo/arquivo.png
	localhosthost:8080/arquivo/arquivo.gif
	localhosthost:8080/arquivo/arquivo.js

•	Testando conexões simultâneas:
	Utilizamos de um sleep(10) para testar conexões simultâneas e os testes mostraram que a 	conexão simultânea ocorre sem problemas.
•	Casos de teste:

Testamos o acesso a todos as chamadas abaixo verificando se a resposta era compatível com o teste em questão.
	localhosthost:8080/arquivo/arquivo.html
	localhosthost:8080/arquivo/arquivo.jpeg
	localhosthost:8080/arquivo/arquivo.png
	localhosthost:8080/arquivo/arquivo.gif
	localhosthost:8080/arquivo/arquivo.js
	localhosthost:8080
	localhosthost:8080/teste

