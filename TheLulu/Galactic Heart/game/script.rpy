# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define narrator = Character("Narrator")
define brandon = Character("Brandon")
define izek = Character("Izek")
define zander = Character("Zander")
define self = Character("Me")

image planetA ="bg_planetA_blur.png"
image planetB ="bg_planetB_blur.png"
image bunk ="bg_bunk_rm"

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

    narrator "Start"


    narrator "Several light years have passed, life at Gaiarise has not been the same without you. "

    narrator "After knowing Solara, a known enemy planet has been stealing resources from neighbouring planets, the people of Galarise had set forth for a mission."
    narrator "To infiltrate and find our information on them, sending their top agent - Agent Izek. But something went wrong, all communication was lost and he  never returned back. Many looked up to him and hoped he would return . "
    narrator "However, now being one of the best, you are needed for a mission. Go to Solara, infiltrate their military. Find information and signal back to the command base to start the siege."
    narrator "And lastly find Izek."

    hide eileen happy

scene bunk at truecenter
menu:
    self "What should I do"
    "Make friends":
        jump choice1_yes
        label choice1_yes:
            $ menu_flag = True
            self "So, what is your name"
            show zander_neutral
            zander "Zander"
            hide zander_neutral
            jump choice1_done
            label choice1_done:
            narrator "Let's explore the area"
            menu: 
                "Finds Meeting Room":
                    jump choice2_yes
                    label choice2_yes:
                        $ menu_flag = True
                        menu: 
                            narrator "You come across important information on Solara’s plan to steal resources from Allied planets."
                            "Sabotage":
                                jump choice21_yes
                                label choice21_yes:
                                    $ menu_flag = True
                                    self "I got to do something about this hmmm.."
                                    jump choice21_done
                                    label choice21_done:
                                        menu:
                                            "Steal Documents":
                                                jump choice211_yes
                                                label choice211_yes:
                                                $ menu_flag = True
                                                self "I need to send this back to the main base.."
                                                narrator "Get caught by higher personnel and is suspicious of you"
                                                
                                                menu:
                                                    "Seduce him":
                                                        jump choice2111_yes
                                                        label choice2111_yes:
                                                        show brandon_neutral
                                                        brandon "I have a wife and 2 kids. I know i look like this but I am loyal to them"
                                                        self "dammit.."
                                                        narrator "You were being brought to the cell"
                                                        hide brandon_neutral
                                                        show bg_jail
                                                        jump choice2111_done
                                                        label choice2111_done:

                                                            narrator "The Questioning"
                                                            narrator "Start of Act 2 (Path 1)"

                                                            narrator "Can you get out of it?  "
                                                            narrator "Getting caught was never the plan but you can always try to get out of it. As the questioning starts, you need to decide what is priority. To escape? Find Izek?"

                                                    "Bribe him":
                                                        show brandon_neutral
                                                        brandon "Fine, i’ll let you off. This is going to help my family.. but its going to cost you."
                                                        narrator "You escaped  but you have to constantly bribe him"
                                                        hide brandon_neutral
                                                        jump choice2_no



                                            "Erase Coordinates":
                                                jump choice221_no
                                                label choice221_no:
                                                $ menu_flag = False
                                                self "I can erase these coordinates.."
                                                narrator "Get caught by higher personnel and is NOT suspicious of you"
                                                jump choice221_done
                                                label choice221_done:
                            

                            "Ignore":
                                jump choice22_yes
                                label choice22_yes:
                                    $ menu_flag = False
                                    self "Its too risky to sabotage the plans now.."
                                    narrator "You weren't caught"
                                    jump choice22_done
                                    label choice22_done:

                        jump choice2_done
                        label choice2_done:
                            
                "Finds Training Room":
                    jump choice2_no
                    label choice2_no:
                        $ menu_flag = False
                        narrator "The Training. Start of Act 2 (Path 2)"
                        narrator "Are you building or burning bridges? Remember to choose wisely and never lose sight of your mission."
                        narrator"As your training begins, you'll face decisions about whether to manipulate others or build alliances. You'll meet Jay, the weakest link in the group, and might rely on your roommate, Zander, to progress. Alternatively, you can try to succeed on your own. But is that the best choice?"
                        jump choice2_done


    "Ignore him":
        jump choice1_no
        label choice1_no:
            $ menu_flag = False
            self "Is that my bed"
            show zander_neutral
            zander "Yes"
            narrator "Zander introduces and explain the facilities"
            jump choice1_done
            "good job"

            
return

    


