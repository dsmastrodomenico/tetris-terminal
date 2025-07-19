# tetris/main.py
import curses
import time
from tetris.game import Game

def main(stdscr):
    # Configuración de curses
    curses.curs_set(0) # Oculta el cursor
    stdscr.nodelay(1) # No bloquea la espera de entrada
    stdscr.timeout(300) # Tiempo de espera para la entrada (velocidad del juego)

    # Dimensiones del tablero
    height, width = 20, 10
    game = Game(height, width)

    while not game.game_over:
        try:
            key = stdscr.getkey()
            if key in ['q', 'Q']:
                break
            game.handle_input(key)
        except curses.error:
            # No se presionó ninguna tecla, la pieza cae
            game.update()
        
        game.draw(stdscr)

    # Espera a que el usuario presione 'q' para salir después de Game Over
    while True:
        try:
            key = stdscr.getkey()
            if key in ['q', 'Q']:
                break
        except:
            time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(main)