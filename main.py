from classes import Servers

ttask = input('Insira o número de "ticks" para finalizar uma tarefa: ')
ttask = int(ttask)
umax = input('Insira o número máximo de usuários por servidor: ')
umax = int(umax)
preco = 0

c1 = Servers(ttask, umax)
for i in range(10):
    num_users = input('Quantos usuários irão se conectar ?')
    num_users = int(num_users)
    c1.insert_user(ttask, num_users)
    print(c1.servers)
    if c1.count_created >= 1:
        print(f'{c1.count_created} servidores foram criados')
    else:
        print('Nenhum servidor foi criado')
    print(f'{c1.count_server} servidores')
    preco += 1 * c1.count_server
    print(f'Preco atual R${preco}')

