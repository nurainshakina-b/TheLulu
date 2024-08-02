# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define narrator = Character("Narrator")
define brandon = Character("Brandon")
define izek = Character("Izek")
define ian = Character("Ian")
define zander = Character("Zander")
define self = Character("Me")

image planetA ="bg_planetA_blur.png"
image planetB ="bg_planetB_blur.png"
image bunk ="bg_bunk_rm_blur.png"
image jailblur = "bg_jail_blur.png"

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
                                                            menu:
                                                                "Knowing that you got caught, you decide to use this opportunity to find out about Izek. Manipulate information out of them":
                                                                    jump choice3_yes
                                                                    label choice3_yes:
                                                                        show brandon_neutral
                                                                        brandon "Are you not going to talk?"
                                                                        narrator " Interrogators are intrigued and start revealing information about Ian (Agent Izek’s undercover name)"
                                                                        narrator "Express familiarity with Ian"
                                                                        hide brandon_neutral                
                                                                        menu:
                                                                            "How did you know him? Who are you to him?"

                                                                            "Tell a semi -lie and that say he is a friend you’ve been searching for.":
                                                                                jump choice31_yes
                                                                                label choice31_yes:
                                                                                    show brandon_neutral
                                                                                    brandon "We are close friends back in the orphanage and I came to find him"
                                                                                    narrator "Interrogators are intrigued and devise a plan to use you for further operations."
                                                                                    narrator "You become a trusted agent (although you are not sure why)"
                                                                                    hide brandon_neutral
                                                                                    show brandon_neutral
                                                                                    brandon "So, you’re friends with Izek..."
                                                                                    brandon "Yea.. do you know him?"
                                                                                    brandon "chuckles"
                                                                                    brandon "Do we know him? we’re familiar..But now we know that you’re close. We can put you to use too"
                                                                                    narrator "You learn that they play to use you in the upcoming operation."
                                                                                    narrator "Izek, now a top operative in the organisation, receives the report and notices your name and details."
                                                                                    hide brandon_neutral
                                                                                    izek "Whats this?"
                                                                                    izek "We have a trainee that we believe is in connection with you and believe that she might be useful for the upcoming mission..Do you recognise her?"
                                                                                    narrator "He further investigate and reviews the documents. He connects the dots and recognises you."
                                                                                    izek "Wait.. i do"
                                                                                    narrator "Calls her into the office under the disguise sharing information of the mission."
                                                                                    izek "Send her in... I’ll run through the details of the mission myself.."
                                                                                    jump choice31_done
                                                                                    label choice31_done:
                                                                                        
                                                                            "Tell them he is your lover. Demand them to tell if he is alive or dead":
                                                                                jump choice31_no
                                                                                label choice31_no:
                                                                                    brandon "We are romantically involved !"
                                                                                    narrator "They stop questioning and look anxious to continue. You receive leniency and it gave you more time to plan."
                                                                                    narrator "They alert the top guy (Izek) about the situation and sends her back to the cell."
                                                                                    narrator "Izek receives the report regarding you. Confuse and intrigued with her claims."
                                                                                    narrator "Izek goes down to the cell, about to confront you."
                                                                                    jump choice31_done
                                                                                    
                                                                    jump choice3_done


                                                                "You can still escape this if you play your cards right. Lie and act clueless":
                                                                    jump choice3_no
                                                                    label choice3_no:
                                                                        narrator "Interrogators become suspicious but have no concrete evidence."
                                                                        menu: 
                                                                            "Show further confusion":
                                                                                jump choice32_yes
                                                                                label choice32_yes:
                                                                                    narrator "I don’t understand.. How are they important? Can you explain"
                                                                                    narrator "Interrogators explains, giving you time to gather information."
                                                                                    narrator "Feign ignorance and escape"
                                                                                    narrator "I’m sorry, I didn’t know. I’ll be more careful. I thought i was just doing the right thing.."
                                                                                    narrator "We will let you off for now. Let this be a warning."
                                                                                    narrator "You are let off with a warning but you are also underestimated"
                                                                                jump choice2_no
                                                                                label choice32_done:

                                                                            "Deflect Questions":
                                                                                jump choice32_no
                                                                                label choice32_no:
                                                                                    narrator "I thought I was just doing my job.. I was just following orders. Can I go now?"
                                                                                    narrator "You are released but will be closely monitored."
                                                                                jump choice2_no

                                                                    jump choice3_done
                                                                    label choice3_done:

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
                                    jump choice2_no
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

    


