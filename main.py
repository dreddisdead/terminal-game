### First portfolio project! (super exciting)
### This adventure terminal game is a little...different.
### Guess there's only one way to find out why.

import functions as f
import os, sys
import time
import keyboard 

def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        sys.stdout.flush()
        time.sleep(0.07)  # Adjust the delay time as needed
    print()  # Print a newline after the typed text

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art(ascii_art):
    print(ascii_art)

def transition_to_scene(scene_ascii_art):
    clear_screen()
    print_ascii_art(scene_ascii_art)
    time.sleep(2)  # Adjust the delay time as needed



### screen size is 96x46
big_string = """                                                                                        
-----------------------------------------------------------------------------------------------                                                                                          
                                           -                                              
                                           *:  :*                                         
                                          **:  -*+                                        
                                          **-  -*+                                        
                                :.   -:   =*-  =*=   :       :.                           
                                :+   -*:  -*=  =*:  :=     :+=                            
                   :=.         .**=  -**  .*=  +*.  +**   -**.         :-++               
              -*-   .+*+.   :   .**:  +*:  *+  +*  .**:  -*+.   :-   :+*+:                
               -**-   :+*-  -*=  .**  .*+  ++  *+  =*=  :*=   =*=  .=*+:   ::             
                .=**-   -*+. :*+. :*+  =*. -*  *- .*+  :*=  .++:  -*+:   -+-              
                   -**-   =*-  +*. -*- .*- .*  *: =*: :*-  :*=  :*+:  .-**=               
                 :.  :+*-  :++. -*: -*: -*  *..*. *- .*-  =+. .++:  :=*=:                 
                  ++:  .=*-  :+- .+- =*  +: +..* -+ .+: .+-  =+:  :++-.  .                
           -=:     :=*=.  -+-  -+. =- =+ .: :..- -  +: -+. :+: .-*=.  :++.                
            .=**+-    :++-  :+- .=- ::.=-=+*****++=-: =- .=: .=+:  :=*=-    :.            
               :-+*+-.   :+=: .=- .--+****************=.-: :=-. :=+-:  .:=+**=--          
                   .-=+=-.  -=-. :-*********************+.-. :==:  .-=**+-:.              
           .-.=*+=-.   .:=+=: .::+************************-.-..:-++=-:.    .--:-.         
             .:--=+***=-:.  :--.***************************-.==-.   .:-=+***+=:.          
       -:::...       ..:-===-. +****************************: :-====--::.         ...     
    :==++++++++**++++===---::.:*****************************+ .  ...::---===++*******+--. 
                     ....:::-:-****************************** ---:::::::.......           
----------------------------------------------------------------------------------------------- 
        WELCOME   TO   THE    GAME   ISN'T   THIS   SUNRISE   JUST   BEAUTIFUL!!!!        
-----------------------------------------------------------------------------------------------

"""
greeting = "You've got a long road ahead of you, traveler."

print_ascii_art(big_string)

type_text(greeting) 

time.sleep(2)

user_name = input('What is your name?\n>')
greeting_user = f'Hello, {user_name}'

print(greeting_user)

#user_birthday = input('What is your date of birth (mm/dd):\n')


#print(f"You're a {f.zodiac_sign(user_birthday)}")







