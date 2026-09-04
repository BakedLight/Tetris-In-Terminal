import curses

def handle_input(screen):
    key = screen.getch()

    if key in (ord("q"), ord("Q")):
        return "quit"
    elif key in (ord("a"), ord("A"), curses.KEY_LEFT):
        return "LEFT"
    elif key in (ord("d"), ord("D"), curses.KEY_RIGHT):
        return "RIGHT"
    elif key in (ord("s"), ord("S"), curses.KEY_DOWN):
        return "DOWN"
    elif key in (ord("w"), ord("W"), curses.KEY_UP):
        return "UP"

    return None

def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)  

    last_action = "None"

    while True:
        action = handle_input(screen)

        if action == "quit":
            break
        elif action is not None:
            last_action = action  # Update action immediately on key press

        screen.clear()
        screen.addstr(1, 2, "=== KEY INPUT TEST ===")
        screen.addstr(3, 2, "Press WASD or Arrow Keys to test.")
        screen.addstr(4, 2, "Press 'Q' to quit.")
        screen.addstr(6, 2, f"Detected Key: [ {last_action} ]")
        screen.refresh()

if __name__ == "__main__":
    curses.wrapper(main)