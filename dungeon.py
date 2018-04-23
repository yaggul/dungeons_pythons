def Dungeon(filename):
    with open(filename, 'r') as f:
        matrix = []
        lines = f.readlines()
        for line in lines:
            row = []
            for i in line:
                row.append(i)
            matrix.append(row[:-1])
        return matrix
