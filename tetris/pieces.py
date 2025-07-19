# tetris/pieces.py

# Colores para las piezas usando códigos de color ANSI
COLORS = {
    'I': '\033[96m',  # Cyan
    'O': '\033[93m',  # Amarillo
    'T': '\033[95m',  # Magenta
    'S': '\033[92m',  # Verde
    'Z': '\033[91m',  # Rojo
    'J': '\033[94m',  # Azul
    'L': '\033[33m',  # Naranja
    'RESET': '\033[0m' # Resetea el color
}

# Definición de las formas de los tetrominós
SHAPES = {
    'I': [[(0, 0), (0, 1), (0, 2), (0, 3)]],
    'O': [[(0, 0), (0, 1), (1, 0), (1, 1)]],
    'T': [[(0, 0), (0, 1), (0, 2), (1, 1)]],
    'S': [[(0, 1), (0, 2), (1, 0), (1, 1)]],
    'Z': [[(0, 0), (0, 1), (1, 1), (1, 2)]],
    'J': [[(0, 0), (1, 0), (1, 1), (1, 2)]],
    'L': [[(0, 2), (1, 0), (1, 1), (1, 2)]],
}

class Tetromino:
    def __init__(self, x, y, shape_name):
        self.x = x
        self.y = y
        self.shape_name = shape_name
        self.shape = SHAPES[shape_name][0] # Usamos la primera rotación por defecto
        self.color = COLORS[shape_name]

    def rotate(self):
        # Lógica de rotación simple (no incluye "wall kicks")
        # Se rota la pieza sobre su propio eje local
        center = self.shape[1] # Usamos el segundo bloque como pivote
        new_shape = []
        for x, y in self.shape:
            # Transladar al origen, rotar y transladar de vuelta
            rel_x, rel_y = x - center[0], y - center[1]
            new_x, new_y = -rel_y + center[0], rel_x + center[1]
            new_shape.append((new_x, new_y))
        self.shape = new_shape