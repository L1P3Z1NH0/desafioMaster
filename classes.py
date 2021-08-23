class Servers:

    def __init__(self, ttask, umax):
        self.ttask = ttask
        self.umax = umax
        self.servers = []
        self.count_server = 0
        self.count_max = 0
        self.count_created = 0

    def insert_user(self, ttask, num_users):
        self.count_created = 0
        for i in range(num_users):
            if len(self.servers) == 0 or self.count_max >= self.umax:
                self.count_max = 0
                self.count_created += 1
                self.count_server += 1
                self.count_max += 1
                self.servers.append([ttask + 1])
            else:
                self.count_max += 1
                self.servers[-1].append(ttask + 1)

        for serverI, serverV in enumerate(self.servers):
            subtract_all = [i - 1 for i in self.servers[serverI]]
            self.servers[serverI] = subtract_all

            filtered_list = [i for i in self.servers[serverI] if i]
            self.servers[serverI] = filtered_list

            if not self.servers[serverI]:
                self.count_server -= 1

        if [] in self.servers:
            remove_empty = [i for i in self.servers if i]
            self.servers = remove_empty


        # for i, v in enumerate(self.servers):
        #     if len(self.servers[i]) < self.umax and len(self.servers[i]) != len(self.servers[-1]):
        #         self.servers[i].append(self.servers[-1][-1])
        #         del self.servers[-1][-1]
        #
        #     elif len(self.servers[i]) < self.umax and len(self.servers[i - 1]) == len(self.servers[-1]) \
        #             and len(self.servers) > 1:
        #         self.servers[i].append(self.servers[-1][-1])
        #         del self.servers[-1][-1]
