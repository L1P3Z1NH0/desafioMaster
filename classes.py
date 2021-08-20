class Servers:

    def __init__(self, ttask, umax):
        self.ttask = ttask
        self.umax = umax
        self.servers = {}
        self.id = 0
        self.contServer = 0
        self.contMax = 0

    def insert_user(self, ttask, num_users):
        for i in range(num_users):
            if f'Servidor {self.contServer}' not in self.servers or self.contMax >= self.umax:
                self.contMax = 0
                self.contServer += 1
                self.id += 1
                self.contMax += 1
                self.servers[f'Servidor {self.contServer}'] = {self.id: ttask + 1}
            else:
                self.id += 1
                self.contMax += 1
                self.servers[f'Servidor {self.contServer}'].update({self.id: ttask + 1})

    def task_control(self):
        for serverK, serverV in self.servers.items():
            for userV in list(serverV.keys()):
                serverV[userV] -= 1

                if serverV[userV] <= 0:
                    print(f'id= {userV} foi excluido')
                    serverV.pop(userV)
