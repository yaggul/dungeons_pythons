from hero import Hero


class Dungeon:

    def __init__(self, filename, hero=None):
        self.filename = filename
        self.matrix = []
        self.rows = 0
        self.cols = 0
        self.hero = None

    def open_file(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                row = []
                for i in line:
                    row.append(i)
                self.matrix.append(row[:-1])
        return self.matrix

    def print_map(self):
        if len(self.matrix) == 0:
            self.open_file()
            for row in self.matrix:
                for col in row:
                    print(col, end='')
                print()
        else:
            for row in self.matrix:
                for col in row:
                    print(col, end='')
                print()

    def spawn(self, Hero):
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 'S':
                    self.matrix[i][j] = 'H'
                    self.hero = Hero
                    return True

            return False

    def valid_position(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        else:
            return True

    def move_hero(self, direction):
        xDirections = [0, 0, -1, 1]
        yDirections = [-1, 1, 0, 0]
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        hero = self.spawn

        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == 'H':
                    curr_position_row = self.matrix[i]
                    curr_position_col = self.matrix[j]

                    if direction == 'left':
                        if self.valid_position(i - 1, j):
                            self.matrix[i - 1][j] = 'H'
                            self.matrix[i][j] = '.'
                            return True
                        else:
                            return False
                    elif direction == 'right':
                        if self.valid_position(i + 1, j):
                            self.matrix[i + 1][j] = 'H'
                            self.matrix[i][j] = '.'
                            return True
                        else:
                            return False
                    if direction == 'up':
                        if self.valid_position(i, j + 1):
                            self.matrix[i][j + 1] = 'H'
                            self.matrix[i][j] = '.'
                            return True
                        else:
                            return False
                    elif direction == 'down':
                        if self.valid_position(i, j - 1):
                            self.matrix[i][j - 1] = 'H'
                            self.matrix[i][j] = '.'
                            
                        else:
                            return False
