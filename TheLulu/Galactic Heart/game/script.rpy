﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image planetA ="planetA.jpg"
image planetB ="planetB.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene planetA at truecenter
    with dissolve

    


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Start"


    e "You are needed for a mission. 
    To go undercover and infiltrate the military 
    Find information and signal to Command Base to start the siege
    Retrieve Agent M"

    show testing

    e "“Is that my bed?”"

    



    # This ends the game.

    return
