# tetris/board.py
import curses

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        # La grilla ahora almacenará los símbolos específicos
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def draw(self, stdscr):
        """Dibuja el tablero y los bordes en la pantalla."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                # Dibuja el símbolo que está en la celda
                stdscr.addstr(y + 1, x * 2 + 1, cell)

        # Dibuja los bordes del tablero
        for y in range(self.height + 2):
            stdscr.addstr(y, 0, '█')
            stdscr.addstr(y, self.width * 2 + 1, '█')
        for x in range(self.width * 2 + 2):
            stdscr.addstr(0, x, '█')
            stdscr.addstr(self.height + 1, x, '▀')


    def is_valid_move(self, piece):
        """Verifica si la posición actual de la pieza es válida."""
        for x, y in piece.shape:
            abs_x, abs_y = piece.x + x, piece.y + y
            if not (0 <= abs_x < self.width and 0 <= abs_y < self.height):
                return False # Fuera de los límites
            if self.grid[abs_y][abs_x] != ' ':
                return False # Colisión con otra pieza
        return True

    def place_piece(self, piece):
        """Coloca una pieza permanentemente en el tablero."""
        for x, y in piece.shape:
            abs_x, abs_y = piece.x + x, piece.y + y
            if 0 <= abs_y < self.height and 0 <= abs_x < self.width:
                self.grid[abs_y][abs_x] = piece.symbol

    def clear_lines(self):
        """Verifica y limpia las líneas completas."""
        lines_cleared = 0
        new_grid = [row for row in self.grid if any(cell == ' ' for cell in row)]
        lines_cleared = self.height - len(new_grid)
        
        # Añade nuevas líneas vacías en la parte superior
        for _ in range(lines_cleared):
            new_grid.insert(0, [' ' for _ in range(self.width)])
        
        self.grid = new_grid
        return lines_cleared