import game
import random


game.init()


def draw_board(screen):
    game.draw.line(screen, (255, 255, 255), (100, 0), (100, 300), 3)
    game.draw.line(screen, (255, 255, 255), (200, 0), (200, 300), 3)
    game.draw.line(screen, (255, 255, 255), (0, 100), (300, 100), 3)
    game.draw.line(screen, (255, 255, 255), (0, 200), (300, 200), 3)


def make_move(screen, symbol):
    for i in range(3):
        for j in range(3):
            if symbol[i][j] == "0":
                game.draw.circle(screen, (255, 255, 0),
                                   (j * 100 + 50, i * 100 + 50), 45)
            elif symbol[i][j] == "x":
                game.draw.line(screen, (255, 0, 255), (j * 100 + 5,
                                 i * 100 + 5), (j * 100 + 95, i * 100 + 95), 20)
                game.draw.line(screen, (255, 0, 255), (j * 100 +
                                 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 20)


def get_win_check(board, symbol):
    if_win = False
    for line in board:
        if line.count(symbol) == 3:
            if_win = True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            if_win = True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        if_win = True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        if_win = True
    return if_win


SCREEN_SIZE = (300, 300)

window = game.display.set_mode(SCREEN_SIZE)
screen = game.Surface(SCREEN_SIZE)

game.display.set_caption("Крестики-нолики")
screen.fill((0, 0, 0))

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

runGame = True
move = 1
game_over = False

while runGame:
    for event in game.event.get():
        if event.type == game.QUIT:
            runGame = False

        if event.type == game.MOUSEBUTTONDOWN and not game_over:
            pos = game.mouse.get_pos()
            if board[pos[1] // 100][pos[0] // 100] == "" and move % 2 != 0:
                board[pos[1] // 100][pos[0] // 100] = "x"
                move += 1
            if board[pos[1] // 100][pos[0] // 100] == "" and move % 2 == 0:
                board[pos[1] // 100][pos[0] // 100] = "0"
                move += 1

            player_1 = get_win_check(board, "x")
            player_2 = get_win_check(board, "0")

            if player_1 or player_2:
                game_over = True
                if player_1:
                    game.display.set_caption("Крестики победили")
                else:
                    game.display.set_caption("Нолики победили")

            elif move == 10 and not game_over:
                game_over = True
                game.display.set_caption("Ничья")

    make_move(screen, board)
    draw_board(screen)
    window.blit(screen, (0, 0))
    game.display.update()