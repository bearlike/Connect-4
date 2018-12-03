# ==============================================================================
# Created by Krishna Alagiri, https://github.com/KrishnaAlagiri                |
# Started on Decemeber 11:00 PM, 03/12/2018                                    |
# Status: NOT COMPLETED                                                        |
# ==============================================================================
import random
import copy
import sys
import pygame
from pygame.locals import *

""" Configuration Area """

board_width = 4 # Width of the Board (Should not be less than 4)
board_height = 6 # Height of the Board (Should not be less than 4)
space = 50 # Size of the each tokens and individual board spaces (in pixels)
FPS = 30 # frames per second to update the screen
window_width = 640 # width of the program's window, in pixels
window_height = 480 # height in pixels
bgcolour = (0,0,0) # Background colour default set to BLACK
text_colour = (225,225,225) # Text colour default set to WHITE
X_margin = int((window_width - board_width * space) / 2) # Calculate X-Margin
Y_margin = int((window_height - board_height * space) / 2) # Calculate Y-Margin
p1 = 'Player 1'
p2 = 'Player 2'
red = 'red'
yellow = 'yellow'
EMPTY = None
""" End of Configuration Area """
""" Functions Begin """

def DrawBoard(board, extraToken=None):
    screen.fill(bgcolour)
    pass


def runGAME():
    turn = p1
    # Set up a blank board data structure.
    mainBoard = resetBoard()
    while True: # main game loop
        # Player 1
        if turn == p1:
            P1_getMove(mainBoard)
            if isWinner(mainBoard, red):
                break
            turn = p2
        # Player 2
        else:
            P2_getMove(mainBoard)
            if isWinner(mainBoard, yellow):
                break
            turn = p1
        # Tie
        if isBoardFull(mainBoard):
            breaks
    DrawBoard(mainBoard)
    pass

def resetBoard():
    board = []
    for x in range(0, board_width):
        board.append([empty]*board_height)
    return board

def main():
    if board_width < 4 and board_height < 4:
        print("Invalid board_width or board_height")
        exit()

    global clock, screen, redpilerect, yellowpilerect, redtoken_img
    global yellowtoken_img, board_img, p1w_img
    global p2w_img, winnerrect, tie_img

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Connect 4: Created by Krishna Alagiri')

    runGAME()

if __name__ == '__main__':
    main()
