import curses

def get_string(stdscr, prompt, row, col):
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()

    curses.echo()
    input_string = stdscr.getstr(row, col + len(prompt), 20)
    curses.noecho()

    return input_string.decode('utf-8')