#Name: Pranav T (23)
#Class: 2L
#This story is adapted from an iPhone text-based adventure game apps named Horror in the Pacific, Madness at Hobbsgate and Horror in the Darkness, all by Karmic Shift Studios.
#Timed Input code borrowed from https://www.reddit.com/r/learnpython/comments/19a658/get_user_input_within_time_limit/
#Type print function code borrowed from https://stackoverflow.com/questions/20302331/typing-effect-in-python

import time
import datetime
import sys

def halp():     #helpline for Horror in the Pacific
    print('''
*** Please maximise this screen for the best playing experience ***

Helpline for Horror in the Pacific
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyze the keywords in the story carefully before deciding your next move.

Possible moves:
walk north
walk south
walk east
walk west
enter 
exit 
take
leave

* Hit enter after keying in your input *

Note: If you enter an invalid input, the system will automatically ask you to enter your move again...

For your convenience, all inputs ,execpt for the code to diffuse the bomb, are not case sensitive.

Also note: To refer to this page, simply key in "help" when asked to enter your move...

Advertisment: Upgrade to the Pro version of this game for just $9.99,to unlock all the chapters of the game...

- A text with a title is a waypoint (Example: Quiet Street is a waypoint)
                                              ------------
Very Important:
    Your compass direction remains the same until you reach a waypoint.
    (Example: if you walked west to reach a waypoint and the text says that there is a hallway in front of you, then you have to continue walking west to move forward into the hallway)
    
That's all from me,

Have fun playing!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    time.sleep(2)


def halp1():     #helpline for Madness at Hobbsgate
    print('''
*** Please maximise this screen for the best playing experience ***

Helpline for Madness at Hobbsgate
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyze the keywords in the story carefully before deciding your next move.

Possible moves:
walk north
walk south
walk east
walk west
walk up
walk down

* Hit enter after keying in your input *

Note: If you enter an invalid input, the system will automatically ask you to enter your move again...

For your convenience, all inputs ,execpt for the code to diffuse the bomb, are not case sensitive.

Also note: To refer to this page, simply key in "help" when asked to enter your move...

Advertisment: Upgrade to the Pro version of this game for just $9.99,to unlock all the chapters of the game...

- A text with a title is a waypoint (Example: Front Gate is a waypoint)
                                              ----------
Very Important:
    Your compass direction remains the same until you reach a waypoint.
    (Example: if you walked west to reach a waypoint and the text says that there is a hallway in front of you, then you have to continue walking west to move forward into the hallway)
    
That's all from me,

Have fun playing!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    time.sleep(2)


def halp2():     #helpline for Horror in the Darkness
    print('''
*** Please maximise this screen for the best playing experience ***

Helpline for Horror in the Darkness  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyze the keywords in the story carefully before deciding your next move.

Possible moves:
walk north
walk south
walk east
walk west
continue investigation 
read 

* Hit enter after keying in your input *

Note: If you enter an invalid input, the system will automatically ask you to enter your move again...

For your convenience, all inputs ,execpt for the code to diffuse the bomb, are not case sensitive.

Also note: To refer to this page, simply key in "help" when asked to enter your move...

Advertisment: Upgrade to the Pro version of this game for just $9.99,to unlock all the chapters of the game...

- A text with a title is a waypoint (Example: Airstrip is a waypoint)
                                              --------
Very Important:
    Your compass direction remains the same until you reach a waypoint.
    (Example: if you walked west to reach a waypoint and the text says that there is a hallway in front of you, then you have to continue walking west to move forward into the hallway)
    You will be given hints where necessary...
    
That's all from me,

Have fun playing!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    time.sleep(2)


#The astonishing art of asteriks...
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def horror_in_the_pacific_art():   
    print('''
***********************************************************************************************************************************************************************************
*                                                                                                                                                                                 *
*   *    *  *****  *****  *****  *****  *****      *********  **     *      *********  *    *  ******      *****        *         ******  *********  ******  *********   ******   *
*   *    *  *   *  *   *  *   *  *   *  *   *          *      * *    *          *      *    *  *           *   *       * *       *           *      *            *      *         *
*   *    *  *   *  *   *  *   *  *   *  *   *          *      *  *   *          *      *    *  *           *   *      *   *      *           *      *            *      *         *
*   ******  *   *  *****  *****  *   *  *****          *      *   *  *          *      ******  ******      *****     *******     *           *      ******       *      *         *
*   *    *  *   *  * *    * *    *   *  * *            *      *    * *          *      *    *  *           *        *       *    *           *      *            *      *         *
*   *    *  *   *  *  *   *  *   *   *  *  *           *      *     **          *      *    *  *           *       *         *   *           *      *            *      *         *
*   *    *  *****  *   *  *   *  *****  *   *      *********  *      *          *      *    *  ******      *      *           *   ******  ********* *        *********   ******   *
*                                                                                                                                                                                 *
***********************************************************************************************************************************************************************************

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')


def horror_in_the_darkness_art():
    print('''
***********************************************************************************************************************************************************************************
*                                                                                                                                                                                 *
*   *    *  *****  *****  *****  *****  *****      *********  **     *      *********  *    *  ******      ****          *        *****  *    *  **     *  ******   ****   ****   *  
*   *    *  *   *  *   *  *   *  *   *  *   *          *      * *    *          *      *    *  *           *    *       * *       *   *  *   *   * *    *  *       *      *       *
*   *    *  *   *  *   *  *   *  *   *  *   *          *      *  *   *          *      *    *  *           *    *      *   *      *   *  *  *    *  *   *  *       *      *       *
*   ******  *   *  *****  *****  *   *  *****          *      *   *  *          *      ******  ******      *    *     *******     *****  * *     *   *  *  ******   ***    ***    *
*   *    *  *   *  * *    * *    *   *  * *            *      *    * *          *      *    *  *           *    *    *       *    * *    *  *    *    * *  *           *      *   *
*   *    *  *   *  *  *   *  *   *   *  *  *           *      *     **          *      *    *  *           *    *   *         *   *  *   *   *   *     **  *           *      *   *
*   *    *  *****  *   *  *   *  *****  *   *      *********  *      *          *      *    *  ******      ****    *           *  *   *  *    *  *      *  ******  ****   ****    *
*                                                                                                                                                                                 *
***********************************************************************************************************************************************************************************

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')


def madness_at_hobbsgate_art():
    print('''
**************************************************************************************************************************************************************************************
*                                                                                                                                                                                    *
*   **           **        *        ****    **     *  ******   ****   ****            *     *********      *    *  *****  ****   ****    ****   ****        *    *********  ******   *
*   * *         * *       * *       *    *  * *    *  *       *      *               * *        *          *    *  *   *  *   *  *   *  *      *           * *       *      *        *
*   *  *       *  *      *   *      *    *  *  *   *  *       *      *              *   *       *          *    *  *   *  *   *  *   *  *      *          *   *      *      *        *
*   *   *     *   *     *******     *    *  *   *  *  ******   ***    ***          *******      *          ******  *   *  *****  *****   ***   *  **     *******     *      ******   *
*   *    *   *    *    *       *    *    *  *    * *  *           *      *        *       *     *          *    *  *   *  *   *  *   *      *  *   *    *       *    *      *        *
*   *     * *     *   *         *   *    *  *     **  *           *      *       *         *    *          *    *  *   *  *   *  *   *      *  *   *   *         *   *      *        *
*   *      *      *  *           *  ****    *      *  ******  ****   ****       *           *   *          *    *  *****  ****   ****   ****    ***   *           *  *      ******   *
*                                                                                                                                                                                    *
**************************************************************************************************************************************************************************************

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')

    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Day of week code
def find_day(date,month,year):          #day of the week code to determine the player's day of birth
    leap_year = False
    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:  
            if (int(year) % 400) == 0:  
                leap_year = True  
            else:
             leap_year = False
        else:  
          leap_year = True  
    else:  
        leap_year = False  

    century_digits = str(year)[0:2]
    year_digits = str(year)[-2:]

    value = int(year_digits) + (int(year_digits)//4)

    if int(century_digits) == 18:
        value+=2
    elif int(century_digits) == 20:
        value+=6

    if month == '1' and leap_year == False:
        value+=1
    elif month == '2' and leap_year == True:
        value+=3
    elif month == '2' and leap_year == False:
        value+=4
    elif month == '3' or month == '11':
        value+=4
    elif month == '5':
        value+=2
    elif month == '6':
        value+=5
    elif month == '8':
        value+=3
    elif month == '10':
        value+=1
    elif month == '9' or month == '12':
        value+=6

    result = (value+int(date))%7

    if result == 1:
        return 'Sunday'
    elif result == 2:
        return 'Monday'
    elif result == 3:
        return 'Tuesday'
    elif result == 4:
        return 'Wednesday'
    elif result == 5:
        return 'Thursday'
    elif result == 6:
        return 'Friday'
    elif result == 0:
        return 'Saturday'


#Setting the parameters
def type_print(str):            #this function prints out the letters in the statement one my one, making it seem like it is being typed
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print
    
def ask_to_continue():  #ask to continue
    continue_yes_no = ''
    continue_y_n = True
    while continue_yes_no != 'y' and continue_yes_no != 'n' and continue_yes_no != 'yes' and continue_yes_no != 'no':    #input validation
        continue_yes_no = input('Do you still wish to continue? (y/n): ')
        continue_yes_no = continue_yes_no.lower()   #converting input to lowercase
    else:
        if continue_yes_no == 'y' or continue_yes_no == 'yes':
            continue_y_n = True         #assigning boolean flags to inputs
        elif continue_yes_no == 'n' or continue_yes_no == 'no':
            continue_y_n = False
    return continue_y_n

def reject_input():     #this is displayed when the user's input is rejected    
    print('''You can't walk in that direction.
''')
    time.sleep(2)

    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Directory - Horror in the Pacific
def introduction():   #Introduction story
    halp()
    time.sleep(15)
    horror_in_the_pacific_art()
    time.sleep(3)
    print('''                                            
Introduction
------------
It was a rainy winter’s day when I got the letter. 
I’d arrived at my office at noon which was typical these days. 
My secretary has managed to find a space on my desk amongst the empty liquor bottles and past due bills for the daily mail. 
Most of it was more bills and junk mail but one envelope caught my eye.
Handwritten and addressed to me, it was from someone in Providence, Rhode Island. 
They had heard about that business with Lacy Wentsire a few years ago and were asking for my help. 
It was another missing person case. 
I remembered reading in the newspaper, some tourists had disappeared from a resort on Malaki Island near Papua New Guinea. 
Something felt off about it, like an itch at the back of my neck that I couldn’t scratch. 
But another glance at the past due notices followed by a glance at the rain outside the window settled it. 
I’d better pack my suitcase, I thought.
''')
    
def airstrip():         #I've used functions to store the entire storyline to make the main code easier to understand and also easier to troubleshoot...
    print('''
Airstrip
--------
The airstrip is short and caters to small aircraft flying groups of tourists to and from the resort.
The occasional crack in the tarmac gives enough space for small weeds and grass to push through.
The humid air is tainted with the smell of petrol.
To the north, at the end of a wide paved path, I can make out the resort in the distance...
                    ----- progress saved -----
''')                                                                                                        #main story text
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':    #input validation    
        what_to_do = input('What would you like to do?: ')
        what_to_do = what_to_do.lower() #converting the input to lowercase                                                   
    if what_to_do == 'walk north':          #if the player wants to walk south:
        paved_path()                            #he is brought to paved path
    elif what_to_do == 'walk south':        #if the player wants to walk south:
        swamp_trail()                           #he is brought to swamp trail
    elif what_to_do == 'walk east':         #if the player wants to walk east:
        print('''The gate has been locked with what seems like a fairly new lock.
''')
        airstrip()                              #he is sent back to the airstrip because the gate is locked
    elif what_to_do == 'help':              #if the player enters help:
        halp()                                  #the helpline is displayed 
        airstrip()                              #he is sent back to the airstrip to enter another move
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter' or what_to_do == 'exit':    #if the player enters take, leave, enter or exit:
        print('There is nothing to '+what_to_do+''' here.                                                          
''')
        time.sleep(2)                                                                                           #he is told that there is nothing such to do here
        airstrip()                                                                                              #and he is sent back to the airstrip to enter another move
    else:                                   #if the player enters a wrong move which is not enter, exit, take or leave:
        reject_input()                          #he is told that the move does not work here
        airstrip()                              #and he is sent back to the airstrip to enter another move
        
                                    #********** This explanation is similar for all the directories and paths...**********
def paved_path():
    print('''
Paved Path
----------
A neatly paved path leads from the airstrip towards the resort on the north coast of the island.
On the eastern side of the path is a small prefabricated building which seems to be the offices of the airline that operate on this island.
                    ----- progress saved -----
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':    #input validation    
        what_to_do = input('What would you like to do?: ')     #input validation 
        what_to_do = what_to_do.lower()       #converting the input to lowercase
    if what_to_do == 'walk east':
        enter_airline_office()
    elif what_to_do == 'walk south':
        airstrip()
    elif what_to_do == 'walk north':
        resort_entrance()
    elif what_to_do == 'help':
        halp()
        paved_path()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter' or what_to_do == 'exit':        
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        paved_path()
    else:
        reject_input()
        paved_path()
    
def enter_airline_office():
    type_print('''
You arrive at the doorstep of the small, prefabricated building...

''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help': #input validation   
        what_to_do = input('What would you like to do?: ')  
        what_to_do = what_to_do.lower()
    if what_to_do == 'enter':       
        airline_office()
    elif what_to_do == 'walk west':
        paved_path()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'exit':     
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        enter_airline_office()
    elif what_to_do == 'help':
        halp()
        enter_airline_office()
    else:
        reject_input()
        enter_airline_office()
        
def airline_office():
    type_print('''
You enter the building...
''')
    time.sleep(2)
    print('''
Airline Office
--------------
The inside of the airline office tries unsuccessfully to portray an image of enthusiasm in what is a fairly grim environment.
Cliche motivational and landscape posters are plastered onto the cracking walls.
A single counter stands at one end of the building for customer service.
The rest of the building is full of empty waiting chairs.
                        ----- progress saved -----
''')
    time.sleep(5)
    type_print('''You wait for an hour yet, nobody comes to your service...

You should leave the building now...
                    
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':  #input validation      
        what_to_do = input('What would you like to do?: ')  
        what_to_do = what_to_do.lower()
    if what_to_do == 'exit':   
        type_print('''
You leave the building...
''')
        time.sleep(3)
        death_by_assult()       
        time.sleep(5)
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter':     
        print('''You can't do that here.
''')
        time.sleep(2)
        airline_office()
    elif what_to_do == 'help':
        halp()
        airline_office()           
    else:
        reject_input()
        airline_office()

def death_by_assult():      #player dies
    print('''
Death by Assault
---------------
As you leave the building, you are surrounded by a group of 5 gangsters.
You remember them to be the loansharks you borrowed money from, last month, but have been unable to pay back the loan.
They threaten to beat you up if you don't pay up the money.
You explain that you have no money with you right now.
They get furious and begin throwing a barrage of punches on you.
You can't help but crouch down in pain.
You are unable to move and are left bleeding on the ground...

''')

def resort_entrance():
    print('''
Resort Entrance
---------------
A well paved path from the airstrip in the south finally reaches the entrance of the resort.
Bright and friendly signs welcoming guests are fitted across the path with palm trees and decorative shrubs framing the elegant building, which could probably cater for a hundred guests at full capacity
At the moment, it feels empty.
The main lobby lies to the north past several large doors.
A small side path leads away from the main building and off to the west...
                    ----- progress saved -----
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation      
        what_to_do = input('What would you like to do?: ')     
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        lobby()
    elif what_to_do == 'walk south':
        paved_path()
    elif what_to_do == 'walk west':
        shed()
    elif what_to_do == 'help':
        halp()
        resort_entrance()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter' or what_to_do == 'exit':        
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        resort_entrance()
    else:
        reject_input()
        resort_entrance()

def lobby():        
    print('''
Lobby
-----
The lobby looks fairly deserted. A reception desk is located against the west wall.
Further to the north are large doors which open out onto a magnificent beachfront.
A sign indicates that the restaurant and bar are through the doors to the east.
There is a door behind the reception desk with a sign that reads, "staff only".
                    ----- progress saved -----
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation      
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        print('''The doors to the beach have been locked.
''')
        time.sleep(2)
        lobby()
    elif what_to_do == 'walk west':
        print('''I can't, the manager is back there!
''')
        time.sleep(2)
        lobby()
    elif what_to_do == 'walk east':
        restaurant()
    elif what_to_do == 'walk south':
        resort_entrance()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter' or what_to_do == 'exit':        
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        lobby()
    elif what_to_do == 'help':
        halp()
        lobby()           
    else:
        reject_input()
        lobby()

def restaurant():
    print('''
Restaurant
----------
The restaurant area is completely deserted.
No tourists are dining here and it seems that because of this, the staff felt it unnecessary to be here either.
To the east end of the room is a bar.
To the north is the kitchen area, separated from the restaurant by a hole in the wall for passing food ready for service and a small door.
                    ----- progress saved -----
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation      
        what_to_do = input('What would you like to do?: ')     
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        print('''The door to the kitchen is locked.
''')
        time.sleep(2)
        restaurant()
    elif what_to_do == 'walk west':
        lobby()
    elif what_to_do == 'walk east':
        bar()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter' or what_to_do == 'exit':        
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        restaurant()
    elif what_to_do == 'help':
        halp()
        restaurant()           
    else:
        reject_input()
        restaurant()

def bar():
    print('''
Bar
---
The bar is dimly lit and quiet, but not completely empty.

A tourist wearing a bright tropical shirt and a wide brimmed hat is sitting at the bar, staring into a drink and looking sorry for himself.
Hanging around the tourist's neck is a small camera.

Almost suddenly, the bartender calls out to me and tells me that someone had left a package for me.

Something seems really off...
                    ----- progress saved -----
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation      
        what_to_do = input('What would you like to do with the package?: ')     
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk west':
        restaurant()
    elif what_to_do == 'take':
        bomb_blast()
    elif what_to_do == 'leave':
        type_print('''
You did a good thing by leaving the parcel alone...
Upon further investigation by the police department, it is determined that the parcel contained a bomb which would have detonated upon touching it...
''')
        time.sleep(3)
        print('''
Good Job! You have survived Chapter 1.
''')
        time.sleep(2)       #end of preview
        print('''Subscribe to the pro version for just $9.99 to unlock the next chapter...
''')
    elif what_to_do == 'enter' or what_to_do == 'exit':     
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        bar()
    elif what_to_do == 'help':
        halp()
        bar()
    else:
        reject_input()
        bar()

def bomb_blast():
    type_print('''
You open up the parcel and see a bomb.
Oh my lord, and what could be worse?
There is a timer on it.
60 seconds is all you have...
''')
    time.sleep(1)
    type_print('''
Oh wait, it comes with a note too...
It reads,"Xfmm!epof!dijfg"!Zpv!uvsofe!pvu!up!cf!tnbsufs!uibo!j!uipvhiu///"

''')
    time.sleep(2)
    print('''Oh my lord how am I suppossed to understand this gibberish?
''')
    time.sleep(2)
    print('''Or could it be....
Some kind of a cipher?
''')
    time.sleep(2)
    print('''like a caesar cipher...
''')
    time.sleep(2)
    print('''let me dig my backpack to see if I can find anything...
''')
    time.sleep(5)
    type_print('''
I've found these notes from my CEP lesson...
Mate, I have no idea how this sophisticated code works...
You have to decode this in 50 seconds or the bomb will detonate...
Google it, make a code, do whatever you want but you must decrypt this code!

Here you go, take my lesson notes,

def decrypt(text):
    decrypted_text = []
    for i in range(1, 27):
        output = ''
        for char in text:
            output+=(chr(ord(char)-i))
        decrypted_text.append(output)
    for x in decrypted_text:
        print(x)
        print('')

According to my CEP teacher, the only readable output out of all the other outputs, is the right one...
''')
    out_of_time = False             #timed input code
    start = time.time()
    user_input = ''
    while user_input == '' and out_of_time == False:        
        user_input = input("Enter the decoded code: ")
    if user_input == 'Well done chief! You turned out to be smarter than I thought...':  
        print('''The bomb beeps and deactivates...''')
    else:
        print('''You enter the wrong code yet, the bomb only beeps. Seems like the bomb was just a hoax. You heave a sigh of relief!''')
    now = time.time()
    if now - start <= 50:
        print('You took '+str(now - start)+' seconds')
        out_of_time = False
    else:
        print('''but that could only be a dream because you have run out of time''')            #player dies
        out_of_time = True
        print('You took '+str(now - start)+' seconds')
        print('the bomb denotates...')
        time.sleep(3)
        print('I would have continued my journey but only if I was able to live the journey...')
        
def shed():
    print('''
Maintenance Shed
----------------
The small metal maintenence shed contains a workbench with a variety of attached tools and implements.
It looks tidy and well-organised.
A small door to the west sits ajar and through which wafts a disgusting smell...
                    ----- progress saved -----
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'enter' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk west':
        enter_dumpster()
    elif what_to_do == 'walk east':
        resort_entrance()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter':        
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        shed()
    elif what_to_do == 'exit':
        resort_entrance()
    elif what_to_do == 'help':
        halp()
        shed()           
    else:
        reject_input()
        shed()

def enter_dumpster():
    type_print('''
You arrive at the doorstep of the small room...

''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'enter' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'enter':
        toxic_dumpster()
        time.sleep(5)
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'exit':     
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        enter_dumpster()
    elif what_to_do == 'exit':
        shed()
    elif what_to_do == 'help':
        halp()
        enter_dumpster
    else:
        reject_input()
        enter_dumpster()
    
def toxic_dumpster():       #player dies
    print('''
Toxic Dumpster
--------------
Behind the maintenence shed is a large dumpster.
Dead bodies are strewn everywhere.
The door behind you suddenly slams shut.
Everything feels so suspicious...
To your right you notice a sign which reads,"welcome to the death chamber".
You soon realise that you are in a state of turmoil.
You inhale the deadly gas and your body starts to feel weak.
You try to unlock the door behind you but it is to no avail.
Your life slowly and painfully seeps out of your body.
In a matter of seconds, you succumb to the deadly gas...

''')

def swamp_trail():
    print('''
Swamp Trail
-----------
The trail leads away from the airstrip in the north and towards the swamp further down south.
The vegetation grows thicker and more dense and the track becomes harder and harder to follow.
It becomes clear that directions will be needed to travel further south and navigate the swamp safely.

Resting on a branch immediately above the south trail is a panther.
It turns its head to look at me as I grow closer.
                    ----- progress saved -----

''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'enter' and what_to_do != 'take' and  what_to_do != 'leave' and what_to_do != 'exit' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk south':
        death_by_panther()
        time.sleep(5)
    elif what_to_do == 'walk north':
        airstrip()
    elif what_to_do == 'take' or what_to_do == 'leave' or what_to_do == 'enter' or what_to_do == 'exit':        
        print('There is nothing to '+what_to_do+''' here.
''')
        time.sleep(2)
        swamp_trail()
    elif what_to_do == 'help':
        halp()
        swamp_trail()
    else:
        reject_input()
        swamp_trail()

def death_by_panther():         #player dies
    print('''
Death by Panther
----------------
Panthers are just large cats and I'm not afraid of cats, I think to myself strolling forward down the trail.
The panther stands and tenses its muscles at which point I realise that no household cat I've ever seen has muscles that big.
The panther then pounces and I note that no household cat weighs 150 pounds, which is the weight of an angry clawing biting panther that hits me square in the chest.
The fight was not a long one and I didn't win it...

''')
        
#End of Horror in the Pacific
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Directory - Madness at Hobbsgate
def prologue():
    halp1()
    time.sleep(10)
    madness_at_hobbsgate_art()
    time.sleep(3)
    print('''
Prologue
---------
Lacy stood on the gloomy street, the infrequent street lights no match for the rapidly fading daylight that left her eyes darting from shadow to growing shadow.
Months of searching had brought her to this place, standing in the shadow of the imposing Hobbsgate Asylum for the Criminally Insane.
Would he even recognise her, she thought to herself when she considered the task at hand.
It had cost her dearly, but she had managed to secure a brief visitation.
Inhaling deeply, she took her first step forward, hoping that this wasn't all in vain.
''')

def quiet_street():
    print('''
Quiet Street
------------
The street leading to the front gate of the asylum was quiet, with a faint trace of fog clinging to the road still sightly wet from the rain earlier in the day.
To the north loomed the imposing silhouette of the asylum building, framed by the rapidly setting sun.
The faint crash of waves against the stony shoreline below the asylum filled in the oppressive silence yet, somehow made the scene even more forebonding.
                                                  ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk up' and  what_to_do != 'walk down' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')   #input validation   
        what_to_do = what_to_do.lower()        #converting the input to lowercase
    if what_to_do == 'walk north':
        gate()
    elif what_to_do == 'walk up':
        print('''I can't fly buddy.
''')
        time.sleep(2)
        quiet_street()
    elif what_to_do == 'help':
        halp1()
        quiet_street()           
    else:
        reject_input()
        quiet_street()

def gate():
    print('''
Gate
----
A large gothic wrought iron gate acted as a barrier to keeping the inmates inside.
It was never really intended to keep people out, although it would have done a good job on that as well.

The guard that Lacy had bribed to get into the asylum was standing at the gate, as promised.
A statue was vaguely visible further down south.
                            ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk up' and  what_to_do != 'walk down' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        statue()
    elif what_to_do == 'walk up':
        print('''I can't fly buddy.
''')
        time.sleep(2)
        gate()
    elif what_to_do == 'walk south':
        quiet_street()
    elif what_to_do == 'help':
        halp1()
        gate()           
    else:
        reject_input()
        gate()

def statue():
    print('''
Statue
------
The driveway from the road formed a loop here, offering a place for vehicles to turn around.
In the middle of the loop was a grassy area with a statue in the middle.
The statue itself was of a woman standing on a pedestal staring towards the south.
Up towards the north was the foyer.

The guard guides Lacy up the driveway and past the statue.
            ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk up' and  what_to_do != 'walk down' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        foyer()
    elif what_to_do == 'walk up':
        print('''I can't fly buddy.
''')
        time.sleep(2)
        statue()
    elif what_to_do == 'walk south':
        print('''"There is no going back now."
''')
        time.sleep(2)
        statue()
    elif what_to_do == 'help':
        halp1()
        statue()           
    else:
        reject_input()
        statue()

def foyer():
    print('''
Foyer
-----
The foyer of the asylum was a large open space with a wide winding staircase leading up to the inmate wards.

The guard ushered her through the front doors of the asylum and past the security checkpoint.
At one point, it seemed as though one of the guards on duty would protest but he stopped himself and reconsidered.
                                ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk up' and  what_to_do != 'walk down' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk up':
        atrium()
    elif what_to_do == 'walk south':
        print('''The guard indicated that Lacy needed to climb the staircase.
''')
        time.sleep(2)
        foyer()
    elif what_to_do == 'help':
        halp1()
        foyer()           
    else:
        reject_input()
        foyer()

def atrium():
    print('''
Atrium
------
The first-floor of the atrium provided a view of the lower foyer area which at that time, was relatively empty of staff.
To the east were the wards.

The guard nervously followed Lacy up the stairs.
            ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk up' and  what_to_do != 'walk down' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk east':
        waiting_room()
    elif what_to_do == 'walk down':
        print('''She was so close to her goal that it would have been folly to turn back.
''')
        time.sleep(2)
        atrium()
    elif what_to_do == 'help':
        halp1()
        atrium()           
    else:
        reject_input()
        atrium()

def waiting_room():
    print('''
Waiting Room
------------
The waiting room had several uncomfortable benches for patients awaiting treatment.
To the south was a door with the word "visitation" stencilled on it.
The hallway continued to the east, to the main wards.

The guard looked slightly relieved to have finally reached the visitation room entrance         
            ------- progress saved -------
''')                                                                                            
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk up' and  what_to_do != 'walk down' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help':     #input validation   
        what_to_do = input('What would you like to do?: ')      
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk west':
        print('''She considered going back but realised that she was only a few steps away from her goal.
''')
        time.sleep(2)
        waiting_room()
    elif what_to_do == 'walk east':
        print('''The guard wouldn't let Lacy just wander around the wards.
''')
        time.sleep(2)
        waiting_room()
    elif what_to_do == 'walk south':
        locked_up_and_lost_forever()
    elif what_to_do == 'help':
        halp1()
        waiting_room()           
    else:
        reject_input()
        waiting_room()

def locked_up_and_lost_forever():
    print('''
Chapter 1: Locked Up and Lost 
------------------------------
"Get up."

The words echo through my pounding head.
Groggy and confused, I force my eyes open to see an elderly woman in a white nurses' uniform, standing over me.
Her contorted expression is a mixture of disgust and contempt.

In a haze and with much effort, I lurch up and off the mattress that I was lying on, and take the moment to glance around the room.
It appeares to be some form of a small padded cell.
At the door to the cell is the woman flanked by a rather large orderly.
Neither of them look like particularly pleasant people.

The woman is looking at me with expectation.

"I'd better see what she wants," I think to myself...
''')
    time.sleep(10)
    print('''
You have come to the end of this preview...
Subscribe to the pro version for just $9.99, to unlock the rest of the chapters...''')      #end of preview
#End of Madness at Hobbsgate
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Directory - Horror in the Darkness 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def prelude():
    halp2()
    time.sleep(15)
    horror_in_the_darkness_art()
    time.sleep(3)
    print('''
Prelude
-------
It was a cold New England morning when I received the letter.
It was from Annabelle Jackson, Tommy's widow.
I served with Tommy during the war and he was one heck of a guy, by the end, I even considered him a friend.
Tommy had written home about me before he died, and now, his widow, Annabelle needed my help.
She had family living at a place called Wentsire Manor, located on a small island off the coast of Brunswick, Maine.
The used to be frequent contact but over the past few months, their letters had become unusual and infrequent and lately, stopped completely.

Something about it seemed off, but the letter included a cheque to cover the bill, and I didn't have any other work at that time.
My ex-wife had been complaining about alimony for weeks, so it wasn't the time to be turning up my nose at paid work.

I slipped my coat and turned up the collar to the cold.
A few hours and a short boat ride out there to make sure everything is fine, then back home by supper.

Or so I thought.
''')


def front_gate():
    print('''
Front Gate
----------
I stand before a decorative wrought iron gate set into a large fence in the east.
The fence is topped with uninviting sharp ironwork.
The street proceeds to the south, and to the north is an ornamental letter box.
               ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')      #input validation
        what_to_do = what_to_do.lower()     #converting the input to lowercase
    if what_to_do == 'walk north':
        letter_box()
    elif what_to_do == 'walk east':
        print('''The gate blocks the way.
''')
        front_gate()
    elif what_to_do == 'walk south':
        an_empty_street()
    elif what_to_do == 'continue investigation':
        print('''I'm afraid there's nothing to investigate here.
''')
        time.sleep(2)
        front_gate()
    elif what_to_do == 'read':
        print('''The signboard beside the front gate reads, "Wentsire Manor".
''')
        time.sleep(2)
        front_gate()
    elif what_to_do == 'help':
        halp2()
        front_gate()           
    else:
        reject_input()
        front_gate()

def letter_box():
    print('''
Letter Box
----------
Here is an ornamental letter box.
Judging by the bulging circulars and flyers, it hasn't been checked in quite some time.
To the south is the main front gate to the estate.
There is no point going in any other direction.
       ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk south':
        front_gate()
    elif what_to_do == 'continue investigation':
        print('''I'm afraid there's nothing to investigate here.
''')
        time.sleep(2)
        letter_box()
    elif what_to_do == 'read':
        print('''No, it would be morally wrong for me to read the letters inside the letter box.
''')
        time.sleep(2)
        letter_box()
    elif what_to_do == 'help':
        halp2()
        letter_box()           
    else:
        reject_input()
        letter_box()

def an_empty_street():
    print('''
An Empty Street
---------------
This is an empty street, much like all the other empty streets I have seen before.
A street light flickers above and casts off an eerie light.
To the north is the main front gate to the estate.
To the west is a small tidy house with a well-maintained front yard.
There are no lights on the inside of the house.

Lying in the gutter is a newspaper.
        ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk west':
        quiet_path()
    elif what_to_do == 'walk north':
        front_gate()
    elif what_to_do == 'continue investigation':
        print('''I'm afraid there's nothing to investigate here.
''')
        time.sleep(2)
        an_empty_street()
    elif what_to_do == 'read':
        print('''I'm afraid there's nothing to read here.
''')
        time.sleep(2)
        an_empty_street()
    elif what_to_do == 'help':
        halp2()
        an_empty_street()           
    else:
        reject_input()
        an_empty_street()

def quiet_path():
    print('''
Quiet Path
----------
A small quiet path leads from the street up to the front door.
At first, I think that nobody is at home because there are no lights on, but then I notice that the front door is ajar.
                                        ------- progress saved -------
                                        
Hint: You are walking west so to walk forward to the front door, you need to continue walking west...
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk west':
        hallway()
    elif what_to_do == 'walk east':
        an_empty_street()
    elif what_to_do == 'continue investigation':
        print('''I'm afraid there's nothing to investigate here.
''')
        time.sleep(2)
        quiet_path()
    elif what_to_do == 'read':
        print('''I'm afraid there's nothing to read here.
''')
        time.sleep(2)
        quiet_path()
    elif what_to_do == 'help':
        halp2()
        quiet_path()           
    else:
        reject_input()
        quiet_path()

def hallway():
    print('''
Hallway
-------
The hallway shows signs of struggle.
Family pictures have been pulled off the wall and smashed onto the ground.
At one point, it looks like someone has punched a hole in the wall.
            ------- progress saved -------
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        messy_lounge()
    elif what_to_do == 'walk south':
        bedroom()
    elif what_to_do == 'walk east':
        quiet_path()
    elif what_to_do == 'walk west':
        dining_room()
    elif what_to_do == 'continue investigation':
        print('''Not yet, keep moving.
''')
        time.sleep(2)
        hallway()
    elif what_to_do == 'read':
        print('''The text on one of the picture reads, "Hawaii,2017".
''')
        time.sleep(2)
        hallway()
    elif what_to_do == 'help':
        halp2()
        hallway()           
    else:
        reject_input()
        hallway()

def messy_lounge():
    print('''
Messy Lounge
------------
The small lounge has seen better days.
The television has been smashed onto the floor with other broken furniture scattered around.
There is a large pool of what seems like blood, near the door out to the garage.

A small leather-bound journal is half concealed by the television.
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk east':
        print('''The door to the garage is locked.
''')
        messy_lounge()
    elif what_to_do == 'walk south':
        hallway()
    elif what_to_do == 'continue investigation':
        type_print('''
You have come to the end of your free trial preview.
Subscribe to the pro version for just $9.99 to continue your investigation.
''')
    elif what_to_do == 'read':
        print('''I'm afraid there's nothing to read here.
''')
        time.sleep(2)
        messy_lounge()
    elif what_to_do == 'help':
        halp2()
        messy_lounge()           
    else:
        type_print('''
You have come to the end of your free trial preview.
Subscribe to the pro version for just $9.99 to continue your investigation.
''') 

def bedroom():
    print('''
Bedroom
-------
The bedroom looks like it was sacked by burglars.
Furniture has been thrown about and clothing lies strewn across the floor.

The only evidence that this wasn't a burglary is that a small gold watch is lying on the floor in plain sight.
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk north':
        hallway()
    elif what_to_do == 'continue investigation':
        type_print('''
You have come to the end of your free trial preview.
Subscribe to the pro version for just $9.99 to continue your investigation.
''')
    elif what_to_do == 'read':
        print('''I'm afraid there's nothing to read here.
''')
        time.sleep(2)
        bedroom()
    elif what_to_do == 'help':
        halp2()
        bedroom()           
    else:
        type_print('''
You have come to the end of your free trial preview.
Subscribe to the pro version for just $9.99 to continue your investigation.
''')

def dining_room():
    print('''
Dining Room
-----------
The dining room seems to be in good order.
Any conflict must have happened in the other parts of the house.
A simple but cosy dining table sits in the centre of the room, surrounded by four chairs.

On the dining table is a small note, carefully folded and weighed down by a flower vase.
''')
    what_to_do = ''
    while what_to_do != 'walk north' and what_to_do != 'walk south' and what_to_do != 'walk east' and what_to_do != 'walk west' and what_to_do != 'help' and what_to_do != 'continue investigation' and what_to_do != 'read':     #input validation   
        what_to_do = input('What would you like to do?: ')       
        what_to_do = what_to_do.lower()
    if what_to_do == 'walk east':
        hallway()
    elif what_to_do == 'read':
        time.sleep(1)
        type_print('''
The note read,

"To whoever finds this,

Something terrible has happened to my husband, James.
He spends more time at Wentsire, Manor.
Ever since he started that job there, it's been like he is a different person.

I'm going over there to make one last try to talk him into coming home and seeking help.
I'm leaving this note because I'm afraid something unnatural is happening at that place.

God help us all.

Mary."
''')
        time.sleep(5)
        dining_room()
    elif what_to_do == 'continue investigation':
        type_print('''
You have come to the end of your free trial preview.
Subscribe to the pro version for just $9.99 to continue your investigation.
''') 
    elif what_to_do == 'help':
        halp2()
        dining_room()           
    else:                                                           #end of preview
        type_print('''
You have come to the end of your free trial preview.
Subscribe to the pro version for just $9.99 to continue your investigation.
''')
#End of Horror in the Darkness
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Main Code
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Beginning Formalities
print('''***** Please maximise your screen for the best playing experience *****
''')
time.sleep(3)
type_print('''Starting Game''')
for i in range(5):
    time.sleep(0.8)
    type_print('.')
print('''
''')
now = datetime.datetime.now()           #display date and time
type_print(now.strftime("%Y-%m-%d %H:%M:%S"))
type_print('''
Created by: Pranav Tumminkatti,2L'2020
''')
name = ''
while name == '':
   name = str(input('''Hey buddy, what's your name?: '''))
dob = ''
while len(dob)!=8:
    dob = str(input('Date of Birth(DDMMYYYY): '))
dt = dob[0:2]
mt = dob[2:4]
yr = dob[4:]
type_print('Hey '+name+',') 
time.sleep(1)
type_print(' so you were born on a '+find_day(dt.strip('0'),mt.strip('0'),yr)+' huh?')   #utilising the day of week code
time.sleep(1)
type_print('''
That's all cool but look, ''')
time.sleep(0.8)
type_print('''we need to get serious here...
''')
time.sleep(2)
type_print('''I will have to to ask the great lord if this day is auspicious enough for you to play this game...
''')
if find_day(dt.strip('0'),mt.strip('0'),yr) == 'Monday' or find_day(dt.strip('0'),mt.strip('0'),yr) == 'Wednesday' or find_day(dt.strip('0'),mt.strip('0'),yr) == 'Friday' or find_day(dt.strip('0'),mt.strip('0'),yr) == 'Sunday':
    time.sleep(3)                                                       #if the player's day of birth is Monday, Wednesday, Friday or Sunday, then it is auspicious enough for him to play
    type_print('''The supreme lord approves your request...
''')
    time.sleep(2)
    type_print('''You may proceed...
''')
    time.sleep(2)
    type_print('''Follow me closely on my journey into this delusional virtual world...
''')
else:                                                                   #else it is unauspicious, yet I sneak him through
    time.sleep(3)
    type_print('''Oh no, the supreme god says that this day is unauspicious to play this game!
''')
    time.sleep(1)
    type_print('''Mate, this is bad news...
''')
    time.sleep(1)
    type_print('''But fret not, I can sneak you through...
''')
    time.sleep(2)
    type_print('''Follow me closely on my journey and always be alert, the god's servants may be looking for you...
''')
time.sleep(2)
type_print('''Loading Resources
''')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(0.5)             #check for corona
type_print('''Hold up, I completely forgot to test you for the coronavirus...      
''')
type_print('''Just some government formalities, please don't mind...
''')
feel_ok = ''
while feel_ok != 'ok' and feel_ok != 'not ok':            #input validation 
    feel_ok = input('1. How are you feeling today?(ok/not ok): ')
    feel_ok = feel_ok.lower()       #converting the input to lower case
if feel_ok == 'ok':  
    print('great!')
elif feel_ok == 'not ok':
    print('''eh,I'm sure it's just some slight cough. We'll get through just fine...''')
temp = ''
while temp == '':       #input validation
    temp = input('2. What is your temperature today?: ')     
if float(temp)<37.6 and float(temp)>34:
    print('''ok,you're good to go...''')
    abnormal_temp = False
elif float(temp)>=37.6 and float(temp)<45:
    print('''no worries, that's not too high...''')
    abnormal_temp = True
else:
    print('''mate, stop messing around with me...''')
    time.sleep(1)
    print('''argh let's just move on, I don't have the time to deal with your temperature...''')
    abnormal_temp = True
travel = ''
while travel != 'y' and travel != 'n' and travel != 'yes' and travel != 'no':             #input validation
    travel = input('3. Have you travelled out of Singapore in the past 1 month?(y/n): ')
    travel = travel.lower()     #converting the input to lowercase
if travel == 'y' or travel == 'yes':
    which_country = ''          
    while which_country == '':
        which_country = input('4. Which country did you travel to?: ')
        which_country = which_country.lower()
    if which_country == 'india' or which_country == 'america' or which_country == 'usa' or which_country == 'italy' or which_country == 'china':        
        print('''uh, let's just not tell anyone about this...''')
    else:
        print('''nah, not a big deal...let's continue...''')
elif travel == 'n' or travel == 'no':
    print('''that's great!
''')
print('Loading Resources')
for i in range(5):
    time.sleep(0.5)
    print('.')
print('''let's start''')
time.sleep(1)

#Story Code
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    game_to_play = ''
    while game_to_play != '1' and game_to_play != '2' and game_to_play != '3':
        print('''
To play Horror in the Pacific, enter 1
To play the preview of Madness at Hobbsgate, enter 2
To play the preview of Horror in the Darkness, enter 3

Note: Madness at Hobbsgate and Horror in the Darkness are just game previews while Horror in the Pacific is a full-fledged game...
''')
        game_to_play = input('Which game would you like to play?: ')
    if game_to_play == '1':
        introduction()      #if the player wants to play horror in the pacific, then it's introduction function is called
        time.sleep(20)
    elif game_to_play == '2':
        prologue()          #if the player wants to play madness at hobbsgate, then it's prologue function is called
        time.sleep(10)
    elif game_to_play == '3':
        prelude()           #if the player wants to play horror in the darkness, then it's prelude function is called
        time.sleep(20)
    print('')
    type_print('Hey '+name+''', you seem terrified...

''')
    time.sleep(3)
    #checking if the player still wants to continue
    while ask_to_continue() == True:
        if game_to_play == '1':             #deciding which game code to run
            airstrip()      #start state for horror in the pacific
        elif game_to_play == '2':                                  
            quiet_street()  #start state for madness at hobbsgate
        elif game_to_play == '3':
            front_gate()    #start state for horror in the darkness
        break
    while True:                 #checking if the player wants to play again
        answer = input('Would you like to try another game or play this free trial again? (y/n): ')     #input validation
        answer = answer.lower()
        if answer == 'y' or answer == 'n' or answer == 'yes' or answer == 'no':
            break
        else:
            print('Invalid input.')
    if answer == 'y' or answer == 'yes':                     #if the player wants to play again, the story code is run again
        continue
    else:
        type_print('Thank you for playing, '+name+'!')       #if the player does not want to play again, the program is terminated and he is thanked for playing...
        time.sleep(1)
        type_print('''
Goodbye!
''')
        if abnormal_temp == True:                       #if the system recorded an abnormal temperature, the player is asked to take care of his temperature
            time.sleep(1)
            type_print('''
And yes, do take care of your temperature!
''')
        time.sleep(1)                                   #end credits...just like a real game
        print('''
Credits to the following apps for the story texts and idea:
- Horror in the Pacific by Karmic Shift Studios
- Madness at Hobbsgate by Karmic Shift Studios
- Horror in the Darkness by Karmic Shift Studios
''')
        break
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#End of story code  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#End of main code
    
