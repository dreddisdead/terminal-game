

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


### Checks if being run on non-Windows system (Git Bash) and clears terminal
def clear_screen():
    os.system('clear')

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
greeting = "You've got a long road ahead of you, traveler.\n" 

print_ascii_art(big_string)

type_text(greeting) 

time.sleep(2)

user_name = input('What is your name?\n>')

# image window 46x25
new_scene = """
-----------------------------------------------------------------------------------------------
                            .==:=*%@@@@@%#+--**:       +=-            -+    #-            
                           -+:*@@@@@@@@@@@@@%+:+*      .#=.           -+    #-            
                          :=+@@@@@@@@@@@@@%%@@@*:*.     -++           -+    #-            
                          +=@@@@@@@@@@@%+:-+:#@@%:%.     *+           -+    #-            
                         .=%@@@@@@@@@*-   %:  -%@*-+     *+           -+    #-            
                         --@@@@@@@#=     :#     =@:#     *+           -+   -#:            
                         =-@@@@#=.    -=*%=      .**     ++           -+:+*-              
                         --@#=.    -==. *.=+.     #+.    ++           -#*:                
                        .+=.    :==.   .*  .+=    #+.    ++         .*#:                  
                     :--.    :--:      *-    .=*-:#=.    ++       :**:                    
                    *=::::===.        .%       .+-*=.    =+     -#+.                      
                    :- .--:           +*------:::+%=.    =+   :#*:                        
                     ==:              #........:::*=.    =+ -##.                          
                  -+=:...            :+          -#=.    =*#+:                            
                  =*:.::--------+*---*.        :#@@=:  .+%*                               
                    +-          =*           :#@@@@=: =%@@=                               
                    -%#:        *=         -*++*#@@+#@@@@#=                               
                 .+%%%@@+       #.       -*-.:---=#%=@@@*+=                               
               :++=:  :+%%-     %      -*:     :*%=. @@%.==                               
             .*++:      .=%*.  .#    :*-     :*@+    @@= ==                               
             *%=           =#+.:*  -+-     -*#=      @*  ==                               
             #%:             -##+-*:     =#*-        @:  ==                                                           
-----------------------------------------------------------------------------------------------
        LOOKS    LIKE    WE    GOT    SOME    MAIL... I    WONDER    WHAT    IT    IS?
-----------------------------------------------------------------------------------------------
"""

transition_to_scene(new_scene)

#user_birthday = input('What is your date of birth (mm/dd):\n')

#print(f"You're a {f.zodiac_sign(user_birthday)}")
look_counter = 0
while True:
    action = input('(Look/Open/Sunrise)\n')

    if action == 'Look':
        # Look at mailbox
        if look_counter >= 3:
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
        type_text('There is a letter for you. You open it.')
        break  # Exit the loop after the "Open" action

    elif action == 'Sunrise':
        # Return to sunrise scene
        transition_to_scene(big_string)
        break  # Exit the loop after the "Sunrise" action

    else:
        type_text('Invalid action. Please try again.')








