from cell import Cell, Board
import curses
from curses import wrapper
import time
from random import randint

SCREEN_WIDTH = 5
SCREEN_HEIGHT = 5
# CELL_POS = [(2, 3), (2, 4), (3, 3), (4, 3)]
CELL_POS = [(2, 2), (2, 3), (3, 2), (4, 2)]
cell_list = []


def main(stdscr):
    temp_list = []
    alive_list = []
    stdscr.clear()

    for _ in range(0, SCREEN_WIDTH):
        alive_list.append([])

    for x in range(0, SCREEN_WIDTH):
        for y in range(0, SCREEN_HEIGHT):
            alive_list[x].append(Cell(x, y, 0))

    board = Board(alive_list)

    for cell in CELL_POS:
        board.alive(cell[0], cell[1])

    for n in range(len(alive_list)):
        for cell in (alive_list[n]):
            if cell.state == 1:
                stdscr.addstr(cell.x, cell.y, str(board.checkNeighbour(cell)))
            else:
                stdscr.addstr(cell.x, cell.y, 'o')

    stdscr.refresh()
    stdscr.getch()

# def checkNeighbour(list_of_cells):
#     for cell in list_of_cells:


# def main(stdscr):
#     stdscr.clear()

#     for x in range(SCREEN_SIZE[0]):
#         for y in range(SCREEN_SIZE[1]):
#             cell = Cell(x, y, 0)
#             cell_list.append(cell)

#     board = Board(cell_list)

#     for cell in CELL_POS:
#         board.alive(cell[0], cell[1])
#         # print(cell.x, cell.y, board.checkNeighbour(cell))
#         # stdscr.addstr(cell.x, cell.y, 'o')
#     # while True:

#     # for i in range(0, 3):
#     board = Board(cell_list)
#     stdscr.clear()
#     for cell in cell_list:
#         if cell.state == 1:
#             stdscr.addstr(cell.x, cell.y, str(board.checkNeighbour(cell)))
#             print(cell.x, cell.y, board.checkNeighbour(cell))

#         else:
#             stdscr.addstr(cell.x, cell.y, ' ')
#     stdscr.refresh()
#     stdscr.getch()

#     stdscr.clear()

#     for cell in cell_list:
#         cell.stateChange(board.checkNeighbour(cell))
#         if cell.state == 1:
#             stdscr.addstr(cell.x, cell.y, str(
#                 board.checkNeighbour(cell)))

#         else:
#             stdscr.addstr(cell.x, cell.y, ' ')

#     stdscr.refresh()

#     stdscr.getch()
wrapper(main)
