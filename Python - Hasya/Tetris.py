import curses # used curses for making termial interactive
import time
import random



def board_outline(stdscr, width=20, height=20):
    left_side = "#|"
    right_side = "|#"

    
    for y in range(height):

        try:
            stdscr.addstr(y, 0, left_side + " " * width + right_side)
        except curses.error:
            pass 
        
    
    bottom_border = "#|" + "#" * width + "|#"
    try:
        stdscr.addstr(height, 0, bottom_border)
    except curses.error:
        pass
        


def main(stdscr):

    curses.curs_set(0) # This  removes the blinking cursor :) noiceee 
    
    stdscr.nodelay(False) 

    score = 0

    stdscr.clear()

    stdscr.addstr(4, 5, "Welcome to Terminal Tetris!")
    stdscr.addstr(7, 5, f"Score: {score}")
    stdscr.addstr(8, 5, "Press ANY key to start (Don't press the power key BITCH)")
    stdscr.addstr(9, 5, "Press 'q' to quit.")


    stdscr.refresh() 


    key = stdscr.getch()
    if key == ord('q'):
        return 


    stdscr.clear()
    
    stdscr.nodelay(True)
    is_running = True

    while is_running:

        board_outline(stdscr)
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('q'):
            is_running = False
            
        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(main)




