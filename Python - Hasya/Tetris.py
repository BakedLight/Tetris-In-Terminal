import curses # used curses for making termial interactive
import time
import random



def main(stdscr):

    curses.curs_set(0) # This  removes the blinking cursor :) noiceee  
    
    stdscr.nodelay(True) 

if __name__ == "__main__":
    curses.wrapper(main)