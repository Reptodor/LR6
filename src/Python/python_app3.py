# Клиентская часть (chess_client.py)
import pygame
import socket
import ast

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION

class ChessClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 5555))
        self.color = self.client.recv(1024).decode()
        self.selected_piece = None
        self.board = []
        self.update_board()

    def update_board(self):
        self.client.send('GET_BOARD'.encode())
        self.board = ast.literal_eval(self.client.recv(4096).decode())

    def draw_board(self, screen):
        colors = [(235, 235, 208), (119, 148, 85)]
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                piece = self.board[row][col]
                if piece:
                    font = pygame.font.Font(None, 50)
                    text = font.render(piece[1], True, (0,0,0) if piece[0] == 'b' else (255,255,255))
                    screen.blit(text, (col*SQ_SIZE + 15, row*SQ_SIZE + 10))

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.color == self.get_current_turn():
                    x, y = pygame.mouse.get_pos()
                    col = x // SQ_SIZE
                    row = y // SQ_SIZE
                    if self.selected_piece:
                        from_pos = (self.selected_piece[0], self.selected_piece[1])
                        to_pos = (row, col)
                        self.client.send(f'MOVE{from_pos, to_pos}'.encode())
                        self.selected_piece = None
                        self.update_board()
                    else:
                        piece = self.board[row][col]
                        if piece and piece.startswith(self.color[0]):
                            self.selected_piece = (row, col)

            screen.fill((0,0,0))
            self.draw_board(screen)
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

    def get_current_turn(self):
        # Реализуйте получение текущего хода с сервера
        return 'white'  # Временная заглушка

if __name__ == "__main__":
    ChessClient().run()