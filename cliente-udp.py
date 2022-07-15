import socket 

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("Cliente socket criado com sucesso!")

host = 'localhost'

question =  input("Deseja inserir uma porta manualmente? s/n: ")

porta = 5433

mensagem = 'Conectado!'

try:
    print('cliente ' +  mensagem)
    conexao.sendto(mensagem.encode(), (host, 5433))

    dados = conexao.recvfrom(4096)
    dados =  dados.decode()
    print("Cleinte " + dados)
finally:
    print('Cliente: Fechando conexao')
    conexao.close

