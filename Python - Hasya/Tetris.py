import curses # used curses for making termial interactive
import time
import random


block_shapes = []


def board_outline(stdscr):


    for y in range(20):
        stdscr.addstr(y, 0, "#|")
        stdscr.addstr(y, 22, "|#")

    stdscr.addstr(20, 0, "#|" + "#" * 20 + "|#")


def main(stdscr):


    curses.curs_set(0) # This  removes the blinking cursor :) noiceee 

    score = 0
    is_running = True

    stdscr.addstr(5, 5, "Welcome to Terminal Tetris!!")
    stdscr.addstr(7, 5, "Press ANY key to start (Don't press the power key BITCH)")
    stdscr.addstr(8, 5, "Press q to quit")
    stdscr.refresh()

    key = stdscr.getch()

    if key == ord("q"):
        return


    stdscr.clear()
    stdscr.nodelay(True)

    while is_running:
        stdscr.clear()

        board_outline(stdscr)

        stdscr.addstr(2, 25, f"Score: {score}")

        key = stdscr.getch()

        if key == ord("q"):
            break

        time.sleep(0.1)


# curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(main)