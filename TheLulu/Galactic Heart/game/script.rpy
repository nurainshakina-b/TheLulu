# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#Characters
define narrator = Character("")
define connor = Character("Commander Connor")
define brandon = Character("Brandon")
define izek = Character("Izek")
define ian = Character("Commander Ian (AKA Izek)")
define jay = Character("Jay")
define zander = Character("Zander")
define self = Character("Me")
define thoughts = Character("Thinks to self")
define annoucer = Character("Annoucement")
define soldierA = Character("Soldier A")
define soldierB = Character("Soldier B")

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
    show screen grand_screen_1
    


#BACKGROUD INFORMATION
    narrator "Let's start"

    narrator "Several light years have passed, life at Gaiarise has not been the same without you."

    narrator "After knowing Solara, a known enemy planet has been stealing resources from neighbouring planets, the people of Gaiarise had set forth a mission."
    narrator "To infiltrate and find our information on them, sending their top agent - Agent Izek."
    narrator " But something went wrong, all communication was lost and he never returned back. Many looked up to him and hoped he would return."
    narrator "However, now being one of the best, you are needed for a mission. Go to Solara, infiltrate their military. Find information and signal back to the command base to start the siege."
    narrator "And lastly find Izek."

#CONVO1
    show bg_command_base_blur
    with fade

    show connor_neutral
    with vpunch

    connor " Reports from our allies indicate a rise in resource theft. All evidence points to Solara as the perpetrator. Intelligence suggests Gaiarise is their next target. You’re one of our top agents, and this mission falls to you. "
    hide connor_neutral

    self "What’s the mission?" 

    show connor_neutral
    connor "You’re going undercover in Solara. We’re embedding you in their military. Your job is to infiltrate and dig up whatever you can on their plans."
    connor "And don’t forget—find Izek. Undercover name: Ian."
    hide connor_neutral

    self "Izek? After all this time? We haven’t heard from him in ages."
    show connor_neutral
    connor "I know it’s been a while. But we need answers, and we need him back. Whether he’s alive or… not, just bring him home."
    connor "This ring is fingerprint-activated. It’s your signal for the siege of Solara. Use it if you’re in trouble, or when you’ve decided it’s time to initiate the siege."
    hide connor_neutral

    self " I successfully integrate into the military, and begin my journey as a trainee. My mission is clear: gather intelligence and locate Izek. My quest starts now."
    show bunk
    with fade
    with hpunch

    show zander_neutral at truecenter
    self "Training life starts. I come across Zander, my new roommate."
    hide zander_neutral
    

#CHOICE1
menu:
    "Ignore Him":
        jump choice1_yes
        label choice1_yes:
            $ menu_flag = False
            self " So... are you my roommate?"
            show zander_neutral
            zander " Yea.."
            hide zander_neutral
            self " Okayyy"
            thoughts "Hmmm.. Maybe I should I go look around."

            jump choice1_done
            label choice1_done:
            narrator "Let's explore the area"
            show bg_corridor_blur
            with fade
            #CHOICE12
            menu: 
                "Finds Meeting Room":
                    jump choice12_yes
                    label choice12_yes:
                        $ menu_flag = True
                        show bg_meeting_rm_blur
                        with fade
                        self "What’s this? Oh, damn... "
                        self "These are coordinates and secret pathways to Astralis and Lunara—Gaiarise’s allies. " 
                        self "They’re planning to hit them next?? What should I do? Hmm..."

                        menu: 
                            "Sabotage Plans":
                                jump choice13_yes
                                label choice13_yes:
                                    $ menu_flag = True
                                    self "I got to stop this. What do I do?"
                                jump choice13_done
                                label choice13_done:
                                        menu:
                                            "Steal Documents":
                                                jump choice14_yes
                                                label choice14_yes:
                                                $ menu_flag = True
                                                self "These documents. I need to send them back to command base."
                                                narrator "Door Opens. "
                                                self "Oh damn. "
                                                show brandon_neutral
                                                with hpunch
                                                with vpunch
                                                brandon "What are you doing here? Aren’t you a trainee? You’re not authorised to be in here."
                                                hide brandon_neutral
                                                self "Oh, I did not know."
                                                show brandon_neutral
                                                brandon "These are top secret information. How did you get in here?"
                                                hide brandon_neutral
                                                self " I was looking around and I got lost. I was trying to find the training room. I did not mean to cause trouble."
                                                show brandon_neutral
                                                brandon "So you didn’t want to cause trouble.  What’s that you’re holding?"
                                                hide brandon_neutral
                                                thoughts "How do I get out of this? "                                              
                                                menu:
                                                    #CHOICE15
                                                    "Seduce him":
                                                        jump choice15_yes
                                                        label choice15_yes:

                                                        self "Can’t you let me off? I just got lost."
                                                        show brandon_neutral
                                                        brandon "You got lost? And somehow ended up with those classified papers in your hands?"
                                                        hide brandon_neutral
                                                        self " I... I didn’t mean any harm. I’ll do anything to make it right. Please, just let me off the hook. I mean... you’re a good-looking guy. Maybe we could work something out?"
                                                        show brandon_neutral
                                                        brandon "Flattery won’t get you far, but I have to admit, you’ve got guts. Still, you’re in deep water here. What exactly are you offering?"
                                                        hide brandon_neutral
                                                        self "-leans in closer, her voice softening-"
                                                        self "Whatever you want. I just don’t want any trouble... and I’d really hate for this to ruin our first impression. Maybe we could come to a... mutual understanding?"
                                                        show brandon_smirk
                                                        with easeinright
                                                        brandon "I have a wife and two kids. I know I look like this but I am loyal to them. Come on. I’m sending you down to the cells. "
                                                        hide brandon_smirk
                                                        self "Dammit..."
                                                        show screen grand_screen_2_jail
                
                                                        show bg_jail
                                                        with fade
                                                        jump choice15_done
                                                        label choice15_done:

                                                            narrator "Can you get out of it?  "
                                                            narrator "Getting caught was never the plan but you can always try to get out of it. As the questioning starts, you need to decide what is priority. To escape? Find Izek?"
                                                            menu:
                                                                #CHOICE2
                                                                "Ask them questions":
                                                                    jump choice2_yes
                                                                    label choice2_yes:
                                                                        show soldier
                                                                        soldierA "Are you not going to talk?"
                                                                        hide soldier
                                                                        self "I have questions of my own. I’ll talk if you agree to answer mine too."
                                                                        show soldier
                                                                        soldierA "You’re in no position to be making deals."
                                                                        hide soldier
                                                                        self "Do you know Ian(Agent Izek’s undercover name)?"
                                                                        show soldier
                                                                        soldierB "Ian? What does he have to do with this?"
                                                                        hide soldier
                                                                        self "He’s someone I heard about—a name that came up in some old reports. Thought he might be useful to mention. Any idea where he is now?"
                                                                        show soldier
                                                                        soldierB "Ian’s not someone you just ‘hear about. No one’s seen him in ages, but those who do... well, let’s just say he’s not someone to be crossed"
                                                                        hide soldier
                                                                        self "So he’s still around then? I heard he was good at what he did."
                                                                        show soldier
                                                                        soldierB "(scoffs) Good? That’s an understatement. If you’re asking about Ian, you’re treading dangerous ground. Why the sudden interest?"
                                                                        soldierB "What and how do you know of him?"
                                                                        hide soldier                
                                                                        menu:

                                                                            "Semi-lie : He’s a friend":
                                                                                jump choice21_yes
                                                                                label choice21_yes:
                                                                                    
                                                                                    self "We are close friends from back in the orphanage and I came to find him."
                                                                                    show soldier
                                                                                    soldierB "So, you’re friends with Ian.."
                                                                                    hide soldier
                                                                                    self "Yea..You know him, right?"
                                                                                    show soldier
                                                                                    soldierA "We’re familiar. And now that we know you’re close. We can put you to use too."
                                                                                    hide soldier
                                                                                    self "Huh... Okay.."

                                                                                    narrator "As the questioning ends, they report this situation to their commander. A familiar face."

                                                                                    show izek_neutral
                                                                                    ian "What’s this? "
                                                                                    hide izek_neutral
                                                                                    show soldier
                                                                                    soldierA "We have a trainee who we believe is in connection with you and believe that she might be useful for the upcoming mission... Do you recognise her?"
                                                                                    hide soldier
                                                                                    show izek_neutral
                                                                                    ian "...I do. So, she’s here?"
                                                                                    hide izek_neutral
                                                                                    show soldier
                                                                                    soldierA "Yes, sir. She’s currently waiting for further instructions."
                                                                                    hide soldier
                                                                                    show izek_neutral
                                                                                    ian "Send her in. I’ll run through the details of the mission myself."

                                                                                    jump choice22_done
                                                                                        
                                                                            #CHOICE21
                                                                            "Lie : He’s my lover":
                                                                                jump choice21_no
                                                                                label choice21_no:
                                                                                    self "We are romantically involved !"
                                                                                    show soldier
                                                                                    soldierA "You and Ian? Okay, I’ve heard enough from you for today."
                                                                                    hide soldier
                                                                                    self "You’re going to let me off?"
                                                                                    show soldier 
                                                                                    soldierA "No, you’re going back to the cell. We will continue this tomorrow."
                                                                                    hide soldier
                                                                                    narrator "As the questioning ends, they report this situation to their commander. A familiar face."


                                                                                    jump choice3_lover
                                                                                    
                                                                    jump choice2_done


                                                                #CHOICE2
                                                                "Act clueless":
                                                                    jump choice2_no
                                                                    label choice2_no:
                                                                        show soldier
                                                                        soldierA " Do you realise what those documents are?"
                                                                        hide soldier
                                                                        self "Oh, these? I thought they were just routine reports. Am I not supposed to have them?"
                                                                        show soldier
                                                                        soldier"Routine reports? You expect us to believe you just stumbled upon classified material by accident?"
                                                                        hide soldier
                                                                        menu: 
                                                                            "Show confusion":
                                                                                jump choice212_yes
                                                                                label choice212_yes:
                                                                                    self "I don’t understand.. How are they important? Can you explain"
                                                                                    show soldier
                                                                                    soldierA "You really don’t know what you’re holding, do you?"
                                                                                    hide soldier
                                                                                    self "No, I honestly don’t. They just looked like regular reports to me. Is there something special about them?"
                                                                                    show soldier
                                                                                    soldierA "These ‘regular reports’ are strategic assessments—highly sensitive intel. They outline potential vulnerabilities in our operations, detailed coordinates, and troop movements. Information like this in the wrong hands could jeopardize entire missions"
                                                                                    hide soldier
                                                                                    self "Oh... I had no idea. I swear, I wasn’t trying to snoop or anything. I’m just new and trying to get up to speed. I didn’t realize how serious this was.."
                                                                                    show soldier
                                                                                    soldierA "This isn’t something to take lightly. You’re lucky we’re not treating this as espionage... yet. Stay away from documents like these unless you’re cleared to handle them."
                                                                                    hide soldier
                                                                                    self "Absolutely! I’ll be more careful. I didn’t mean to cause any trouble. Thank you for explaining."
                                                                                    show soldier
                                                                                    soldierA "You are let off with a warning but you are also underestimated"
                                                                                    hide soldier
                                                                                jump choice12_no
                                                                                label choice212_done:

                                                                            "Deflect Questions":
                                                                                jump choice212_no
                                                                                label choice212_no:
                                                                                    narrator "I thought I was just doing my job.. I was just following orders. Can I go now?"
                                                                                    narrator "You are released but will be closely monitored."
                                                                                jump choice12_no

                                                                    jump choice2_done

                                                    #CHOICE15
                                                    "Bribe him":
                                                        jump choice15_no
                                                        label choice15_no:
                                                        self "Can’t you let me off? I was just curious about what this was all about. "
                                                        show brandon_neutral
                                                        brandon "Why did you need to know? "
                                                        hide brandon_neutral
                                                        self " I’m new here, and honestly, a bit of an overachiever. I just wanted to be prepared. Please, just this once, let it slide. I’ll make it worth your while—Celestium, as much as you want. Name your price."
                                                        show brandon_neutral
                                                        brandon "Alright, I’ll let it go. This’ll help my family… but it’s going to cost you. "
                                                        hide brandon_neutral
                                                        self "Okay so 50 Celestium anytime? "
                                                        show brandon_neutral
                                                        with vpunch
                                                        brandon "You got yourself a deal."
                                                        brandon " You’re playing a dangerous game, Alia. But maybe I can be persuaded... this time. Just remember, I’m not as easy to sway as you might think. If you get caught again, you’re on your own."
                                                        hide brandon_neutral
                                                        thoughts "That was a close call. I got away this time. But why the heck did I offer 50 Celestium, anytime? This is going to cost me big time. Dammit. Now where’s the training room?"
                                                        show screen grand_screen_2
                                                        jump choice2p2

                                            #CHOICE14
                                            "Erase Coordinates":
                                                jump choice14_no
                                                label choice14_no:
                                                $ menu_flag = False
                                                self "Wait, these seem to be the only copies they have. I could just erase the coordinates."
                                                narrator "Door opens."
                                                show brandon_neutral
                                                with hpunch
                                                brandon "What are you doing here? Aren’t you a trainee? You’re not authorised to be in here."
                                                hide brandon_neutral
                                                self "Oh, I did not know."
                                                show brandon_neutral
                                                brandon "Mind you trainee, only a higher personnel like myself and your sergeant majors could enter in here and not the likes of you. So.. how did you get in here?"
                                                hide brandon_neutral
                                                self " I was looking around and I got lost. I was trying to find the training room. I did not mean to cause trouble."
                                                show brandon_neutral
                                                brandon "Don’t come in here unless you were told to again. The Combat Simulation Chamber is right around the corner. Now, go your training is about to start."
                                                hide brandon_neutral
                                                show screen grand_screen_2

                                                jump choice2p2
                                                label choice14_done:
                            

                            #CHOICE13
                            "Ignore Plans":
                                jump choice13_no
                                label choice13_no:
                                    $ menu_flag = False
                                    self "It’s too risky to do anything now. I’ll have to report back what I saw. Maybe I could come back here again. I need to go to the training room now."
                                    narrator "You weren't caught"
                                    jump choice2p2
                                    show screen grand_screen_2

                        jump choice2_done
                        label choice2_done:
                            
                #CHOICE12
                "Finds Training Room":
                    show bg_training_rm_blur
                    with fade
                    jump choice12_no
                    label choice12_no:
                        $ menu_flag = False
                        self "Combat Simulation Chamber? Hmm.. Ahhh so this is the training room."


                        jump choice2p2
                        label choice2p2:
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


    "Make Friends":
        jump choice1_no
        label choice1_no:
            $ menu_flag = True
            self "Hey... I’m Alia and I’m new here. What’s your name? "
            show zander_neutral
            zander "Oh hey, Zander here. Do you want me to show you around? "
            hide zander_neutral
            self "That’d be great, thanks..!"
            show bg_corridor_blur
            with fade
            show zander_neutral
            zander "So, here’s the Neural Lounge— it’s our version of a break room. You can decompress and clear your mind from a tough mission here. Over there, we have the Holo-Conferencing Room. That’s where we sync commands across the galaxy in real-time."
            hide zander_neutral
            self "Impressive... What’s next?"
            show zander_neutral
            zander "Now, we’re heading to the Combat Simulation Chamber. It’s where you’ll be training."
            hide zander_neutral
            self "Cool... So, is training tough? "
            show zander_neutral
            zander "Let’s just say, the sim chamber adapts to your skill level. You’ll be facing everything from basic drills to full-scale virtual invasions. But don’t worry—you’re going to find out soon enough"
            hide zander_neutral
            show screen grand_screen_2

        jump choice2p2

            
return

    


