# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#Characters
define narrator = Character("")
define connor = Character("Commander Connor")
define brandon = Character("Brandon")
define izek = Character("Izek")
define ian = Character("Commander Ian")
define jay = Character("Jay")
define zander = Character("Zander")
define self = Character("Me")
define thoughts = Character("Me")
define announcer = Character("Annoucement")
define soldierA = Character("Soldier A")
define soldierB = Character("Soldier B")
define soldierC = Character("Soldier C")
define faceless = Character("Random Soldier")

image planetA ="bg_planetA_blur.png"
image planetB ="bg_planetB_blur.png"
image bunk ="bg_bunk_rm_blur.png"
image jailblur = "bg_jail_blur.png"
image planetboth = "bg_planetBoth_blur.png"

default player_trust = 50
default player_trust_max = 100


 

# The game starts here.

label start:    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png"or "bg room.jpg") to the
    # images directory to show it.
    
    play music "audio/Bleeping Demo.mp3" volume 0.5 loop
    show planetboth
    with fade
    hide planetA
    



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png"to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.



    show screen single_stat
    show screen grand_screen_1
    


#BACKGROUD INFORMATION
    narrator "Let's start."

    narrator "Several light years have passed, life at Gaiarise has not been the same without you."

    narrator """After knowing Solara, a known enemy planet has been stealing resources from neighbouring planets, the people of Gaiarise had set forth a mission-
    
    To infiltrate and find out information on them, sending their top agent - Agent Izek.

    But something went wrong, all communication was lost and he never returned back. Many looked up to him and hoped he would return.

    However, now being one of the best, I am needed for a mission.

    Go to Solara, and infiltrate their military. Find information and signal back to the command base to start the siege.

    And lastly, find Izek."""

#CONVO1
    show bg_command_base_blur
    with fade

    show connor_neutral
    with vpunch

    connor "Reports from our allies indicate a rise in resource theft. All evidence points to Solara as the perpetrator."
    connor "Intelligence suggests Gaiarise is their next target. You’re one of our top agents, and this mission falls on you."
    hide connor_neutral

    self "What’s the mission?"

    show connor_neutral
    connor """You’re going undercover in Solara. We’re embedding you in their military.

    Your job is to infiltrate and dig up whatever you can on their plans.
    
    And don’t forget—find Izek. His undercover name is Ian."""
    hide connor_neutral

    self "Izek? After all this time? We haven’t heard from him in ages."
    show connor_neutral
    connor "I know it’s been a while. But we need answers, and we need him back."
    connor "Whether he’s alive or… not, just bring him home."
    connor "This ring is fingerprint-activated. It’s your signal for the siege of Solara."
    connor "Use it if you’re in trouble, or when you’ve decided it’s time to initiate the siege."
    hide connor_neutral

    """I successfully integrate into the military, and begin my journey as a trainee.

    My mission is clear: gather intelligence and locate Izek. My quest starts now."""
    show bunk
    with fade
    with hpunch

    show zander_neutral at truecenter
    self "Training life starts. I come across Zander, my new roommate."
    hide zander_neutral
    

#CHOICE1
menu:
    "Ignore him":
        jump choice1_yes
        label choice1_yes:
            $ menu_flag = False
            self "So... are you my roommate?"
            show zander_neutral
            zander "Yeah."
            hide zander_neutral
            self "Okay..."
            thoughts "{i}Hmmm.. Maybe I should I go look around.{\i}"

            jump choice1_done
            label choice1_done:
            narrator "Let's explore the area"
            show bg_corridor_blur
            with fade
            #CHOICE12
            menu: 
                "Find Meeting Room":
                    jump choice12_yes
                    label choice12_yes:
                        stop music fadeout 1.0
                        play music "audio/Half Mystery.mp3" volume 0.5 loop
                        $ menu_flag = True
                        show bg_meeting_rm_blur
                        with fade
                        self "What’s this? Oh, damn..."
                        self "These are coordinates and secret pathways to Astralis and Lunara—Gaiarise’s allies."
                        self "They’re planning to hit them next? What should I do? Hmm..."

                        menu: 
                            "Sabotage plans":
                                jump choice13_yes
                                label choice13_yes:
                                    $ menu_flag = True
                                    self "I got to stop this. What do I do?"
                                jump choice13_done
                                label choice13_done:
                                        menu:
                                            "Steal documents":
                                                jump choice14_yes
                                                label choice14_yes:
                                                $ menu_flag = True
                                                self "These documents. I need to send them back to command base."
                                                play sound "audio/Door Open.mp3" volume 0.8
                                                narrator "Door Opens."
                                                self "Oh damn."
                                                show brandon_neutral
                                                with hpunch
                                                with vpunch
                                                brandon "What are you doing here? Aren’t you a trainee? You’re not authorised to be in here."
                                                hide brandon_neutral
                                                self "Oh, I did not know."
                                                show brandon_neutral
                                                brandon "These are top secret information. How did you get in here?"
                                                hide brandon_neutral
                                                self "I was looking around and I got lost. I was trying to find the training room. I did not mean to cause trouble."
                                                show brandon_neutral
                                                brandon "So you didn’t want to cause trouble.  What’s that you’re holding?"
                                                hide brandon_neutral
                                                thoughts "{i}How do I get out of this?{\i}"                                             
                                                menu:
                                                    #CHOICE15
                                                    "Seduce him":
                                                        jump choice15_yes
                                                        label choice15_yes:

                                                        self "Can’t you let me off? I just got lost."
                                                        show brandon_neutral
                                                        brandon "You got lost? And somehow ended up with those classified papers in your hands?"
                                                        hide brandon_neutral
                                                        self "I... I didn’t mean any harm. I’ll do anything to make it right. Please, just let me off the hook. I mean... you’re a good-looking guy. Maybe we could work something out?"
                                                        show brandon_neutral
                                                        brandon "Flattery won’t get you far, but I have to admit, you’ve got guts. Still, you’re in deep water here. What exactly are you offering?"
                                                        hide brandon_neutral
                                                        narrator "I lean in closer to him, my voice softening-"
                                                        self "Whatever you want. I just don’t want any trouble... and I’d really hate for this to ruin our first impression. Maybe we could come to a... mutual understanding?"
                                                        show brandon_smirk
                                                        with easeinright
                                                        brandon "I have a wife and two kids. I know I look like this but I am loyal to them. Come on. I’m sending you down to the cells."
                                                        hide brandon_smirk
                                                        self "Dammit..."
                                                        show screen grand_screen_2_jail
                
                                                        show bg_jail
                                                        with fade
                                                        jump choice15_done
                                                        label choice15_done:

                                                            narrator """Can I get out of it?

                                                            Getting caught was never the plan but I can always try to get out of it. The questioning is starting.

                                                            I need to decide what is priority. To escape? Find Izek?"""
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
                                                                                    hide izek_neutral

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
                                                                                    self "What’s happening? Where are you taking me now... "
                                                                                    show soldier
                                                                                    soldierA "The commander wants to see you. "
                                                                                    hide soldier
                                                                                    self "The commander?...It’s you. How?"
                                                                                    show izek_neutral
                                                                                    ian "The rest of you can leave. It seems like we have some reconnecting to do, right?"
                                                                                    self "Izek..! You’re okay... And alive?"
                                                                                    ian "As you can see, I am more than okay. So, tell me, how did you end up here... my lover?"
                                                                                    self "You’re the commander now, the leader of the Solara military?"
                                                                                    hide izek_neutral
                                                                                    show screen grand_screen_3

                                                                                    jump choice3_lover
                                                                                    
                                                                                    
                                                                    jump choice2_done


                                                                #CHOICE2
                                                                "Act clueless":
                                                                    jump choice2_no
                                                                    label choice2_no:
                                                                        show soldier
                                                                        soldierA "Do you realise what those documents are?"
                                                                        hide soldier
                                                                        self "Oh, these? I thought they were just routine reports. Am I not supposed to have them?"
                                                                        show soldier
                                                                        soldierA"Routine reports? You expect us to believe you just stumbled upon classified material by accident?"
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
                                                                                    show screen grand_screen_2
                                                                                jump choice2p2
                                                                                label choice212_done:

                                                                            "Deflect questions":
                                                                                jump choice212_no
                                                                                label choice212_no:
                                                                                    self "I’m new here, remember? I was just doing some filing and grabbed the wrong stack. Honest mistake. I didn’t even get a chance to look at what’s inside."
                                                                                    show soldier
                                                                                    soldierA "You had better hope that’s true. We don’t take security breaches lightly."
                                                                                    hide soldier
                                                                                    self "Security breach? I swear, it was just a mix-up. I wouldn’t know what to do with classified documents if they fell in my lap!"
                                                                                    show soldier 
                                                                                    soldierA "You’re on thin ice. Make sure this doesn’t happen again."
                                                                                    hide soldier
                                                                                    self "Absolutely. I’ll be more careful. Thank you for understanding."
                                                                                    thoughts "{i}That was close but they’re going to keep a closer eye on me now.{\i}"
                                                                                    show screen grand_screen_2
                                                                                jump choice2p2

                                                                    jump choice2_done

                                                    #CHOICE15
                                                    "Bribe him":
                                                        jump choice15_no
                                                        label choice15_no:
                                                        self "Can’t you let me off? I was just curious about what this was all about."
                                                        show brandon_neutral
                                                        brandon "Why did you need to know? "
                                                        hide brandon_neutral
                                                        self "I’m new here, and honestly, a bit of an overachiever. I just wanted to be prepared. Please, just this once, let it slide. I’ll make it worth your while—Celestium, as much as you want. Name your price."
                                                        show brandon_neutral
                                                        brandon "Alright, I’ll let it go. This’ll help my family… but it’s going to cost you."
                                                        hide brandon_neutral
                                                        self "Okay so 50 Celestium anytime? "
                                                        show brandon_neutral
                                                        with vpunch
                                                        brandon "You got yourself a deal."
                                                        brandon "You’re playing a dangerous game, Alia. But maybe I can be persuaded... this time. Just remember, I’m not as easy to sway as you might think. If you get caught again, you’re on your own."
                                                        hide brandon_neutral
                                                        thoughts """{i}That was a close call.

                                                        I got away this time but why the heck did I offer 50 Celestium, anytime? This is going to cost me big time. Dammit.

                                                        Now where’s the training room?{\i}"""
                                                        show screen grand_screen_2
                                                        jump choice2p2

                                            #CHOICE14
                                            "Erase coordinates":
                                                jump choice14_no
                                                label choice14_no:
                                                $ menu_flag = False
                                                self "Wait, these seem to be the only copies they have. I could just erase the coordinates."
                                                narrator "Door opens."
                                                play sound "audio/Door Open.mp3" volume 0.8
                                                show brandon_neutral
                                                with hpunch
                                                brandon "What are you doing here? Aren’t you a trainee? You’re not authorised to be in here."
                                                hide brandon_neutral
                                                self "Oh, I did not know."
                                                show brandon_neutral
                                                brandon "Mind you trainee, only a higher personnel like myself and your sergeant majors could enter in here and not the likes of you. So.. how did you get in here?"
                                                hide brandon_neutral
                                                self "I was looking around and I got lost. I was trying to find the training room. I did not mean to cause trouble."
                                                show brandon_neutral
                                                brandon "Don’t come in here unless you were told to again. The Combat Simulation Chamber is right around the corner. Now, go your training is about to start."
                                                hide brandon_neutral
                                                show screen grand_screen_2

                                                jump choice2p2
                                                label choice14_done:
                            

                            #CHOICE13
                            "Ignore plans":
                                jump choice13_no
                                label choice13_no:
                                    $ menu_flag = False
                                    self "It’s too risky to do anything now. I’ll have to report back what I saw. Maybe I could come back here again. I need to go to the training room now."
                                    #narrator "You weren't caught"
                                    jump choice2p2
                                    show screen grand_screen_2

                        jump choice2_done
                        label choice2_done:
                            
                #CHOICE12
                "Find Training Room":
                    show bg_training_rm_blur
                    with fade
                    jump choice12_no
                    label choice12_no:
                        $ menu_flag = False
                        self "Combat Simulation Chamber? Hmm.. Ahhh so this is the training room."
                        
                        jump choice2p2
                        label choice2p2:
                        show screen grand_screen_2
                        show bg_training_rm_blur
                        with fade

                        #CHOICE2PATH2
                        stop music fadeout 1.0
                        play music "audio/Galactic Rap.mp3" volume 0.5 loop

                        narrator """The Training. Start of Act 2 (Path 2)
                        
                        Should I build or burn bridges? I need to choose wisely and most importantly, never lose sight of my mission.
                        
                        As training begins, I’ll have to face decisions about whether to manipulate others or build alliances.

                        I meet Jay, the weakest link in the group, and I might need to rely on my roommate, Zander, to progress.

                        Alternatively, I can try to succeed on my own.
    
                        But is that the best choice?"""
                        self "So, this is the training room.  Dammit, I got to do this all over again. I hate this."
                        menu:
                            "Burn bridges":
                                jump choice22_yes
                                label choice22_yes:
                                
                                self """Let’s get through this quickly.

                                So, we have to climb the ranks? It might be faster if I work alone.

                                Hmm... If only there was a way to slip past some of these obstacles.

                                If I can find a way to undermine the others, especially the weaker ones like Jay, it could speed up my progress.
                                
                                I’ll need to be careful, though—subtlety is key."""
                                play sound "audio/Fighting.mp3" volume 0.8 
                                with Pause (0.8) 
                                self "Yes! I made him slip."
                                show soldier
                                faceless "Did you see that? What is happening?"
                                hide soldier
                                self "Huh, this is good. Everyone’s is getting nervous. It’s time to end this."
                                show soldier
                                soldierA "Trainee Alia has completed her training. Good job, trainee."
                                hide soldier
                                self "Thanks."
                                self "{i}I’ve got some time to spare, maybe it’s a good opportunity to take a look around.{\i}"
                                self "{i}I should gather as much information as possible while the others are distracted.{\i}"


                                show bg_meeting_rm_blur
                                with fade

                                self "This looks interesting."
                                "{i}Damn.. I knew it was too good to be true. {\i}"

                                #TODO if condition
                                #if player stole documents in act 1,
                                show brandon_neutral
                                brandon "Ha... It’s you again. What are you doing here? You’re not authorised to be in here."
                                self """Oh, I did not know. 
                                
                                I was looking around and I got lost. I did not mean to cause trouble."""
                                brandon "That excuse is not gonna work on me the second time."
                                hide brandon_neutral
                                show brandon_smirk
                                brandon """And you didn’t want to cause trouble but you sneak out of training? And then decide to enter a restricted area, {i}again{\i}?
    
                                Let’s go. You’re going to the cell today."""
                                narrator "{i}Shoot.{\i}"
                                hide brandon_smirk
                                #TODO jump to act 3 general route

                                #TODO if condition
                                #if player stole documents in act 1,

                                show brandon_neutral

                                brandon """What are you doing here? Aren’t you a trainee?

                                You’re not authorised to be in here."""
                                self "Oh, I did not know."
                                brandon "These are top secret information. How did you get in here?"
                                self "I was looking around and I got lost. I did not mean to cause trouble."
                                brandon "So you didn’t want to cause trouble but you sneak out of training? And then decide to enter a restricted area?"
                                hide brandon_neutral
                                show brandon_slightsmile
                                brandon "Let’s go. You’re going to the cell today."
                                thoughts "{i}Shoot.{\i}"
                                hide brandon_slightsmile

                                #TODO jump to act 3 general route
                                #TODO update menu below
                                show screen grand_screen_3

                                jump choice3_start
                                label choice22_done:
                                    
                                menu: 
                                    
                                    "The Confrontation":
                                        stop music fadeout 1.0
                                        play music "audio/Beauty Flow.mp3" volume 0.5 loop
                                        show screen grand_screen_3
                                        jump choice3_start
                                        label choice3_start:
                                        narrator "Finally, the truth is laid bare in front of me. But, is he the same person? Can he be trusted?"
                                        #TODO update node below
                                        self "What’s happening? Where are you taking me now? "
                                        show soldier
                                        soldierA "Commander Ian, please excuse my leave."

                                        #SFX DOOR CLOSE
                                        self "Ize.. "
                                        self "I mean Ian. What are you doing here? This can’t be true... You’re the commander now?"
                                        hide soldier
                                        show izek_neutral
                                        ian " I am.. How did you end up here?"

                                        
                                        
                                        jump choice3_general
                                        label choice3_general:

                                        self "I can’t believe you would do this.. You really betrayed us? You betrayed Gaiarise?"
                                        izek """I did no such thing. I still stand with Gaiarise. But the plan changed. 

                                        The people of Solara don’t deserve what’s coming. They need help... and I have a plan to root out the corruption."""
                                        self "...and what? You’re telling me you’re not corrupted yourself? After everything?"
                                        izek """Do you really think I would betray my home planet? Betray you?

                                        I’m doing this to save them. To save Gaiarise.

                                        I have a plan, a way to tear down the corrupt system from within."""
                                        self "And you want me to believe you after all this?"
                                        izek """Yes. I need you to believe me.

                                        Now that I know you’re here, you can help. Together, we can make this right.

                                        Please, Alia. Trust me."""
                                        
                                        #calculated trust point determines, need to research
                                        menu:
                                            #High score of trust points
                                            "Believe him":
                                                jump choice31_yes
                                                label choice31_yes:
                                                    self "Okay, I’ll hear you out. You won’t betray us, right?"
                                                    izek "I would never do that to you. You know that."
                                                    self "What do you need me to do?"
                                                    izek """Send a message back to the command base.

                                                    Tell them about me—about what’s really going on here. Let them know Solara is corrupted, but we’re taking it down from the inside.
                                                    
                                                    The people here need our help, not our wrath."""
                                                    
                                                    izek """Contact Astralis and Lunara as well. Make sure they’re aware of the situation.

                                                    Tell them we’ll return what was taken and rebuild the damage caused by previous conflicts.
                                                    
                                                    We need to unite to fix this—together. We can turn this whole situation around."""

                                                    show planetboth
                                                    narrator """Deciding to work with him, I send covert messages back to the command base, sharing details of Izek and the current state of Solara.

                                                    With Izek’s lead, he carried out a revolution with the Solaraian military and took down the corrupted regime.

                                                    Solara is rebuilding and mending its relationship with the planets they have wronged before. And with the newfound support of Gaiarise, an alliance was formed.

                                                    This is the start of a new beginning for Solara. 

                                                    After all is well, Izek and I explore old feelings and our happily ever after is just beginning."""
                                                    narrator "{i}Spread love, not war.{\i}"
                                                    #TODO jump to finish
                                                    jump choice31_done
                                                    label choice31_done:
                                            #Low score of trust points
                                            "Do not believe him":
                                                jump choice31_no
                                                label choice31_no:
                                                self "I can’t believe this, Izek!"
                                                izek "Listen, it’s not what you think... I wouldn’t betray you or Gaiarise. Please, just hear me out—"
                                                self """You really think I’ll listen to you after all this? I can’t risk it, Ian.

                                                I will not give up Gaiarise... not even for you.

                                                I’m sorry. I have to signal the siege."""
                                                izek "Wait..!"
                                                narrator "Izek pauses and then nods slowly."
                                                izek """Do it. It’s okay.

                                                I know it’s going to be harder to convince them now, but I will never blame you. Do what you have to do."""
                                                show izek_slightsmile
                                                izek "Just... please stay safe, Alia."

                                                show planetboth

                                                narrator """While all is well for Gaiarise, it has been revealed how corrupted the government of Solara is.

                                                The siege might have been a saving grace for the people but it was going to take a longer time for Gaiarise and the people Solara to get along. 

                                                As for Izek, his loyalty is still a question. However, he never blamed me for his current situation.

                                                He know it’s going to take a lot of convincing and evidence to prove his allegiance to Gaiarise. 

                                                Due to high tensions, both of us were never able to share our feelings for one another.

                                                With the stakes high, I am not willing to risk my planet, my home, even for the man I love."""
                                                narrator "Was it the right choice?"
                                                jump choice31_done
                                                jump choice3_lover

                            "Build bridges":
                                jump choice22_no
                                label choice22_no:
                                    thoughts """{i}Let’s get through this quickly. So, we have to climb the ranks?

                                    Maybe it’s smarter to work with the others... My roommate, Zander, and Jay? {\i}"""
                                    show soldier
                                    show zander_neutral
                                    self "Do you guys want to work together?"
                                    jay "That would be a great help. I’ve been struggling to keep up on my own."
                                    show zander_slightsmile
                                    zander "Sure, why not? Could be interesting to see how we handle this as a team."
                                    self "Great. Let’s get this training over and done with, then."

                                    #TODO fade in out to black

                                    narrator "During training,"
                                    jay "You know, it’s kinda bone-chilling when you think about the fact that people have died here..."
                                    self "What? People died here? In training? Isn’t it just... training?"
                                    zander """Did you guys hear about that one guy? Pretty sure he died during this training.

                                    Word is, he was climbing the ranks too fast, and some folks didn’t like it."""
                                    self "Who was it? It can’t be that serious... right?"
                                    zander """Apparently he was making waves, moving up faster than the others.

                                    Then, during combat training, something went wrong—a freak accident, they say.
    
                                    But who knows?

                                    Some people here play dirty when they feel threatened."""
                                    jay "Makes you wonder if we should be more careful... or more ruthless."

                                    menu:
                                        "Ask about when it happened":
                                            jump choice221_yes
                                            label choice221_yes:
                                                self "When was this?"
                                                show zander_neutral
                                                zander "It was 3-4 years ago..? It was right before I got in, really."
                                                jay "I mean there were rumours that there people trying to cover up the whole thing"
                                                zander """Yeah, I remember something about that. Saw some big meeting happening among the leaders at the holo-conferencing room.

                                                I almost got into trouble for poking around there."""
                                                self  "Huh, interesting..."
                                                self "Anyway, that’s enough. Let’s get through this fast so that we could get a break."
                                                #TODO fade in out to black

                                                soldierA "Trainee Alia, Trainee Zander, Trainee Jay, training is completed. Good job, trainees."
                                                jump choice221_done
                                                label choice221_done:
                                                    menu: 
                                                        "Sneak away":
                                                            jump choice222_yes
                                                            label choice222_yes:

                                                            self "We got time to spare. Maybe I should sneak away."
                                                            #TODO jump to next node

                                                            jump choice222_done
                                                        
                                                        "Stay with them":
                                                            jump choice222_no
                                                            label choice222_no:
                                                
                                                                play sound "audio/Annoucement.mp3" volume 1
                                                                announcer "Attention trainees! Please report to the training grounds for the Annual Solara Trainee Sparring."
                                                                soldierC """Welcome, trainees, to the Annual Solara Trainee Sparring.

                                                                Attendance is mandatory. The rules are simple: fight until only one remains standing.

                                                                The winner will earn the opportunity to lead our upcoming mission alongside our First Commander."""

                                                                zander "No one’s ever met the First Commander. But a whole mission? This might be interesting."
                                                                jay "Yeah... I’m not even going to try. You guys go ahead. I’ll be here watching."
                                                                self "Well, looks like this will be a breeze. Let’s give my all then!"
                                                                
                                                                #TODO fade in out to black

                                                                narrator "One final fight-"
                                                                narrator """As Zander hits the ground, the impact echoes throughout the arena. I wince.

                                                                I need to focus. I can’t afford any distractions now.

                                                                Finally, the quarter-finals are over, and Zander is out. Only one more opponent stands between me and victory.

                                                                While I continue fighting on, the First Commander was lurking in the shadows unbeknownst to me."""
                                                                
                                                                show izek_neutral
                                                                izek """I detest attending these kind of events but let’s see what the trainees got.

                                                                Last two standing, finally. Hmm... That fighting style..! It’s so familiar.

                                                                It reminds me of my times back in Gaiarise. Could it be... {i}her{\i}? What is she doing here? 

                                                                I want that trainee’s documents. Send them to my office, {i}now{\i}."""
                                                                soldierB "Yes, sir. Will she be going for the mission? "
                                                                show izek_slightsmile
                                                                izek """Yes. I can already tell she’s going to win...

                                                                {i}I taught her, after all.{\i}

                                                                Send her to my office once it’s over. I’ll go through the mission details with her personally."""
                                                                
                                                                                                                                #will create a menu to link back to "Calls her into the office under the disguise sharing information of the mission."
                                                                    
                                                                jump choice222_done
                                                                label choice222_done:
                                        "Ask how he looked like":
                                            jump choice221_no
                                            label choice221_no:
                                                self "What did he look like?"
                                                show zander_neutral
                                                zander """Some said he had dark hair, others swore he was blonde.

                                                Honestly, we don’t really know. The story’s been passed down so much, it’s hard to say what’s accurate anymore."""
                                                jay "You’re really into this huh.."
                                                self "I mean, yeah. Somebody died?! That’s not exactly something you just brush off."
                                                jay "But yeah, it’s not surprising the government did nothing about it. That’s just how things work around here."
                                                zander "I bet they kept the higher up silent about it too."
                                                self "Why do you say that?"
                                                jay "I mean, don’t you know? Our government doesn’t care about its people. We’re just cogs in the machine to them."
                                                self """Oh, right, right... But you know, for being such a hater... why are you even here?
                                                You’re not exactly, err... soldier material? No offence."""
                                                jay "I have to. For my family. You understand, right?."
                                                self "Yeah, I get it. We all have our reasons."
                                                self "Anyway, that’s enough. Let’s get through this."
                                                soldierA "Trainee Alia, Trainee Zander, Trainee Jay, training is completed. Good job, trainees."

                                                jump choice222_no
                        jump choice2_done


    "Make friends":
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
            zander """So, here’s the Neural Lounge— it’s our version of a break room. You can decompress and clear your mind from a tough mission here.

            Over there, we have the Holo-Conferencing Room. That’s where we sync commands across the galaxy in real-time."""
            hide zander_neutral
            self "Impressive... What’s next?"
            show zander_neutral
            zander "Now, we’re heading to the Combat Simulation Chamber. It’s where you’ll be training."
            hide zander_neutral
            self "Cool... So, is training tough? "
            show zander_neutral
            zander """Let’s just say, the Simulation Chamber adapts to your skill level.

            You’ll be facing everything from basic drills to full-scale virtual invasions.

            But don’t worry—you’re going to find out soon enough"""
            hide zander_neutral
            show screen grand_screen_2

        jump choice2p2

            
return

menu:
    "The Confrontation":
        jump choice3_lover
        label choice3_lover:  
        stop music fadeout 1.0
        play music "audio/Beauty Flow.mp3" volume 0.5 loop
        show screen grand_screen_3
        narrator "Finally, the truth is laid bare in front of me. But, is he the same person? Can he be trusted?"
        #TODO update node below
        self "What’s happening? Where are you taking me now? "
        show soldier
        soldierA "Commander Ian, please excuse my leave."

        #SFX DOOR CLOSE
        self "Ize.. "
        self "I mean Ian. What are you doing here? This can’t be true... You’re the commander now?"
        hide soldier
        show izek_neutral
        ian " I am.. How did you end up here?" 
        menu:
            "Reveal plans":
                jump choice311_yes
                label choice311_yes:
                    self "If you remember me, then you would know I came to find you"
                    show izek_slightsmile
                    izek "I could never forget you. But is that all there is?"
                    self "I came to find you, to get you out of Solara! You don’t belong here, Izek!"

                    jump choice3_general

            "Ask questions":
                jump choice311_no
                label choice311_no:
                    show izek_neutral
                    self "What happened to you? I thought you were dead?"
                    show izek_slightsmile
                    izek "I’m not dead but I have seen better days. It took awhile but I became the leader of Solara’s military."
                    hide izek_neutral
                jump choice311_done
                label choice311_done:
                    menu:
                        "Show frustration":
                            jump choice3111_yes
                            label choice3111_yes:
                                self "Everyone has been worried about you ever since your contact got cut but it seems like I was worried sick for nothing."
                                self "Glad to know this was all just a waste of time."
                                izek "Good to know you still care, my lover."
                                self "I can’t believe you. You would do this... after everything?"
                                #link to the nodes
                            jump choice31_no
                            label choice3111_done:
            
                        "Show concern":
                            jump choice3111_no
                            label choice3111_no:
                                self "Are you okay? I  haven’t heard from you for so long...Are you hurt?"
                                show izek_neutral
                                izek "I’ve been better...Glad to know you still care about me.. Oh wait.. we’re lovers right"
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
    
            
jump choice3_lover_done
label choice3_lover_done:

    


