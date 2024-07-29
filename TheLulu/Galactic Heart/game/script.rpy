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


    e "Several light years have passed, life at Gaiarise has not been the same without you. "


    e "After knowing Solara, a known enemy planet has been stealing resources from neighbouring planets, the people of Galarise had set forth for a mission."
    e "To infiltrate and find our information on them, sending their top agent - Agent Izek. But something went wrong, all communication was lost and he  never returned back. Many looked up to him and hoped he would return . "
    e "However, now being one of the best, you are needed for a mission. Go to Solara, infiltrate their military. Find information and signal back to the command base to start the siege."
    e "And lastly find Izek."

    hide eileen happy

    show testing

    e "“Is that my bed?”"

    



    # This ends the game.

    return
