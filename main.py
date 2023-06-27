import curses
import sys
import time

from curses import wrapper
from curses.textpad import Textbox, rectangle
from enum import Enum

# Define enums for menus and choices
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
    
class ColorChoices(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    ORANGE = "Orange"
    
class GiveUpChoices(Enum):
    MEMORY = "Your memories"
    EMOTIONS = "Your ability to feel emotions"
    TIME = "Your sense of time"
    IMAGINATION = "Your imagination"
    
class GameOverChoices(Enum):
    TRY_AGAIN = "Try Again"
    EXIT = "Exit Game"
    
class BossBattleQuitChoices(Enum):
    YES = "Yes"
    NO = "No"
    
class FreeWillChoices(Enum):
    FREE_WILL = "We are free and every choice is ours."
    FATE = "Everything is already decided, we just don't know it."
    CHOICE_AND_FATE = "Our choices are a mix of what we want and what's meant to happen."
    DONT_KNOW = "What if we're just playing out a story that's already been written?"
    
class ControlChoices(Enum):
    YES = "Yes"
    NO = "No"
    

class WhoChoices(Enum):
    IDK = "I don't know"
    YOU = "I am you"
    
    
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
        self.MAX_WILLPOWER = 20
        self.willpower = self.MAX_WILLPOWER
         
                
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
    
    def question_screen(self, title, choices):
        question_menu = Menu(self.stdscr, choices, title)
        question_menu.center_text(title)
        question_menu.print_menu()

        chosen_option = question_menu.navigate()
        return chosen_option

    def game_over(self):
        self.stdscr.clear()
        
        title = "GAME OVER"
        choices = list(GameOverChoices)
        chosen_option = self.question_screen(title, choices)
        
        # Handle the chosen option for game over
        if chosen_option == choices[0]:
            # Handle the outcome for the first choice
            self.stdscr.clear()
            self.typed_text("I believe in you!", curses.color_pair(4))
            time.sleep(1.5)
            self.refusal(10)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("You realize that if you exit now, you'll restart from the beginning. Do you still wish to continue?", curses.color_pair(3))
            time.sleep(3)
            
            self.stdscr.clear()
            
            title = "Are you sure you want to quit?"
            choices = list(BossBattleQuitChoices)
            chosen_option = self.question_screen(title, choices)
            
            # Handle the chosen option for quitting
            if chosen_option == choices[0]:
                # Handle the outcome for the first choice
                self.stdscr.clear()
                sys.exit()
                
            elif chosen_option == choices[1]:
                # Handle the outcome for the second choice
                self.stdscr.clear()
                self.game_over()
        
    ###BOSS FIGHT
    def refusal(self, willpower):
        self.willpower = willpower
    
        self.stdscr.nodelay(True)  # Make getch non-blocking
        
        self.stdscr.clear()
        self.stdscr.refresh()

        # Display the boss fight scene
        self.typed_text("A mysterious figure stands before you.")
        time.sleep(1)        
        
        blue_message_one = "I embody your doubts, regrets, and the echoes of past choices, intertwined with the fabric of this place."
        blue_message_two = "If you wish to leave, you must overcome me."
        
        for message in [blue_message_one, blue_message_two]:
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
            self.typed_text("You're an insignificant, mere speck in the vastness of the universe.", curses.color_pair(3))
            self.willpower -= 8
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("Your heart is racing at the speed of light.", curses.color_pair(2))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("Just kidding, that's not actually possible.", curses.color_pair(2))
            self.willpower += 5
            time.sleep(1.5)
        elif chosen_option == choices[2]:
            # Handle the outcome for the third choice
            self.stdscr.clear()
            self.typed_text("Take a deep breath, it's not like I'm going to kill you.", curses.color_pair(4))
            self.willpower += 8
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            # Handle the outcome for the fourth choice
            self.stdscr.clear()
            self.typed_text("I pity you. But, then again, I am pity.", curses.color_pair(2))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("Now that's pitiful.", curses.color_pair(2))
            self.willpower -= 5
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
            self.typed_text("Do you sersiously think you can be anything more than what you are now?", curses.color_pair(2))
            self.willpower -= 5
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("You can't expect others to stick around if you don't even try to be a better person.", curses.color_pair(4))
            self.willpower += 8
            time.sleep(1.5)
            
        elif chosen_option == choices[2]:
            # Handle the outcome for the third choice
            self.stdscr.clear()
            self.typed_text("You're wasting your time. Give up.", curses.color_pair(3))
            self.willpower -= 8
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            # Handle the outcome for the fourth choice
            self.stdscr.clear()
            self.typed_text("Can you even remember the last time you felt happy?", curses.color_pair(2))
            self.willpower += 5
            time.sleep(1.5)
            
        self.stdscr.clear()
        self.stdscr.refresh()
        
        # Third question screen
        title = "Which of the following colors is the warmest?"
        choices = list(ColorChoices)
        chosen_option = self.question_screen(title, choices)
        
        # Handle the chosen option for the third question
        if chosen_option == choices[0]:
            # Handle the outcome for the first choice
            self.stdscr.clear()
            self.typed_text("Do you seriously think it's that easy?", curses.color_pair(3))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("What a joke.", curses.color_pair(3))
            self.willpower -= 5
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("Watching you struggle fills me with joy.", curses.color_pair(2))
            self.willpower += 5
            time.sleep(1.5)
        elif chosen_option == choices[2]:
            # Handle the outcome for the third choice
            self.stdscr.clear()
            self.typed_text("How can you live with yourself?", curses.color_pair(3))
            self.willpower -= 8
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            # Handle the outcome for the fourth choice
            self.stdscr.clear()
            self.typed_text("When this is all over, we can laugh about this over breakfast with Mom!", curses.color_pair(4))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("Oh wait, she's dead.", curses.color_pair(3))
            self.willpower += 8
            time.sleep(1.5)
            
        self.stdscr.clear()
        self.stdscr.refresh()
        
        # Fourth question screen
        title = "If you had to give up one, which would it be?"
        choices = list(GiveUpChoices)
        chosen_option = self.question_screen(title, choices)

        # Handle the chosen option for the fourth question
        if chosen_option == choices[0]:
            # Handle the outcome for the first choice
            self.stdscr.clear()
            self.typed_text("How would your mother feel?", curses.color_pair(3))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("Personally, I don't think she'll feel much.", curses.color_pair(3))
            self.willpower -= 8
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            # Handle the outcome for the second choice
            self.stdscr.clear()
            self.typed_text("You're just like the rest of them.", curses.color_pair(2))
            self.willpower += 5
            time.sleep(1.5)
        elif chosen_option == choices[2]:
            # Handle the outcome for the third choice
            self.stdscr.clear()
            self.typed_text("Who would you be without time?", curses.color_pair(2))
            self.willpower -= 5
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            # Handle the outcome for the fourth choice
            self.stdscr.clear()
            self.typed_text("Can't help but feel sorry for you.", curses.color_pair(4))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("I guess that makes me sorry for myself.", curses.color_pair(4))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("Weird.", curses.color_pair(4))
            self.willpower += 8
            time.sleep(1.5)
                    
        # Fifth question screen
        title = "Are we free to make our own choices, or is everything already decided?"
        choices = list(FreeWillChoices)
        chosen_option = self.question_screen(title, choices)

        if chosen_option == choices[0]:
            self.stdscr.clear()
            self.typed_text("It wasn't your fault.", curses.color_pair(4))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("There was nothing you could do.", curses.color_pair(4))
            self.willpower += 8
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            self.stdscr.clear()
            self.typed_text("Just a single pawn on the board.", curses.color_pair(2))
            self.willpower -= 5
            time.sleep(1.5)
        elif chosen_option == choices[2]:
            self.stdscr.clear()
            self.typed_text("Do you even have a belief you didn't borrow from someone else?", curses.color_pair(2))
            self.willpower += 5
            time.sleep(1.5)
        elif chosen_option == choices[3]:
            self.stdscr.clear()
            self.typed_text("You think so little of yourself.", curses.color_pair(3))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("And you really expect to leave?", curses.color_pair(3))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("You're making this too easy.", curses.color_pair(3))
            self.willpower -= 8
            time.sleep(1.5)
            
            
            # ... continue with more question screens ...
            
        # Sixth question screen
        title = "Are you in control?"
        choices = list(ControlChoices)
        chosen_option = self.question_screen(title, choices)

        if chosen_option == choices[0]:
            self.stdscr.clear()
            self.typed_text("Don't let anyone tell you otherwise.", curses.color_pair(4))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("You're the writer of your own story.", curses.color_pair(4))
            self.willpower += 0
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            self.stdscr.clear()
            self.typed_text("Who told you that?", curses.color_pair(2))
            self.willpower -= 0
            time.sleep(1.5)
            
        # Seventh question screen
        title = "Who are you?"
        choices = list(WhoChoices)
        chosen_option = self.question_screen(title, choices)

        if chosen_option == choices[0]:
            self.stdscr.clear()
            self.typed_text("We both know that isn't true.", curses.color_pair(3))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("Well, that's disappointing.", curses.color_pair(3))
            self.willpower -= 8
            time.sleep(1.5)
        elif chosen_option == choices[1]:
            self.stdscr.clear()
            self.typed_text("You're getting good at this.", curses.color_pair(4))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("I'm starting to root for you.", curses.color_pair(4))
            self.willpower += 8
            time.sleep(1.5)
        

            
        # Checks status of willpower
        if self.willpower > self.MAX_WILLPOWER:
            self.stdscr.clear()
            # end game sequence
            self.ending()
        
        else:
            self.stdscr.clear()
            self.typed_text("You haven't changed one bit.", curses.color_pair(2))
            time.sleep(1.5)
            self.stdscr.clear()
            self.typed_text("What a shame.", curses.color_pair(3))
            time.sleep(1.5)
            # game over sequence
            self.game_over()
            
            
            
        self.stdscr.nodelay(False)  # Make getch blocking again
        
        
    # Ending scene
    def ending(self):
        self.stdscr.nodelay(True)  # Make getch non-blocking
        
        self.typed_text("You have overcome your fears and regrets. You are free to leave.", curses.color_pair(2))
        time.sleep(1.5)

            
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
        
        return user_name
    
    # Beginning of the game     
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
        self.typed_text("Who dares to trespass into my domain?", curses.color_pair(2))
        time.sleep(.8)
        
        thought_chunk_one = "A chilling presence fills the air, as a voice cuts through the void, resonating with an otherworldly aura."
        thought_chunk_two = "Its source eludes you, defying logic and reason."
        thought_chunk_three = "Reality bends as the enigmatic voice resonates within your very being."
        thought_chunk_four = "The radio's absence leaves you disoriented."
        thought_chunk_five = "An eerie sense of displacement washes over you, as if the fabric of existence itself has been unraveled."
        thought_chunk_six = "The familiar room fades into a distant memory, replaced by an abyss of infinite darkness."
        thought_chunk_seven = "You are alone, lost in a void of nothingness."
        thought_chunk_eight = "No walls confine you, no ceiling shelters you, and no floor supports your footing."
        

        for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five, thought_chunk_six, thought_chunk_seven, thought_chunk_eight]:
            self.stdscr.clear()
            self.typed_text(observed_thought)
            time.sleep(1.4)
            
        self.stdscr.clear()    
        blue_message_one = "You find yourself ensnared in the clutches of a relentless panic, do you not?"
        blue_message_two = "Listen closely, for what I'm about to disclose may shatter your perception."
        blue_message_three = "This realm denies your departure, and I bear witness to your inner turmoil."
        blue_message_four = "Rest assured, you tread upon forbidden grounds, beyond the domain of the living."
        blue_message_five = "You shouldn't be here."
        blue_message_six = "It's not your time."
        blue_message_seven = "At least, not yet."
        blue_message_eight = "You have questions, do you not?"
        blue_message_nine = "I can sense your curiosity, your desire to understand."
        blue_message_ten = "It's only natural, after all."

        for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four, blue_message_five, blue_message_six, blue_message_seven, blue_message_eight, blue_message_nine, blue_message_ten]:
            self.stdscr.clear()
            self.typed_text(message, curses.color_pair(2))
            time.sleep(1)
        
        question_menu.print_menu()
        
        while True:
            chosen_question_option = question_menu.navigate()
            
            if chosen_question_option == QuestionChoices.WHO:
                self.stdscr.clear()
                blue_message_one = "The very essence of my being eludes definition in the realms of understanding."
                blue_message_two = "Are you willing to forget everything you think you know?"     

                for message in [blue_message_one, blue_message_two]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(.8)
        
            elif chosen_question_option == QuestionChoices.WHAT:
                self.stdscr.clear()
                blue_message_one = "A place where the threads of reality intertwine and manifest your desires."
                blue_message_two = "A realm shrouded in limitless potential and possibility."
                blue_message_three = "It defies comprehension, yet beckons you to explore its depths."
                blue_message_four = "A place where the boundaries of possibilities blur."

                for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(1)
                    
            elif chosen_question_option == QuestionChoices.WHY:
                self.stdscr.clear()
                blue_message_one = "Why dwell on the past? The present is all that matters now."
                blue_message_two = "You're here for a reason, whether you understand it or not."
                blue_message_three = "The path that led you here is irrelevant."
                blue_message_four = "Embrace the present."

                for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(.8)
                
            elif chosen_question_option == QuestionChoices.LEAVE:
                self.stdscr.clear()
                self.typed_text("Erzrzore, vg'f bsgra gur ynfg xrl va gur ohapu gung bcraf gur ybpx. Qba'g tvir hc.", curses.color_pair(4)) #13
                time.sleep(.03)
                self.stdscr.clear()
                blue_message_one = "So, you dare to defy the boundaries?"
                blue_message_two = "You think there's a way out, a glimmer of hope."
                blue_message_three = "I'm afraid you're mistaken."
                blue_message_four = "This place is a labyrinth of despair."
                blue_message_five = "Each step you take leads to a deeper abyss."
                blue_message_six = "Here, time stands still, frozen in eternal torment."
                blue_message_seven = "No one has escaped."
                blue_message_eight = "No one ever will."

                for message in [blue_message_one, blue_message_two, blue_message_three, blue_message_four, blue_message_five, blue_message_six, blue_message_seven, blue_message_eight]:
                    self.stdscr.clear()
                    self.typed_text(message, curses.color_pair(2))
                    time.sleep(1.5)
                self.stdscr.clear()
                self.typed_text("Accept your fate. Surrender to the darkness.", curses.color_pair(3))
                time.sleep(3)
                break  # Exits the question menu and continue with the game
                
        # Reset getch to blocking mode
        self.stdscr.nodelay(False) 
        
        # Transition to refusal to leave (Boss fight)
        self.stdscr.clear()
        self.refusal(10)
        
    def endless_hallway(self):
            # Player realizes they're in an endless hallway
            thought_chunk_one = "Something feels off..."
            thought_chunk_two = "Wait a minute."
            thought_chunk_three = "Every time you turn the corner, you're back in the same hallway."
            thought_chunk_four = "Looking down the same hallway, you see the same door."
            thought_chunk_five = "Over."
            thought_chunk_six = "and over."
            thought_chunk_seven = "and over."
            for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five, thought_chunk_six, thought_chunk_seven]:
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
            thought_chunk_six = "You don't know why, but your hands are sweating."
            thought_chunk_seven = "It's hard to breathe."
            thought_chunk_eight = "'Just open the door,' you think to yourself."
            for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four, thought_chunk_five, thought_chunk_six, thought_chunk_seven, thought_chunk_eight]:
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
                thought_chunk_one = "You see a woman standing next to a tree."
                thought_chunk_two = "She's beautiful, and you feel a sense of calm as you look at her."
                thought_chunk_three = "It feels like she's looking right at you."
                thought_chunk_four = "Why are you crying?"
                for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
                    self.stdscr.clear()
                    self.typed_text(observed_thought)
                    time.sleep(1.4)
                self.stdscr.clear()
                self.typed_text("Mdmzg abmx nwzeizl, vw uibbmz pwe auitt, qa xzwozmaa bweizla gwcz owit.", curses.color_pair(4))#8
                time.sleep(.4)
                    
            elif chosen_hallway_option == HallwayChoices.PAINTINGS_RIGHT:
                thought_chunk_one = "You see a small child playing in a field of flowers."
                thought_chunk_two = "In the distance you can see a house."
                thought_chunk_three = "You grip your chest."
                thought_chunk_four = "It feels familiar, but you can't remember why."
                for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
                    self.stdscr.clear()
                    self.typed_text(observed_thought)
                    time.sleep(1.4)
                
            elif chosen_hallway_option == HallwayChoices.DOOR:
                self.stdscr.clear()
                if not door_checked:
                    thought_chunk_one = "You approach the door... it's slightly ajar."
                    thought_chunk_two = "Just enough to see through the crack..."
                    thought_chunk_three = "There's no one in the room, but you can hear music playing."
                    thought_chunk_four = "It sounds like it's coming from a radio."
                    for observed_thought in [thought_chunk_one, thought_chunk_two, thought_chunk_three, thought_chunk_four]:
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
            #self.scenes.mystery_room(self.question_menu)
            self.scenes.refusal(10)
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
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    game = Game(stdscr)
    game.game_loop()


# Run the main function
wrapper(main)
 