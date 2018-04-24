
class Dungeon:
    def __init__(self, filename):
        self.filename = filename

    def print_map(self):
        with open(self.filename, 'r') as f:
            matrix = []
            lines = f.readlines()
            for line in lines:
                row = []
                for i in line:
                    row.append(i)
                matrix.append(row[:-1])
            for row in matrix:
                for coll in row:
                    print(coll, end='')
                print()
