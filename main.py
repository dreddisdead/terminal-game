
import scenes as s
import functions as f
import os, sys
import time
import keyboard 
import os
import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10, "Hello World")
    stdscr.refresh()
    stdscr.getch()
    
wrapper(main)


def set_terminal_size(width, height):
    os.system(f'printf "\\e[8;{height};{width}t"')

# Set terminal size to 96 columns and 46 rows
set_terminal_size(96, 46)

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

### Checks if being run on non-Windows system (Git Bash) and clears terminal
def clear_screen():
    os.system('cls')

def print_ascii_art(ascii_art):
    print(ascii_art)

def transition_to_scene(scene_ascii_art):
    clear_screen()
    print_ascii_art(scene_ascii_art)
    time.sleep(2)  # Adjust the delay time as needed


### putting this away for now

for_now = """user_name = input('What is your name?\n>')


greeting = f"A grand adventure awaits you, {user_name}.\n" 

print_ascii_art(s.sunrise_scene)

type_text(greeting)
type_text("Wake up.")

time.sleep(2)

clear_screen()





transition_to_scene(s.mailbox_scene)

#user_birthday = input('What is your date of birth (mm/dd):\n')

#print(f"You're a {f.zodiac_sign(user_birthday)}")
look_counter = 0
while True:
    action = input('(Look/Open)\n')

    if action == 'Look':
        # Look at mailbox
        if look_counter >= 2:
            type_text('You really enjoy looking at this mailbox.')
            time.sleep(1)
            type_text('As long as you are happy, I guess...')
            time.sleep(2)
            continue
        else:
            type_text('It is, in fact, a mailbox.')
            look_counter += 1
            continue  # Continue to prompt for input again

    elif action == 'Open':
        # Open mail
        type_text('You open the mail.')
        type_text('It is mostly spam and ads.')
        time.sleep(1)
        type_text('Oh wait.')
        time.sleep(1)
        type_text('There is a letter for you.')
        time.sleep(1)
        type_text('You open it.')
        break  # Exit the loop after the "Open" action

    else:
        type_text('Invalid action. Please try again.')

amended_letter = f"{s.letter_top}\n Dear {user_name}" + s.letter_from_anna

transition_to_scene(amended_letter)

input("Press Enter to Continue")

cafe = "el cafe"

transition_to_scene(cafe)

type_text('A few days later...', 0.08)

type_text('You find yourself in line to order at a local cafe. Quite a nice place. ')
time.sleep(1)
type_text('To be honest')
time.sleep(2)
type_text("You're not entirely sure who you're looking for...")
time.sleep(0.5)
type_text("You're hoping they recognize you first.")
time.sleep(1)

# look counter resets to zero
look_counter = 0
while True:
    action = input('(Look/Order)\n')

    if action == 'Look':
        # Look around in cafe
        if look_counter >= 2:
            type_text("Yes, yes...")
            time.sleep(1)
            type_text('A very nice cafe, indeed.')
            time.sleep(2)
            continue
        else:
            type_text("You look around at the beautiful art on nearly every wall.")
            type_text("This place radiates passion and comfort elegantly.")

            look_counter += 1
            continue  # Continue to prompt for input again

    elif action == 'Order':
        # Make an order
        type_text("You walk up to the counter and the employee greets you.\n")
        time.sleep(1)
        type_text("Hello, Welcome to Abrianna's Cafe and Bakery!")
        type_text("Home to tasty homemade sweets and heartwarming food.")
        time.sleep(1)
        type_text("What would you like to order?")
        # Show featured items
        time.sleep(1)
        print(s.menu)
        menu_items = []
        menu_choice = input("Order Here:\n")
        break  # Exit the loop after the "Open" action

    else:
        type_text('Invalid action. Please try again.')"""







