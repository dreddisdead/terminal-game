import curses
from curses import wrapper
from game import Game
from game import GameScenes



def main(stdscr):
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    game = Game(stdscr)
    game.game_loop()


# Run the main function
wrapper(main)