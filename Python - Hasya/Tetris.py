import curses # used curses for making termial interactive
import time
import random


block_shapes = []


def board_outline(screen):

    try:
        for y in range(15):
            screen.addstr(y, 0, "#|")
            screen.addstr(y, 22, "|#")

        screen.addstr(15, 0, "#|" + "#" * 20 + "|#")


    except curses.error:
        pass

def handle_input(screen):

    key = screen.getch()

    if key in (ord("q"), ord("Q")):
        return "quit"

    elif key in (ord("a"), ord("A"), curses.KEY_LEFT):
        return "left"

    elif key in (ord("d"), ord("D"), curses.KEY_RIGHT):
        return "right"

    elif key in (ord("s"), ord("S"), curses.KEY_DOWN):
        return "down"

    elif key in (ord("w"), ord("W"), curses.KEY_UP):
        return "rotate"

    return None

def main(screen):


    curses.curs_set(0) # This  removes the blinking cursor :) noiceee 

    score = 0
    is_running = True

    screen.addstr(5, 5, "Welcome to Terminal Tetris!!")
    screen.addstr(7, 5, "Press ANY key to start (Don't press the power key BITCH)")
    screen.addstr(8, 5, "Press 'q' to quit")
    screen.refresh()

    key = screen.getch()
    

    if key == ord("q"):
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

        screen.addstr(2, 25, f"Score: {score}")
        screen.addstr(17, 0, f"Detected Key: [ {last_action} ]")
        screen.refresh()
        curses.napms(20)

        key = screen.getch()

        if key == ord("q"):
            break

        time.sleep(0.2)


# curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(main)