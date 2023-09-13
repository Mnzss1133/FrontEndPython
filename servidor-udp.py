from socket import socket, AF_INET, SOCK_DGRAM

server_port = 12000

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', server_port))

print("Servidor pronto!")

while True:
    msg, cliente_address = server_socket.recvfrom(2048)
    msg_modificada = msg.decode().upper()
    server_socket.sendto(msg_modifcada.encode(),cliente_address)



    '''
Importa os módulos necessários:

socket: Fornece funcionalidades para criar e gerenciar sockets de rede.
AF_INET: Uma constante que especifica a família de endereços IPv4.
SOCK_DGRAM: Uma constante que indica que estamos criando um socket UDP.
Define o número da porta do servidor (server_port) como 12000.

Cria um socket UDP do lado do servidor usando socket(AF_INET, SOCK_DGRAM).

Liga (bind) o socket à interface de rede especificada (no caso, '', o que significa que ele está vinculado a todas as interfaces disponíveis) e à porta especificada (server_port) usando server_socket.bind().

Imprime "Servidor pronto!" para indicar que o servidor está em execução e pronto para receber conexões.

Entra em um loop infinito (while True) para receber e responder a mensagens dos clientes.

Quando uma mensagem é recebida, armazena a mensagem e o endereço do cliente que a enviou em msg e cliente_address.

Converte a mensagem recebida em letras maiúsculas usando msg.decode().upper() e armazena-a em msg_modificada.

Envia a mensagem modificada de volta ao cliente usando server_socket.sendto(msg_modificada.encode(), cliente_address).

Resumidamente, este código cria um servidor UDP que fica escutando na porta 12000 e, quando recebe uma mensagem de um cliente, converte essa mensagem para letras maiúsculas e 

a envia de volta ao cliente. Este é um exemplo simples de como um servidor UDP pode processar mensagens recebidas e responder a elas. Note que, assim como no código do cliente,

é importante que o cliente esteja configurado para enviar mensagens que este servidor possa entender e processar corretamente.


    '''