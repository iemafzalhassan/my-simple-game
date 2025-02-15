import curses
import random
from rich.console import Console

console = Console()

# Game Constants
HEIGHT, WIDTH = 20, 50
SNAKE_COLOR = 2  # Green
FOOD_COLOR = 3   # Red
BORDER_COLOR = 4  # Blue

def init_colors():
    curses.start_color()
    curses.init_pair(SNAKE_COLOR, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(FOOD_COLOR, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(BORDER_COLOR, curses.COLOR_BLUE, curses.COLOR_BLACK)

def draw_border(win):
    win.attron(curses.color_pair(BORDER_COLOR))
    for i in range(WIDTH):
        win.addch(0, i, "█")
        win.addch(HEIGHT-1, i, "█")
    for i in range(HEIGHT):
        win.addch(i, 0, "█")
        win.addch(i, WIDTH-1, "█")
    win.attroff(curses.color_pair(BORDER_COLOR))

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)  # Snake speed

    init_colors()
    
    # Initialize snake and food
    snake = [(10, 15), (10, 14), (10, 13)]
    direction = "RIGHT"
    food = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))

    while True:
        stdscr.clear()
        draw_border(stdscr)

        # Draw snake
        for y, x in snake:
            stdscr.attron(curses.color_pair(SNAKE_COLOR))
            stdscr.addch(y, x, "■")
            stdscr.attroff(curses.color_pair(SNAKE_COLOR))

        # Draw food
        stdscr.attron(curses.color_pair(FOOD_COLOR))
        stdscr.addch(food[0], food[1], "🍎")
        stdscr.attroff(curses.color_pair(FOOD_COLOR))

        # Get user input
        key = stdscr.getch()
        if key in [curses.KEY_UP, ord('w')] and direction != "DOWN":
            direction = "UP"
        elif key in [curses.KEY_DOWN, ord('s')] and direction != "UP":
            direction = "DOWN"
        elif key in [curses.KEY_LEFT, ord('a')] and direction != "RIGHT":
            direction = "LEFT"
        elif key in [curses.KEY_RIGHT, ord('d')] and direction != "LEFT":
            direction = "RIGHT"

        # Move the snake
        y, x = snake[0]
        if direction == "UP":
            y -= 1
        elif direction == "DOWN":
            y += 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1

        new_head = (y, x)

        # Check collision
        if new_head in snake or y == 0 or y == HEIGHT-1 or x == 0 or x == WIDTH-1:
            stdscr.addstr(HEIGHT//2, WIDTH//3, "GAME OVER! Press any key.", curses.color_pair(FOOD_COLOR))
            stdscr.refresh()
            stdscr.getch()
            break

        # Add new head and check food
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))
        else:
            snake.pop()

        stdscr.refresh()

curses.wrapper(main)

