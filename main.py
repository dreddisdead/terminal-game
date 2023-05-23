
import scenes as s
import functions as f
import os, sys
import time
import keyboard 
import os

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
    os.system('clear')

def print_ascii_art(ascii_art):
    print(ascii_art)

def transition_to_scene(scene_ascii_art):
    clear_screen()
    print_ascii_art(scene_ascii_art)
    time.sleep(2)  # Adjust the delay time as needed


greeting = "You've got a long road ahead of you, traveler.\n" 

print_ascii_art(s.sunrise_scene)

type_text(greeting) 

time.sleep(2)

user_name = input('What is your name?\n>')



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
        type_text('You open it.')
        break  # Exit the loop after the "Open" action

    else:
        type_text('Invalid action. Please try again.')

amended_letter = f"{s.letter_top}\n Dear {user_name}" + s.letter_from_anna

transition_to_scene(amended_letter)








