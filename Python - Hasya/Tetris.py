import curses # used curses for making termial interactive
import time
import random



def main(stdscr):

    curses.curs_set(0) # This  removes the blinking cursor :) noiceee  
    
    stdscr.nodelay(True) 

    is_running = True
    score = 0

    while is_running:
            key = stdscr.getch()
            
            if key == ord('q'):
                is_running = False


            stdscr.clear()
                    
                  
            stdscr.addstr("Welcome to Terminal Tetris!\n")
            stdscr.addstr(f"Score: {score}\n")
            stdscr.addstr("Press 'q' to quit.\n")
                    
            stdscr.refresh() 
                    


if __name__ == "__main__":
    curses.wrapper(main)
