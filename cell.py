from math import sqrt


class Board:
    def __init__(self, cells):
        self.cells = cells

    def checkNeighbour(self, currentCell):
        neighbours = 0
        cell_coord_x = currentCell.x
        cell_coord_y = currentCell.y
        neighbourList = []

        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells)):
                if self.cells[x][y] == currentCell:
                    continue
                a = abs(self.cells[x][y].x-cell_coord_x)
                b = abs(self.cells[x][y].y-cell_coord_y)
                dist = sqrt((a**2)+(b**2))
                if dist < 2 and self.cells[x][y].state == 1:
                    neighbours += 1
            return neighbours

    def alive(self, x, y):
        self.cells[x][y].state = 1
        return


class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        # self.coords = (x, y)
        self.state = state

    def stateChange(self, neighbours):
        if self.state == 0 and neighbours == 3:
            self.state = 1
        elif self.state == 1:
            if neighbours == 2 or neighbours == 3:
                return self.state
            else:
                self.state = 0
        else:
            self.state = 0

        return self.state
