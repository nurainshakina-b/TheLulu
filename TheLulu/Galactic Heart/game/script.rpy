# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#Characters
define narrator = Character("Narrator")
define brandon = Character("Brandon")
define izek = Character("Izek")
define ian = Character("Ian")
define jay = Character("Jay")
define zander = Character("Zander")
define self = Character("Me")
define annoucer = Character("Annoucement")

image planetA ="bg_planetA_blur.png"
image planetB ="bg_planetB_blur.png"
image bunk ="bg_bunk_rm_blur.png"
image jailblur = "bg_jail_blur.png"
image planetboth = "bg_planetBoth_blur.png"

default player_trust=50
default player_trust_max = 100


 

# The game starts here.

label start:    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    

    show planetboth
    with fade
    hide planetA
    



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.



    show screen single_stat


    narrator "Start"

    narrator "Several light years have passed, life at Gaiarise has not been the same without you. "

    narrator "After knowing Solara, a known enemy planet has been stealing resources from neighbouring planets, the people of Galarise had set forth for a mission."
    narrator "To infiltrate and find our information on them, sending their top agent - Agent Izek. But something went wrong, all communication was lost and he  never returned back. Many looked up to him and hoped he would return . "
    narrator "However, now being one of the best, you are needed for a mission. Go to Solara, infiltrate their military. Find information and signal back to the command base to start the siege."
    narrator "And lastly find Izek."
    

    # hide eileen happy

show bunk
with fade
with hpunch

menu:
    self "What should I do"
    "Make friends":
        jump choice1_yes
        label choice1_yes:
            $ menu_flag = True
            self "So, what is your name?"
            show zander_neutral

            zander "Zander"
            hide zander_neutral
            jump choice12_no
            label choice1_done:
            narrator "Let's explore the area"
            menu: 
                "Finds Meeting Room":
                    jump choice12_yes
                    label choice12_yes:
                        $ menu_flag = True
                        show bg_meeting_rm_blur
                        with fade
                        menu: 
                            narrator "You come across important information on Solara’s plan to steal resources from Allied planets."
                            "Sabotage":
                                jump choice13_yes
                                label choice13_yes:
                                    $ menu_flag = True
                                    self "I got to do something about this hmmm.."
                                jump choice13_done
                                label choice13_done:
                                        menu:
                                            "Steal Documents":
                                                jump choice14_yes
                                                label choice14_yes:
                                                $ menu_flag = True
                                                self "I need to send this back to the main base.."
                                                narrator "Get caught by higher personnel and is suspicious of you"
                                                
                                                menu:
                                                    "Seduce him":
                                                        jump choice15_yes
                                                        label choice15_yes:
                                                        hide zander_neutral
                                                        show brandon_neutral
                                                        brandon "I have a wife and 2 kids. I know i look like this but I am loyal to them"
                                                        self "Dammit.."
                                                        narrator "You were being brought to the cell"
                                                        hide brandon_neutral
                                                        show bg_jail
                                                        with fade
                                                        jump choice15_done
                                                        label choice15_done:

                                                            narrator "The Questioning"
                                                            narrator "Start of Act 2 (Path 1)"

                                                            narrator "Can you get out of it?  "
                                                            narrator "Getting caught was never the plan but you can always try to get out of it. As the questioning starts, you need to decide what is priority. To escape? Find Izek?"
                                                            menu:
                                                                "Knowing that you got caught, you decide to use this opportunity to find out about Izek. Manipulate information out of them":
                                                                    jump choice2_yes
                                                                    label choice2_yes:
                                                                        show brandon_neutral
                                                                        brandon "Are you not going to talk?"
                                                                        narrator " Interrogators are intrigued and start revealing information about Ian (Agent Izek’s undercover name)"
                                                                        narrator "Express familiarity with Ian"
                                                                        hide brandon_neutral                
                                                                        menu:
                                                                            "How did you know him? Who are you to him?"

                                                                            "Tell a semi -lie and that say he is a friend you’ve been searching for.":
                                                                                jump choice21_yes
                                                                                label choice21_yes:
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
                                                                                    jump choice22_done
                                                                                        
                                                                            "Tell them he is your lover. Demand them to tell if he is alive or dead":
                                                                                jump choice21_no
                                                                                label choice21_no:
                                                                                    brandon "We are romantically involved !"
                                                                                    narrator "They stop questioning and look anxious to continue. You receive leniency and it gave you more time to plan."
                                                                                    narrator "They alert the top guy (Izek) about the situation and sends her back to the cell."
                                                                                    narrator "Izek receives the report regarding you. Confuse and intrigued with her claims."
                                                                                    narrator "Izek goes down to the cell, about to confront you."
                                                                                    jump choice3_lover
                                                                                    
                                                                    jump choice2_done


                                                                "You can still escape this if you play your cards right. Lie and act clueless":
                                                                    jump choice2_no
                                                                    label choice2_no:
                                                                        narrator "Interrogators become suspicious but have no concrete evidence."
                                                                        menu: 
                                                                            "Show further confusion":
                                                                                jump choice212_yes
                                                                                label choice212_yes:
                                                                                    narrator "I don’t understand.. How are they important? Can you explain"
                                                                                    narrator "Interrogators explains, giving you time to gather information."
                                                                                    narrator "Feign ignorance and escape"
                                                                                    narrator "I’m sorry, I didn’t know. I’ll be more careful. I thought i was just doing the right thing.."
                                                                                    narrator "We will let you off for now. Let this be a warning."
                                                                                    narrator "You are let off with a warning but you are also underestimated"
                                                                                jump choice12_no
                                                                                label choice212_done:

                                                                            "Deflect Questions":
                                                                                jump choice212_no
                                                                                label choice212_no:
                                                                                    narrator "I thought I was just doing my job.. I was just following orders. Can I go now?"
                                                                                    narrator "You are released but will be closely monitored."
                                                                                jump choice12_no

                                                                    jump choice2_done

                                                    "Bribe him":
                                                        hide zander_neutral
                                                        show brandon_neutral
                                                        brandon "Fine, i’ll let you off. This is going to help my family.. but its going to cost you."
                                                        narrator "You escaped  but you have to constantly bribe him"
                                                        hide brandon_neutral
                                                        jump choice12_no



                                            "Erase Coordinates":
                                                jump choice14_no
                                                label choice14_no:
                                                $ menu_flag = False
                                                self "I can erase these coordinates.."
                                                narrator "Get caught by higher personnel and is NOT suspicious of you"
                                                jump choice12_no
                                                label choice14_done:
                            

                            "Ignore":
                                jump choice13_no
                                label choice13_no:
                                    $ menu_flag = False
                                    self "Its too risky to sabotage the plans now.."
                                    narrator "You weren't caught"
                                    jump choice12_no

                        jump choice2_done
                        label choice2_done:
                            
                "Finds Training Room":
                    show bg_training_rm_blur
                    with fade
                    jump choice12_no
                    label choice12_no:
                        $ menu_flag = False
                        narrator "The Training. Start of Act 2 (Path 2)"
                        narrator "Are you building or burning bridges? Remember to choose wisely and never lose sight of your mission."
                        narrator"As your training begins, you'll face decisions about whether to manipulate others or build alliances. You'll meet Jay, the weakest link in the group, and might rely on your roommate, Zander, to progress. Alternatively, you can try to succeed on your own. But is that the best choice?"
                        narrator "Training obstacle begins and individuals who fail will not advance"
                        menu:
                            "Burning Bridges":
                                jump choice22_yes
                                label choice22_yes:
                                show bg_training_rm_blur
                                with fade
                                narrator "Sabotage others"
                                self "If only I could make 1 other person slip.."
                                narrator "People get suspicious and anxious."
                                narrator "Work alone"
                                narrator "Complete the task fast"
                                self "Since I got time to spare, let's explore"
                                hide bg_training_rm_blur
                                show bg_corridor_blur
                                with fade
                                narrator "Proceeds to explore other facilities- left training grounds"
                                
                                narrator "Guard caught you entering a restricted area with classified information."
                                show bg_jail_blur
                                with fade
                                narrator "You get send to the cell."
                                narrator "Authorities are alerted, reports were to the top guy."
                                narrator "Izek got  the report about her and ask her to be brought to the office."
                                jump choice22_done
                                label choice22_done:
                                menu: 
                                    "The Confrontation":
                                        jump choice3_lie
                                        label choice3_lie:
                                        narrator "The confrontation: Love or War?"
                                        narrator "As you come face to face with him, you discovers the truth. But is he the same person, can he be trusted?"
                                        narrator "You got called in to talk to the commander of Solara’s military."
                                        narrator "Found out that the commander is Izek"
                                        self "What is going on..No this can’t be"
                                        narrator "You are suspicious"
                                        jump choice3_liecut
                                        label choice3_liecut:
                                        narrator "Confront him"
                                        self "I can’t believe you would do this.. You really betrayed us?"
                                        show izek_neutral
                                        izek " I did no such thing. I still stand with Gaiarise."
                                        hide izek_neutral
                                        narrator "Izek reveals his plans and what he has been doing"
                                        show izek_neutral
                                        izek "Its just plans changed. The people of Solara don’t deserve this. They need help... I have a plan to get rid of the corrupt."
                                        hide izek_neutral
                                        self "... and what? You’re not corrupted?"
                                        show izek_neutral
                                        izek " Do you really think i would do that to my home planet? ... To you? I have a plan and now that I know you’re here. You can help. Believe me Pleasee.."
                                        
                                        #calculated trust point determines, need to research
                                        menu:
                                            #High score of trust points
                                            "Believe him":
                                                jump choice31_yes
                                                label choice31_yes:
                                                    show planetboth
                                                    narrator "He tells you what to do"
                                                    narrator "Deciding to work with him, you send covert messages back to the command base. Sharing details of Izek and the current state of the planet. With Izek’s lead, he carried out a revolution with the Solaraian military and took down the corrupted regime. "
                                                    narrator "Solara is rebuilding and mending its relationship with the planets they have wronged before. And with the newfound support of Gaiarise, an alliance was formed and this is the start of a new beginning for Solara. "
                                                    narrator "After all is well, you and Izek explore old feelings and your happily ever after is just beginning. "
                                                    narrator "Spread love, not war."
                                                    jump choice31_done
                                                    label choice31_done:
                                            #Low score of trust points
                                            "Do not believe him":
                                                show planetboth
                                                jump choice31_no
                                                label choice31_no:
                                                    narrator "Izek tries to share his plans but because of blind anger and frustration you reveal your plans to signal the siege to the command base (through a hidden button on your bracelet)"
                                                    show izek_neutral
                                                    izek "Listen, its not what you think.. I wouldn’t.."
                                                    hide izek_neutral
                                                    self "You really think i’ll listen to you.. I can’t risk it. I will not give up Gaiarise...not even for you. I’m sorry. I am going to signal for siege"
                                                    show izek_neutral
                                                    izek "...wait.. "
                                                    izek"/sighs/"
                                                    izek "Do it... Its okay... Its going to be harder to convince them but I will never blame you..."
                                                    hide izek_neutral
                                                    narrator "Signal for siege"
                                                    narrator "While all is well for Gaiarise, its been revealed how corrupted the government of Solara is. The siege might have been saving grace for the people but it was going to take a longer time for Gaiarise and the people Solara to get along. "
                                                    narrator "As for Izek, his loyalty is question. However, he never blamed you for his current situation. He knew its going to take a lot of convincing and evidence to prove his allegiance to Gaiarise. "
                                                    narrator "Due to high tensions, they were never able to share their feelings for one another. With the stakes high, the protagonist was not willing to risk her planet, even for the man she loves. "
                                                    narrator "Was it the right choice?"
                                                    jump choice31_done
                                        
                                        jump choice3_lover
                                        
                                    "The Confrontation":
                                        label choice3_lover:
                                            show brandon_neutral
                                            brandon "The commander wants to see you.."
                                            self "The commander?"
                                            self "gasps.. Its you.."
                                            hide brandon_neutral
                                            show izek_neutral
                                            izek "The rest can leave.. It seems like we have some reconnecting to do right?"
                                            hide izek_neutral
                                            narrator "you are surprise and suspicious"
                                            self "You’re okay.. you are alive?"
                                            show izek_neutral
                                            izek "As you can see I am better than okay.. soo how did you end up here ... lover"
                                            hide izek_neutral
                                            self "You’re the commander now, the leader of the Solara military?"
                                            menu: 
                                                "Reveal your plans":
                                                    jump choice311_yes
                                                    label choice311_yes:
                                                        self "If you remember me, then you would know I came to find you"
                                                        show izek_neutral
                                                        izek "Is that all that is?"
                                                        hide izek_neutral
                                                        self "I came to find you!?"
                                                        jump choice3_liecut

                                                "Find out more about him":
                                                    jump choice311_no
                                                    label choice311_no:
                                                        self "What happened to you? I thought you were dead?"
                                                        show izek_neutral
                                                        izek "I became the leader..."
                                                        hide izek_neutral
                                                    jump choice311_done
                                                    label choice311_done:
                                                        menu:
                                                            "Show frustration":
                                                                jump choice3111_yes
                                                                label choice3111_yes:
                                                                    self "Everyone has been worried about you ever since your contact got cut but it seems like I was worried sick for nothing. Glad to know."
                                                                    #link to the nodes
                                                                jump choice31_no
                                                                label choice3111_done:
                                              
                                                            "Show concern":
                                                                jump choice3111_no
                                                                label choice3111_no:
                                                                    self "Are you okay? I  haven’t heard from you for so long...Are you hurt?"
                                                                    show izek_neutral
                                                                    izek " I’ve been better...Glad to know you still care about me.. Oh wait.. we’re lovers right"
                                                                    hide izek_neutral
                                                                    self "You know why I said that. Is your allegiance to Solara now?"
                                                                    narrator "Izek explains the current situation"
                                                                    show izek_neutral
                                                                    izek "You know, i wouldn’t do that to you right.."
                                                                    izek "My loyalty will always be Gaiarise and to you. After helping you train all these years, wouldn’t you know me enough to not question my loyalty."
                                                                    hide izek_neutral
                                                                    self "I am not sure anymore."
                                                                    show izek_slightsmile
                                                                    izek "Well, then you would remember this. I  have feelings for you."
                                                                    hide izek_slightsmile
                                                                    self "Do not bring our feelings into this."
                                                                    narrator"end"






                            "Building Bridges":
                                jump choice22_no
                                label choice22_no:
                                    narrator "Push other to work together"
                                    self "We should all work together"
                                    narrator"Strengthen current bonds with Jay and Zander"
                                    narrator "Your bond led to finding out information about Izek and more about the people of Solara"
                                    show brandon_neutral
                                    brandon "Did you guys hear about the story of the guy who died here?"
                                    hide brandon_neutral
                                    self "“What? Someone died? Who”"

                                    menu:
                                        "Ask about when it happen":
                                            jump choice221_yes
                                            label choice221_yes:
                                                self "When was this?"
                                                show brandon_neutral
                                                brandon "Like 3- 4 years ago ish..?"
                                                brandon "I mean there were rumours that there people trying to cover up the whole thing"
                                                brandon "I remember seeing some big meeting  happening among the leaders at A2 ll meeting room. I almost got into trouble there."
                                                hide brandon_neutral
                                                self  "Huh...interesting..."
                                                narrator "Through the conversation, you find out about the meeting room."
                                                narrator "You are motivated now that you learn something crucial. You urge your teammates to complete the training so they could have a break ."
                                                self "That's enough, lets get through this fast so that we could get a break.."
                                                narrator "Comeplete the training"
                                                jump choice221_done
                                                label choice221_done:
                                                    menu: 
                                                        "Sneak away and find the meeting room.":
                                                            jump choice222_yes
                                                            label choice222_yes:
                                                        #will direct this and add a menu to "Guard caught you entering a restricted area with classified information."
                                                            jump choice222_done
                                                        
                                                        "Stay with teammates":
                                                            jump choice222_no
                                                            label choice222_no:
                                                                narrator "Announcement bell rang"
                                                                annoucer "Attention trainees! Please report to the training grounds for the Annual Solara Trainee Sparring. "
                                                                narrator "Heads to the training grounds, where they gave a boring speech to start off."
                                                                show bg_training_rm_blur
                                                                with fade
                                                                annoucer "Welcome trainees to the Annual Solara Trainee Sparring. Everyone is required to attend. Fight till one is left standing. The winner will receive an opportunity to lead our upcoming mission alongside our Commander"
                                                                narrator "Proceeds to fight"
                                                                self " Well looks like this will be a breeze. Let’s give my all then! "
                                                                narrator "Became the last pair standing"
                                                                self "So close to the finishing line. I can’t give up yet."
                                                                narrator "Managed to defeat the other trainee and became the winner of Solara’s Annual Trainee Sparring"
                                                                
                                                                narrator "Izek stood by the sidelines at the training ground while listening to the boring opening ceremony"
                                                                show izek_neutral
                                                                izek "I detest attending these kind of events but hm let’s see what the trainees got... "
                                                                narrator "He asks the nearby guard for the name of the newbie that won"
                                                                izek "Send me that trainee’s document to my office now."
                                                                #will create a menu to link back to "Calls her into the office under the disguise sharing information of the mission."
                                                                jump choice222_done
                                                                label choice222_done:
                                        "Ask how he looked like?":
                                            jump choice221_no
                                            label choice221_no:
                                                self "What did he look like?"
                                                show zander_neutral
                                                zander "Some said he had dark hair and some said he was blonde.. honestly we don’t really know. The story is been pass down a lot, we don’t really know if its accurate.."
                                                zander "You’re really into this huh.."

                                                hide zander_neutral
                                                narrator "Through the  conversation you find out how the people of Solara are against the rulers and are suffering."
                                                zander "But yeah its not surprising that the government do nothing about it.." 
                                                zander "I bet they kept the higher up silent about it too"
                                                self "Why do you say that?"
                                                zander "I mean don’t you know our government doesn’t care about our people..."
                                                self "Ohh right right...You know for being such a hater...why are you even here? You’re not exactly err.. soldier material?"
                                                zander "I had too. For my family.You understand right.."
                                                self ".. I mean yeaa yeaa.."
                                                jump choice222_no
                        jump choice2_done


    "Ignore him":
        jump choice1_no
        label choice1_no:
            $ menu_flag = False
            self "Is that my bed?"
            show zander_neutral
            zander "Yes"
            narrator "Zander introduces and explain the facilities"
            hide zander_neutral
            jump choice1_done
            "good job"

            
return

    


