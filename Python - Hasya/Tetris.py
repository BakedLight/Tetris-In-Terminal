import curses # used curses for making termial interactive
import time
import random


block_shapes = []



def wlc_outline(screen):

    try:

        screen.addstr(1, 2, "|" + "=" * 60 + "|")

        for y in range(2,10):
            screen.addstr(y, 2, "|")
            screen.addstr(y, 63, "|")

        screen.addstr(10, 2, "|" + "=" * 60 + "|")


    except curses.error:
        pass



def board_outline(screen):

    try:
        for y in range(3,17):
            screen.addstr(y, 4, "#|")
            screen.addstr(y, 26, "|#")

        screen.addstr(17, 4, "#|" + "#" * 20 + "|#")


    except curses.error:
        pass

def handle_input(screen):

    key = screen.getch()
    screen.keypad(True)

    if key in (ord("q"), ord("Q")):
        print("Exiting Tetris")
        return "quit"

    elif key in (ord("a"), ord("A"), curses.KEY_LEFT):
        return "Left"

    elif key in (ord("d"), ord("D"), curses.KEY_RIGHT):
        return "Right"

    elif key in (ord("s"), ord("S"), curses.KEY_DOWN):
        return "Down"
    
    elif key == ord(' '):
        return "Drop"

    elif key in (ord("w"), ord("W"), curses.KEY_UP):
        return "Rotate"

    return None

def main(screen):


    curses.curs_set(0) # This  removes the blinking cursor :) noiceee 

    score = 0
    is_running = True

    wlc_outline(screen)
    screen.addstr(3, 17, "Welcome to Terminal Tetris!!")
    screen.addstr(6, 5, "Press ANY key to start (Don't press the power key BITCH)")
    screen.addstr(7, 5, "Press 'q' to quit")
    screen.refresh()

    key = screen.getch()
    

    if key == ord("q"):
        print("Exiting Tetris")
        return 


    screen.clear()
    screen.nodelay(True)

    while is_running:

        screen.clear()

        board_outline(screen)
        action = handle_input(screen)
        last_action = "None"

        if action == "quit":
            break
        elif action is not None:
            last_action = action

        screen.addstr(6, 30, f"Score: {score}")
        screen.addstr(19, 5, f"Detected Key: [ {last_action} ]")
        screen.refresh()
        curses.napms(20)

        key = screen.getch()

        # if key == ord("q"):
        #     print("Exiting Tetris")
        #     break

        time.sleep(0.1)


# curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(main)