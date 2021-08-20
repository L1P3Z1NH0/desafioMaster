ttask = input('Insira o número de ticks para realizar uma tarefa: ')
umax = input('Insira o número máximo de usuários por servidor: ')
umax = int(umax)
servidores = []
usuariosTotal = 0

for ticks in range(10):
    usuarios = input('Quantos usuários serão conectados ?')
    usuarios = int(usuarios)
    servidores.append(usuarios)
    usuariosTotal += usuarios

    if usuariosTotal == umax:
        print('Tomanucuuu')
        break

