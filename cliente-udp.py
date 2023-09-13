from socket import socket, AF_INET, SOCK_DGRAM


server_name = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)

msg= input("Entre minusculas \n")

client_socket.sendto(msg.encode(), (server_name,server_port))

msg_odificada, server_address = client_socket.recvfrom(2048)

print(msg_modificada.decode())
client_socket.close()

'''
Importa os módulos necessários:

socket: Fornece funcionalidades para criar e gerenciar sockets de rede.
AF_INET: Uma constante que especifica a família de endereços IPv4.
SOCK_DGRAM: Uma constante que indica que estamos criando um socket UDP.
Define o nome do servidor (server_name) como 'localhost' e o número da porta do servidor (server_port) como 12000.

Cria um socket UDP do lado do cliente usando socket(AF_INET, SOCK_DGRAM).

Solicita ao usuário que insira um texto em letras minúsculas.

Codifica a mensagem inserida pelo usuário para bytes usando msg.encode().

Envia a mensagem codificada para o servidor usando client_socket.sendto(). Ele especifica o destino do servidor como (server_name, server_port).

Aguarda a resposta do servidor usando client_socket.recvfrom(2048). Isso permite que o cliente receba até 2048 bytes de dados do servidor.

Decodifica a mensagem recebida do servidor de volta para uma string e a armazena em msg_modificada.

Imprime a mensagem modificada.

Fecha o socket do cliente usando client_socket.close().

Resumidamente, esse código cria um cliente UDP simples que envia uma mensagem para um servidor em 'localhost' na porta 12000,

 recebe uma mensagem modificada do servidor e a imprime. É importante notar que o servidor ao qual esse cliente se conecta deve estar configurado para lidar com as mensagens UDP corretamente e aplicar alguma lógica de processamento, 

 como modificar o texto para letras maiúsculas, conforme o código do cliente sugere.
'''
