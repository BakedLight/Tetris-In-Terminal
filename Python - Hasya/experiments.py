# import curses

# def handle_input(screen):
#     key = screen.getch()

#     if key in (ord("q"), ord("Q")):
#         return "quit"
#     elif key in (ord("a"), ord("A"), curses.KEY_LEFT):
#         return "LEFT"
#     elif key in (ord("d"), ord("D"), curses.KEY_RIGHT):
#         return "RIGHT"
#     elif key in (ord("s"), ord("S"), curses.KEY_DOWN):
#         return "DOWN"
#     elif key in (ord("w"), ord("W"), curses.KEY_UP):
#         return "UP"

#     return None

# def main(screen):
#     curses.curs_set(0)
#     screen.nodelay(True)  

#     last_action = "None"

#     while True:
#         action = handle_input(screen)

#         if action == "quit":
#             break
#         elif action is not None:
#             last_action = action  # Update action immediately on key press

#         screen.clear()
#         screen.addstr(1, 2, "=== KEY INPUT TEST ===")
#         screen.addstr(3, 2, "Press WASD or Arrow Keys to test.")
#         screen.addstr(4, 2, "Press 'Q' to quit.")
#         screen.addstr(6, 2, f"Detected Key: [ {last_action} ]")
#         screen.refresh()

# if __name__ == "__main__":
#     curses.wrapper(main)



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
        print("Exiting Tetris")
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

        try:
            screen.addstr(2, 25, f"Score: {score}")
            screen.addstr(17, 0, f"Detected Key: [ {last_action} ]")
            screen.refresh()
            curses.napms(20)
        except curses.error:
            pass




        key = screen.getch()

        # if key == ord("q"):
        #     print("Exiting Tetris")
        #     break

        time.sleep(0.2)


# curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(main)