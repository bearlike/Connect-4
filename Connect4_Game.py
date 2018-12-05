# ==============================================================================
# Connect-4                                                                    |
# Created by Krishna Alagiri, https://github.com/KrishnaAlagiri                |
# Started on Decemeber 11:00 PM, 03/12/2018                                    |
# Status: COMPLETED on 19:00 PM, 05/12/2018                                    |
# ==============================================================================
import random
import os
import msvcrt
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

def getFirstEmpty(board, column):
    # Returns the lowest empty row in the given column.
    for y in range(board_height-1, -1, -1):
        if board[column][y] == EMPTY:
            return y
    return -1

def checkWin(board, tile):
    # check -- horizontal spaces
    for x in range(board_width - 3):
        for y in range(board_height):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True
    # check | vertical spaces
    for x in range(board_width):
        for y in range(board_height - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True
    # check / diagonal spaces
    for x in range(board_width - 3):
        for y in range(3, board_height):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True
    # check \ diagonal spaces
    for x in range(board_width - 3):
        for y in range(board_height - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True
    return False

def DrawBoard(board, extraToken=None):
    screen.fill(bgcolour)
    # draw tokens
    spaceRect = pygame.Rect(0, 0, space, space)
    for x in range(board_width):
        for y in range(board_height):
            spaceRect.topleft = (X_margin + (x * space), Y_margin + (y * space))
            if board[x][y] == red:
                screen.blit(redtoken_img, spaceRect)
            elif board[x][y] == yellow:
                screen.blit(yellowtoken_img, spaceRect)
    # draw the extra token
    if extraToken != None:
        if extraToken['color'] == red:
            screen.blit(redtoken_img, (extraToken['x'], extraToken['y'], space, space))
        elif extraToken['color'] == yellow:
            screen.blit(yellowtoken_img, (extraToken['x'], extraToken['y'], space, space))

    # draw board over the tokens
    for x in range(board_width):
        for y in range(board_height):
            spaceRect.topleft = (X_margin + (x * space), Y_margin + (y * space))
            screen.blit(board_img, spaceRect)

    screen.blit(redtoken_img, redpilerect) # red on the left
    screen.blit(yellowtoken_img, yellowpilerect) # YELLOW on the right
    pygame.display.update()
    pass

def checkFull(board):
    # Returns True if there are no empty spaces anywhere on the board.
    for x in range(board_width):
        for y in range(board_height):
            if board[x][y] == EMPTY:
                return False
    return True

def checkValid(board, column):
    if column < 0 or column >= (board_width) or board[column][0] != EMPTY:
        return False
    return True

def P1_getMove(board):
    global p1Count
    draggingToken = False
    tokenx, tokeny = None, None
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not draggingToken and redpilerect.collidepoint(event.pos):
                # start of dragging on red token pile.
                draggingToken = True
                tokenx, tokeny = event.pos
            elif event.type == MOUSEMOTION and draggingToken:
                # update the position of the red token being dragged
                tokenx, tokeny = event.pos
            elif event.type == MOUSEBUTTONUP and draggingToken:
                # let go of the token being dragged
                if tokeny < Y_margin and tokenx > X_margin and tokenx < window_width - X_margin:
                    # let go at the top of the screen.
                    column = int((tokenx - X_margin) / space)
                    if checkValid(board, column):
                        FE = getFirstEmpty(board, column)
                        p1Count = p1Count +1
                        print("Player 1 (Red) moves @ ["+str(column) + "," + str(FE) + "]")
                        board[column][FE] = red
                        DrawBoard(board)
                        pygame.display.update()
                        return
                tokenx, tokeny = None, None
                draggingToken = False
        if tokenx != None and tokeny != None:
            DrawBoard(board, {'x':tokenx - int(space / 2), 'y':tokeny - int(space / 2), 'color':red})
        else:
            DrawBoard(board)

        pygame.display.update()
        clock.tick()

def P2_getMove(board):
    global p2Count
    draggingToken = False
    tokenx, tokeny = None, None
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not draggingToken and yellowpilerect.collidepoint(event.pos):
                # start of dragging on yellow token pile.
                draggingToken = True
                tokenx, tokeny = event.pos
            elif event.type == MOUSEMOTION and draggingToken:
                # update the position of the yellow token being dragged
                tokenx, tokeny = event.pos
            elif event.type == MOUSEBUTTONUP and draggingToken:
                # let go of the token being dragged
                if tokeny < Y_margin and tokenx > X_margin and tokenx < window_width - X_margin:
                    # let go at the top of the screen.
                    column = int((tokenx - X_margin) / space)
                    if checkValid(board, column):
                        FE = getFirstEmpty(board, column)
                        p2Count = p2Count +1
                        print("Player 2 (Yellow) moves @ ["+str(column) + "," + str(FE) + "]")
                        board[column][FE] = yellow
                        DrawBoard(board)
                        pygame.display.update()
                        return
                tokenx, tokeny = None, None
                draggingToken = False
        if tokenx != None and tokeny != None:
            DrawBoard(board, {'x':tokenx - int(space / 2), 'y':tokeny - int(space / 2), 'color':yellow})
        else:
            DrawBoard(board)

        pygame.display.update()
        clock.tick()

def mainGame():
    turn = p1
    # Set up a blank board data structure.
    mainBoard = resetBoard()
    os.system("cls")
    print("  Connect 4: Created by Krishna Alagiri")
    print("===========================================")
    print()
    while True: # main game loop
        # Player 1
        if turn == p1:
            P1_getMove(mainBoard)
            if checkWin(mainBoard, red):
                print("Player 1 won the game in "+ str(p1Count) +" moves!")
                print("Press any key to continue...")
                msvcrt.getch()
                break
            turn = p2
        # Player 2
        else:
            P2_getMove(mainBoard)
            if checkWin(mainBoard, yellow):
                print("Player 2 won the game in "+ str(p2Count) +" moves!")
                print("Press any key to continue...")
                msvcrt.getch()
                break
            turn = p1
        # Tie
        if checkFull(mainBoard):
            print("The game is Tie!")
            print("Press any key to continue...")
            msvcrt.getch()
            breaks
    DrawBoard(mainBoard)

def resetBoard():
    board = []
    for x in range(0, board_width):
        board.append([EMPTY]*board_height)
    return board

def main():
    if board_width < 4 and board_height < 4:
        print("Invalid board_width or board_height")
        exit()

    global clock, screen, redpilerect, yellowpilerect, redtoken_img
    global yellowtoken_img, board_img, p1w_img
    global p2w_img, winnerrect, tie_img, p1Count, p2Count
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Connect 4: Created by Krishna Alagiri')
    redpilerect = pygame.Rect(int(space / 2), window_height - int(3 * space / 2), space, space)
    yellowpilerect = pygame.Rect(window_width - int(3 * space / 2), window_height - int(3 * space / 2), space, space)
    try:
        redtoken_img = pygame.image.load('images//red_coin.png')
        redtoken_img = pygame.transform.smoothscale(redtoken_img, (space, space))
        yellowtoken_img = pygame.image.load('images//yellow_coin.png')
        yellowtoken_img = pygame.transform.smoothscale(yellowtoken_img, (space, space))
        board_img = pygame.image.load('images//board_piece.png')
        board_img = pygame.transform.smoothscale(board_img, (space, space))
    except:
        pygame.display.quit()
<<<<<<< HEAD
        print("\nImages(s) Not Found in */images")
=======
        print()
        print("Images(s) Not Found in */images")
>>>>>>> 7c073ac9fe5f46168147a98f60e1889b31a91270
        print("Place files in */images and restart the program")
        print("Press any key to continue...")
        msvcrt.getch()
        exit(0)
    p1Count = 0
    p2Count = 0
    mainGame()

if __name__ == '__main__':
    main()
