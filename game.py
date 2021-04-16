from board import Board
import pygame

pygame.init()
height = 600
width = height

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TicTacToe")

class Game:
    def __init__(self):
        self.board = Board()
        self.border_width = 5
        self.square_width = (width - (self.border_width * 2) ) // 3

    def display(self, screen):
        screen.fill((0,0,0))
        for row in range(3):
            for col in range(3):
                x_cord = (col * self.square_width) + (self.border_width * col)
                y_cord = row * (self.square_width + self.border_width)
                pygame.draw.rect(screen, (230,230,230), (x_cord, y_cord, self.square_width, self.square_width))
                if self.board.board[col][row] != 0:
                    if self.board.board[col][row] == 1:
                        colour = (255,0,0)
                    else:
                        colour = (0,0,255)
                    centre_x = x_cord + (self.square_width // 2)
                    centre_y = y_cord + (self.square_width // 2)
                    pygame.draw.circle(screen, colour, (centre_x, centre_y), self.square_width // 2)


    def get_square(self, mousepos):
        x = mousepos[0] // (self.square_width + self.border_width)
        y = mousepos[1] // (self.square_width + self.border_width)
        print(x, y)
        return [x,y]


game = Game()

end = False
while not end:
    if not( game.board.winner is None):
        end = True
        print(f"Winner: {game.board.winner}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = game.get_square(pygame.mouse.get_pos())
            if game.board.board[pos[0]][pos[1]] == 0:
                game.board.move(pos)


    game.display(screen)
    pygame.display.update()

    game.display(screen)

                    








