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
# La estructura ahora es un diccionario donde la clave es el nombre de la forma
# y el valor es una tupla que contiene la forma y el símbolo.
SHAPES_AND_SYMBOLS = {
    'I': ([[(0, 0), (0, 1), (0, 2), (0, 3)]], 'I'),
    'O': ([[(0, 0), (0, 1), (1, 0), (1, 1)]], 'O'),
    'T': ([[(0, 0), (0, 1), (0, 2), (1, 1)]], 'T'),
    'S': ([[(0, 0), (0, 1), (1, -1), (1, 0)]], 'S'),
    'Z': ([[(0, -1), (0, 0), (1, 0), (1, 1)]], 'Z'),
    'J': ([[(0, 0), (1, 0), (1, 1), (1, 2)]], 'J'),
    'L': ([[(0, 2), (1, 0), (1, 1), (1, 2)]], 'L'),
}

class Tetromino:
    def __init__(self, x, y, shape_name):
        self.x = x
        self.y = y
        self.shape_name = shape_name
        
        # Obtenemos la forma y el símbolo del nuevo diccionario
        shape_info = SHAPES_AND_SYMBOLS[shape_name]
        self.shape = shape_info[0][0]
        self.symbol = shape_info[1] # <--- NUEVO: Almacenamos el símbolo
        
        self.color = COLORS[shape_name]

    def rotate(self):
        # La lógica de rotación no necesita cambios
        center = self.shape[1]
        new_shape = []
        for x, y in self.shape:
            rel_x, rel_y = x - center[0], y - center[1]
            new_x, new_y = -rel_y + center[0], rel_x + center[1]
            new_shape.append((new_x, new_y))
        self.shape = new_shape