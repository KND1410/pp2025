import curses

class Output:
    @staticmethod
    def display_menu(stdscr, options, selected, title="Use arrow key to move"):
        stdscr.clear()
        stdscr.addstr(5, 5, title + "\n\n")
        
        for i in range(len(options)):
            if i == selected:
                stdscr.addstr(f"{options[i]}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"{options[i]}\n")
        
        stdscr.refresh()
    
    @staticmethod
    def show_message(stdscr, message, wait=True):
        stdscr.clear()
        stdscr.addstr(0, 0, message)
        if wait:
            stdscr.addstr(1, 0, "Press any key to continue...")
            stdscr.getch()
    
    @staticmethod
    def show_list(stdscr, title, items):
        stdscr.clear()
        stdscr.addstr(0, 0, f"=== {title} ===\n\n")
        
        for i, item in enumerate(items):
            stdscr.addstr(i + 2, 0, item)
        
        stdscr.addstr(len(items) + 4, 0, "Press any key to go back...")
        stdscr.getch()