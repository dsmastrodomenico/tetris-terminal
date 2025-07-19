# tetris/game.py
import random
from tetris.board import Board
from tetris.pieces import Tetromino, SHAPES

class Game:
    def __init__(self, height, width):
        self.board = Board(height, width)
        # Inicializamos la pieza siguiente y luego la actual
        self.next_piece = self.new_piece()
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        """Crea una nueva pieza aleatoria."""
        shape_name = random.choice(list(SHAPES.keys()))
        # Para la pieza siguiente, la posición no importa, pero la establecemos por consistencia
        return Tetromino(self.board.width // 2 - 1, 0, shape_name)

    def update(self):
        """Mueve la pieza hacia abajo y maneja las colisiones."""
        if self.game_over:
            return

        self.current_piece.y += 1
        if not self.board.is_valid_move(self.current_piece):
            self.current_piece.y -= 1
            self.board.place_piece(self.current_piece)
            
            lines_cleared = self.board.clear_lines()
            self.score += lines_cleared * 100

            # La pieza siguiente se convierte en la actual
            self.current_piece = self.next_piece
            # Generamos una nueva pieza siguiente
            self.next_piece = self.new_piece()

            if not self.board.is_valid_move(self.current_piece):
                self.game_over = True

    def handle_input(self, key):
        """Maneja la entrada del teclado para mover o rotar la pieza."""
        if self.game_over:
            return
        
        if key == 'KEY_LEFT':
            self.current_piece.x -= 1
            if not self.board.is_valid_move(self.current_piece):
                self.current_piece.x += 1
        elif key == 'KEY_RIGHT':
            self.current_piece.x += 1
            if not self.board.is_valid_move(self.current_piece):
                self.current_piece.x -= 1
        elif key == 'KEY_DOWN':
            self.update()
        elif key == 'KEY_UP':
            self.current_piece.rotate()
            if not self.board.is_valid_move(self.current_piece):
                self.current_piece.rotate()
                self.current_piece.rotate()
                self.current_piece.rotate()

    def draw(self, stdscr):
        """Dibuja todos los elementos del juego."""
        stdscr.clear()
        self.board.draw(stdscr)

        # Dibuja la pieza actual
        piece = self.current_piece
        for x, y in piece.shape:
            abs_x, abs_y = piece.x + x, piece.y + y
            if 0 <= abs_y < self.board.height:
                stdscr.addstr(abs_y + 1, (abs_x * 2) + 1, '■')

        # Dibuja la pieza siguiente
        stdscr.addstr(2, self.board.width * 2 + 5, "Next:")
        next_p = self.next_piece
        for x, y in next_p.shape:
            # Posicionamos la pieza siguiente en la esquina
            stdscr.addstr(y + 4, (x * 2) + self.board.width * 2 + 5, '■')

        # Dibuja la puntuación y el estado del juego
        stdscr.addstr(8, self.board.width * 2 + 5, f"Score: {self.score}")
        if self.game_over:
            stdscr.addstr(self.board.height // 2, 4, "GAME OVER")
            stdscr.addstr(self.board.height // 2 + 1, 2, "Press 'q' to quit")

        stdscr.refresh()