from classes import Servers

ttask = input('Insira o número de "ticks" para finalizar uma tarefa: ')
ttask = int(ttask)
umax = input('Insira o número máximo de usuários por servidor: ')
umax = int(umax)

c1 = Servers(ttask, umax)
for i in range(10):
    num_users = input('Quantos usuários irão se conectar ?')
    num_users = int(num_users)
    c1.insert_user(ttask, num_users)
    c1.task_control()
    print(c1.servers)
    print(f'{c1.contServer} servidores')
