import curses

def get_string(stdscr, prompt, row, col, maxlen=20):
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()
    curses.echo()
    stdscr.move(row, col + len(prompt))
    input_bytes = stdscr.getstr()
    curses.noecho()
    
    if isinstance(input_bytes, bytes):
        try:
            return input_bytes.decode('utf-8')
        except Exception:
            return input_bytes
    return input_bytes