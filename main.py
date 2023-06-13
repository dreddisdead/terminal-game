import curses
import sys
import time

from curses import wrapper
from curses.textpad import Textbox, rectangle
from enum import Enum

# Define an enumeration for menu options
class MenuOptions(Enum):
    PLAY = "Play"
    EXIT = "Exit"


class ExitChoices(Enum):
    YES = "Yes"
    NO = "No"


class PauseChoices(Enum):
    RESUME = "Resume"
    OPTIONS = "Options"
    QUIT = "Quit to Main Menu"
    
class BedroomChoices(Enum):
    PILLOW = "Pillow"
    DRESSER = "Dresser"
    WINDOW = "Window"
    BATHROOM = "Bathroom"
    LEAVE = "Leave Bedroom"
    
class HallwayChoices(Enum):
    PAINTINGS_LEFT = "Paintings (Left)"
    PAINTINGS_RIGHT = "Paintings (Right)"
    DOOR = "Check out the Door"
    CONTINUE = "Continue Down Hallway"
    
class QuestionChoices(Enum):
    WHO = "Who are you?"
    WHAT = "What is this place?"
    WHY = "Why am I here?"
    LEAVE = "How do I leave?"
    
class FearChoices(Enum):
    SPIDERS = "Spiders"
    HEIGHTS = "Heights"
    FAILURE = "Failure"
    DARKNESS = "Darkness"
    
class RegretChoices(Enum):
    DREAMS = "Not pursuing my dreams"
    HURTING = "Hurting someone I love"
    WASTING = "Wasting my life"
    RISKS = "Not taking risks"
    
    
class Menu:
    def __init__(self, stdscr, options, title):
        self.title = title
        self.stdscr = stdscr
        self.options = options
        self.current_row_idx = 0

    def center_text(self, text):
        h, w = self.stdscr.getmaxyx()
        x = w // 2 - len(text) // 2
        y = h // 2 - 4
        self.stdscr.addstr(y, x, text)
    
    def print_menu(self):
        self.stdscr.clear()
        self.center_text(self.title)
        h, w = self.stdscr.getmaxyx()
        for idx, option in enumerate(self.options):
            x = w//2 - len(option.value)//2
            y = h//2 - 2 + idx
            if idx == self.current_row_idx:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, option.value)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, option.value)
        self.stdscr.refresh()

    def navigate(self):
        while True:
            key = self.stdscr.getch()
            if key == curses.KEY_UP and self.current_row_idx > 0:
                self.current_row_idx -= 1
            elif key == curses.KEY_DOWN and self.current_row_idx < len(self.options) - 1:
                self.current_row_idx += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                return self.options[self.current_row_idx]
            self.print_menu()


class GameScenes:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        
    def wrap_text(self, text, width):
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            # If adding a new word doesn't push the length
            # over the window's width, add the word to the current line
            if len(' '.join(current_line + [word])) < width:
                current_line.append(word)
            else:
                # Otherwise, add the current line to the list of lines
                # and start a new line with the current word
                lines.append(' '.join(current_line))
                current_line = [word]

        # Add the last line
        lines.append(' '.join(current_line))

        return lines

  
    def typed_text(self, text, attr=None, speed=0.02):
        h, w = self.stdscr.getmaxyx()
        margin = 25  # Set your desired margin here
        w = w - 2 * margin  # Adjust width for the margins
        y = h // 2 - len(self.wrap_text(text, w)) // 2  # Adjust y to take into account the number of lines

        lines = self.wrap_text(text, w)

        for line in lines:
            x = w // 2 - len(line) // 2 + margin  # Adjust x for the left margin
            if x < w and y < h:  # Ensure x and y are within the window's boundaries
                for char in line:
                    if attr is not None:
                        self.stdscr.attron(attr)
                    self.stdscr.addch(y, x, char)
                    if attr is not None:
                        self.stdscr.attroff(attr)
                    self.stdscr.refresh()
                    time.sleep(speed)
                    x += 1
                y += 1

        self.stdscr.getch()
 

    def center_text(self, text):
        h, w = self.stdscr.getmaxyx()
        y = h // 2
        lines = self.wrap_text(text, w)

        for line in lines:
            x = w // 2 - len(line) // 2
            if x < w and y < h:  # Ensure x and y are within the window's boundaries
                self.stdscr.addstr(y, x, line)
                y += 1
    ###NEW CODE
    def question_screen(self, title, choices):
        question_menu = Menu(self.stdscr, choices, title)
        question_menu.center_text(title)
        question_menu.print_menu()

        chosen_option = question_menu.navigate()
        return chosen_option
    
    ###BOSS FIGHT
    def refusal(self):
        self.stdscr.nodelay(True)  # Make getch non-blocking
        
        self.stdscr.clear()
        self.stdscr.refresh()

        # Display the boss fight scene
        self.typed_text("A mysterious figure stands before you.")
        time.sleep(1)        
        
        blue_message_one = "You can't leave this place. I won't allow it."
        blue_message_two = "This place is your mind, a prison of your own making."
        blue_message_three = "I am the embodiment of your fears, doubts, and regrets."
        blue_message_four = "If you truly want to leave this place, you must confront and overcome me."
        
        for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four]:
            self.stdscr.clear()
            self.typed_text(message, curses.color_pair(2))
            time.sleep(1.5)
            
        # First question screen
        title = "What is your greatest fear?"
        choices = list(FearChoices)
        chosen_option = self.question_screen(title, choices)

        # Handle the chosen option for the first question
        if chosen_option == choices[0]:
            # Handle the outcome for the first choice
            self.stdscr.clear()
            self.typed_text("You chose Spiders.")
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("You chose Heights.")
            time.sleep(1.5)
        elif chosen_option == choices[2]:
            # Handle the outcome for the third choice
            self.stdscr.clear()
            self.typed_text("You chose Failure.")
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            # Handle the outcome for the fourth choice
            self.stdscr.clear()
            self.typed_text("You chose Darkness.")
            time.sleep(1.5)

        self.stdscr.clear()
        self.stdscr.refresh()

        # Second question screen
        title = "What is your biggest regret?"
        choices = list(RegretChoices)
        chosen_option = self.question_screen(title, choices)

        # Handle the chosen option for the second question
        if chosen_option == choices[0]:
            # Handle the outcome for the first choice
            self.stdscr.clear()
            self.typed_text("You chose Not pursuing my dreams.")
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("You chose Hurting someone I love.")
            time.sleep(1.5)
        elif chosen_option == choices[2]:
            # Handle the outcome for the third choice
            self.stdscr.clear()
            self.typed_text("You chose Wasting my life.")
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            # Handle the outcome for the fourth choice
            self.stdscr.clear()
            self.typed_text("You chose Not taking risks.")
            time.sleep(1.5)

        # ... continue with more question screens ...

        self.stdscr.nodelay(False)  # Make getch blocking again
        
    def intro(self):
        self.stdscr.nodelay(True)  # Make getch non-blocking

        # Display the intro sequence
        for title in ["Welcome!", "So glad you could make it.", "What is your name?"]:
            self.stdscr.clear()
            self.center_text(title)
            self.stdscr.refresh()
            time.sleep(1)

        # Ask for the user's name
        height, width = 1, 18
        start_y, start_x = self.stdscr.getmaxyx()
        start_y = start_y // 2 + 2
        win = curses.newwin(height, width, start_y, (start_x - width) // 2)
        rectangle(self.stdscr, start_y - 1, (start_x - width) // 2 - 1, start_y + height, (start_x + width) // 2)
        self.stdscr.refresh()
        win.keypad(True)  # Allow special keys to be recognized

        box = Textbox(win, insert_mode=True)

        while True:
            box.edit()
            user_name = box.gather().strip()

            if len(user_name) <= width:
                break
            else:
                win.clear()
                win.refresh()

        greeting = "We're excited to have you, " + user_name + "!"
        self.stdscr.clear()
        self.center_text(greeting)
        self.stdscr.refresh()
        time.sleep(2)

        self.stdscr.nodelay(False)  # Return getch to blocking mode
        
    def bedroom(self, bedroom_menu):
        glasses_found = False
        # No delay on getch
        self.stdscr.nodelay(True)
        # Display narration sequence
        for narration in ["...you're sleeping soundly...", "...the land of dreams...", "...where polarities dissolve into one...", "...one true form...", "...emptiness..."]:
            self.stdscr.clear()
            self.typed_text(narration)
            time.sleep(1)
        # Display thought sequence
        thought_chunk_one = "Rudely awakened by sunlight's laser-show on your eyelids, you squint for dear life."
        thought_chunk_two = "Thankfully, your vision was not permanently damaged!"
        thought_chunk_three = "You sit at the edge of the bed as your eyes recover, hopelessly observing the blurred image you call a room. Better find your glasses unless you've always fancied life in a hopsital."
        thought_chunk_four = "Seriously, you can't see anything without them."
        for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
            self.stdscr.clear()
            self.typed_text(observed_thought)
            time.sleep(1.4)

        # After the dialog finishes, show the new menu
        bedroom_menu.print_menu()
        while True:
            chosen_bedroom_option = bedroom_menu.navigate()
            if chosen_bedroom_option == BedroomChoices.PILLOW:                
                thought_chunk_one = "You look under the pillow..."               
                thought_chunk_two = "You found nothing."               
                thought_chunk_three = "Oh wait,"               
                thought_chunk_four = "Nope. Still nothing."
                for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
                    self.stdscr.clear()
                    self.typed_text(observed_thought)
                    time.sleep(1.4)      
            elif chosen_bedroom_option == BedroomChoices.DRESSER:
                self.stdscr.clear()
                self.typed_text("You look in the dresser... It's empty.")
                time.sleep(1)
            elif chosen_bedroom_option == BedroomChoices.WINDOW:
                thought_chunk_one = "You look out the window..."
                thought_chunk_two = "What most people would see as a beautiful day, you see"           
                thought_chunk_three = "Well, nothing."            
                thought_chunk_four = "You're blind without your glasses, remember?"
                for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
                    self.stdscr.clear()
                    self.typed_text(observed_thought)
                    time.sleep(1.4)  
            elif chosen_bedroom_option == BedroomChoices.BATHROOM:
                self.stdscr.clear()
                if not glasses_found:
                    self.typed_text("You go to the bathroom... You found your glasses!")
                    glasses_found = True
                    time.sleep(1)
                else:
                    self.typed_text("There's nothing else here.")
                    time.sleep(1)
            elif chosen_bedroom_option == BedroomChoices.LEAVE:
                if glasses_found:
                    self.stdscr.clear()
                    self.typed_text("You leave the bedroom...")
                    time.sleep(1)
                    break  # Exits the bedroom menu and continue with the game
                else:
                    self.stdscr.clear()
                    self.typed_text("You can't leave without your glasses!")
                    time.sleep(1)
                    
        self.stdscr.nodelay(False)  # Return getch to blocking mode
    
    def mystery_room(self, question_menu):
        # No delay on getch
        self.stdscr.nodelay(True)
        # Player is introduced to new character
        self.stdscr.clear()
        # New character has their own color
        self.typed_text("Can I help you?", curses.color_pair(2))
        time.sleep(.8)
        
        thought_chunk_one = "'Who said that?' you think to yourself."
        thought_chunk_two = "Surely that didn't come from the radio."
        thought_chunk_three = "Actually."
        thought_chunk_four = "Where is the radio?"
        thought_chunk_five = "Uh..."
        thought_chunk_six = "This isn't the room you were just in."
        thought_chunk_seven = "'How did I get here?' you think to yourself."
        thought_chunk_eight = "You find yourself in seemingly and endless dark void."
        thought_chunk_nine = "No walls. No ceiling. No floor."
        thought_chunk_ten = "Just you and the voice you heard."
        for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five, thought_chunk_six, thought_chunk_seven, thought_chunk_eight, thought_chunk_nine, thought_chunk_ten]:
            self.stdscr.clear()
            self.typed_text(observed_thought)
            time.sleep(1.4)
            
        self.stdscr.clear()    
        blue_message_one = "Well clearly you're occupied with a panic attack right now."
        blue_message_two = "Listen..."
        blue_message_three = "I understand you're confused."
        blue_message_four = "I'm confused too."
        blue_message_five = "You shouldn't be here."
        blue_message_six = "This place isn't for the living."
        blue_message_seven = "Well..."
        blue_message_eight = "I suppose the only thing I can do is answer your questions."
        blue_message_nine = "Seems like you have a lot of them."
        blue_message_ten = "It's written all over your face."
        for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four, blue_message_five, blue_message_six, blue_message_seven, blue_message_eight, blue_message_nine, blue_message_ten]:
            self.stdscr.clear()
            self.typed_text(message, curses.color_pair(2))
            time.sleep(.8)
        
        question_menu.print_menu()
        
        while True:
            chosen_question_option = question_menu.navigate()
            
            if chosen_question_option == QuestionChoices.WHO:
                self.stdscr.clear()
                blue_message_one = "That's a little complicated."
                blue_message_two = "I'm not sure how to answer that."
                blue_message_three = "You're not going to like the answer."
                for message in [blue_message_one, blue_message_two, blue_message_three]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(.8)
        
            elif chosen_question_option == QuestionChoices.WHAT:
                self.stdscr.clear()
                blue_message_one = "A place where you can make your dreams come true in an INSTANT."
                blue_message_two = "A wonderful place indeed."
                blue_message_three = "There's one thing I know for certain."
                blue_message_four = "Things in this world don't make sense."
                blue_message_five = "It's what you make of it."
                blue_message_six = "Like a good dream."
                for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four, blue_message_five, blue_message_six]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(.8)
            elif chosen_question_option == QuestionChoices.WHY:
                self.stdscr.clear()
                blue_message_one = "Why are you so worried about how you got here?"
                blue_message_two = "You're here now."
                blue_message_three = "You can't change that."
                for message in [blue_message_one, blue_message_two, blue_message_three]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(.8)
                
            elif chosen_question_option == QuestionChoices.LEAVE:
                self.stdscr.clear()
                self.typed_text("You can't leave.", curses.color_pair(3))
                time.sleep(.03)
                self.stdscr.clear()
                blue_message_one = "I mean... you can't leave just yet!"
                blue_message_two = "There's so much here for you to explore."
                blue_message_three = "With me!"
                blue_message_four = "..."
                blue_message_five = "What's that?"
                blue_message_six = "You want to wake up?"
                blue_message_seven = "No."
                blue_message_eight = "You don't want to wake up."
                blue_message_nine = "You want to stay here with me."
                for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four, blue_message_five, blue_message_six, blue_message_seven, blue_message_eight, blue_message_nine]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(1.5)
                self.stdscr.clear()
                self.typed_text("Forever.", curses.color_pair(3))
                time.sleep(3)
                break  # Exits the question menu and continue with the game
                
        # Reset getch to blocking mode
        self.stdscr.nodelay(False) 
        
        # Transition to refusal to leave (Boss fight)
        self.stdscr.clear()
        self.refusal()
        
    def endless_hallway(self):
            # Player realizes they're in an endless hallway
            thought_chunk_one = "Something feels off..."
            thought_chunk_two = "Wait a minute."
            thought_chunk_three = "Every time you turn the corner, you're back in the same hallway."
            thought_chunk_four = "Looking down the same hallway, you see the same door."
            thought_chunk_five = "Over."
            thought_chunk_six = "And over."
            thought_chunk_seven = "And over."
            thought_chunk_eight = "And over."
            for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five, thought_chunk_six, thought_chunk_seven, thought_chunk_eight]:
                self.stdscr.clear()
                self.typed_text(observed_thought)
                time.sleep(1.4)
            # Player is forced to go forward into the door  
            thought_chunk_one = "You feel yourself begin to panic."
            thought_chunk_two = "You take a deep breath."
            thought_chunk_three = "You understand that you cannot escape this hallway."
            thought_chunk_four = "There's only one way you can go."
            thought_chunk_five = "Forward."  
            for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five]:
                self.stdscr.clear()
                self.typed_text(observed_thought)
                time.sleep(1.8)
            thought_chunk_one = "You slowly approach the door."
            thought_chunk_two = "You can still hear music playing on the other side."
            thought_chunk_three = "Gently, you place your hand on the doorknob."
            thought_chunk_four = "The music stops abrubtly."
            thought_chunk_five = "Your heart rate increases."
            thought_chunk_six = "You don't know why, but your heart is thumping in your chest."
            thought_chunk_seven = "You begin to sweat."
            thought_chunk_eight = "'Just open the door,' you think to yourself."
            for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five]:
                self.stdscr.clear()
                self.typed_text(observed_thought)
                time.sleep(1.4)
            
            
        
    def hallway(self, hallway_menu):
        door_checked = False
        # No delay on getch
        self.stdscr.nodelay(True)
        # Display narration sequence
        for narration in ["You step out into the hallway", "Paintings and art line the walls left and right", "The hallway continues further down and to the right", "There, you'll reach the living room", "For now you just stand outside your bedroom"]:
            self.stdscr.clear()
            self.typed_text(narration)
            time.sleep(1)
        # Display thought sequence
        thought_chunk_one = "You feel a sense of calm as you look at the paintings on the wall."
        thought_chunk_two = "'What a nice place to live.' you think to yourself."
        thought_chunk_three = "As you look down the hallway, you see a door ahead of you."
        thought_chunk_four = "It's not quite closed all the way, and you can see a sliver of light coming from the other side."
        for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
            self.stdscr.clear()
            self.typed_text(observed_thought)
            time.sleep(1.4)
            
        # After the dialog finishes, show the new menu
        hallway_menu.print_menu()
        
        while True:
            chosen_hallway_option = hallway_menu.navigate()
            if chosen_hallway_option == HallwayChoices.PAINTINGS_LEFT:
                self.stdscr.clear()
                self.typed_text("You look at the paintings on your left...")
                time.sleep(1)
            elif chosen_hallway_option == HallwayChoices.PAINTINGS_RIGHT:
                self.stdscr.clear()
                self.typed_text("You look at the paintings on your right...")
                time.sleep(1)
                
            elif chosen_hallway_option == HallwayChoices.DOOR:
                self.stdscr.clear()
                if not door_checked:
                    thought_chunk_one = "You approach the door... it's slightly ajar."
                    thought_chunk_two = "Just enough to see through the crack..."
                    thought_chunk_three = "There's no one in the room, but you can hear music playing."
                    thought_chunk_four = "It sounds like it's coming from a radio."
                    thought_chunk_five = "You can't make out the song, but it sounds familiar."
                    for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five]:
                        self.stdscr.clear()
                        self.typed_text(observed_thought)
                        time.sleep(1.4)
                    door_checked = True
                    
                else:
                    self.typed_text("There's nothing else to see here.")
                    time.sleep(1)
            elif chosen_hallway_option == HallwayChoices.CONTINUE:
                if door_checked:
                    self.stdscr.clear()
                    self.typed_text("You continue down the hallway and make a right...")
                    time.sleep(1)
                    break  # Exits the hallway menu and continue with the game
                else:
                    self.stdscr.clear()
                    self.typed_text("You should check out the rest of this area before you leave.")
                    time.sleep(1)
                    
        self.endless_hallway()
                        
        # Reset getch to blocking mode
        self.stdscr.nodelay(False)
        
    
class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.main_menu = Menu(stdscr, list(MenuOptions), "Main Menu")
        self.pause_menu = Menu(stdscr, list(PauseChoices), "Paused")
        self.exit_menu = Menu(stdscr, list(ExitChoices), "Are you sure you want to exit?")
        self.bedroom_menu = Menu(stdscr, list(BedroomChoices), "Find your glasses.")
        self.hallway_menu = Menu(stdscr, list(HallwayChoices), "What's behind the door?")
        self.question_menu = Menu(stdscr, list(QuestionChoices), "Ask a question.")
        self.scenes = GameScenes(stdscr)

    def game_loop(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.scenes.intro()
        self.main_menu.print_menu()
        while True:
            chosen_option = self.main_menu.navigate()
            if chosen_option == MenuOptions.PLAY:
                self.play_game()
            elif chosen_option == MenuOptions.EXIT:
                self.exit_menu.print_menu()
                chosen_exit_option = self.exit_menu.navigate()
                if chosen_exit_option == ExitChoices.YES:
                    sys.exit()
                elif chosen_exit_option == ExitChoices.NO:
                    self.main_menu.print_menu()

    def play_game(self):
        while True:
            # insert the actual game logic here
            #self.scenes.bedroom(self.bedroom_menu)
            #self.scenes.hallway(self.hallway_menu)
            self.scenes.mystery_room(self.question_menu)
            
            key = self.stdscr.getch()
            if key == ord('p') or key == ord('P'):
                self.pause_menu.print_menu()
                chosen_pause_option = self.pause_menu.navigate()
                if chosen_pause_option == PauseChoices.QUIT:
                    break
                
        self.main_menu.print_menu()
def main(stdscr):
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    game = Game(stdscr)
    game.game_loop()


# Run the main function
wrapper(main)
 