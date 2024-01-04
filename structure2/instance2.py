def readInstance2(path):
    instance = {}
    with open(path, "r") as f:

        # In 1b we only have n given, p is 0.25*n
        n = f.readline()
        n = int(n)
        p = 0.25*n

        instance['n'] = n
        instance['p'] = p
        instance['d'] = []
        for i in range(n):
            instance['d'].append([0] * n)
        for i in range(n):
            for j in range(i+1, n):
                u, v, d = f.readline().split()
                u = int(u)
                v = int(v)
                d = round(float(d), 2)
                instance['d'][u][v] = d
                instance['d'][v][u] = d
    return instance
