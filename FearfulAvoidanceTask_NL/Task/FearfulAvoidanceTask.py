# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:41:35 2020

@author: Anneloes Hulsman (anneloes_hulsman@hotmail.com)
"""
# Import libraries
import expyriment


# Global settings
#------------------------------------------------------------------------------
exp = expyriment.design.Experiment(name="Fearful Avoidance Task") # create new experiment
expyriment.control.initialize(exp) # initialize experiment
exp.add_data_variable_names(["trial", "taskversion", "reward", "threat", "response", "rt", "outcome", "reward_amount", "exp_outcome", "dur_anticipation", "dur_ITI", "total_reward", "total_shoot"])


# Define stimuli: get images from files
#------------------------------------------------------------------------------
# Images: avatar handback, avatar shoot, avatar money, background
background1_im = "../Stimuli/" + "Background1.png"
#background2_im = "../Stimuli/" + "Background2.png"
avatar1_handback_im = "../Stimuli/" + "Avatar1_handback.png"
avatar1_shoot_im = "../Stimuli/" + "Avatar1_shoot.png"
avatar1_money_im = "../Stimuli/" + "Avatar1_money.png"
avatar2_handback_im = "../Stimuli/" + "Avatar2_handback.png"
avatar2_shoot_im = "../Stimuli/" + "Avatar2_shoot.png"
avatar2_money_im = "../Stimuli/" + "Avatar2_money.png"
loud_noise = "../Stimuli/" + "loud_noise.wav"
soft_noise = "../Stimuli/" + "soft_noise.wav"
    

# Create stimuli: Fearful Avoidance Task
#------------------------------------------------------------------------------
# Backgrounds
stim_background1 = expyriment.stimuli.Picture(background1_im)
#stim_background2 = expyriment.stimuli.Picture(background2_im)
    
# Avatar: handback
stim_avatar_handback1 = expyriment.stimuli.Picture(avatar1_handback_im)
stim_avatar_handback2 = expyriment.stimuli.Picture(avatar2_handback_im)
        
# Avatar: money
stim_avatar_money1 = expyriment.stimuli.Picture(avatar1_money_im)
stim_avatar_money2 = expyriment.stimuli.Picture(avatar2_money_im)
        
# Avatar: shoot
stim_avatar_shoot1 = expyriment.stimuli.Picture(avatar1_shoot_im)
stim_avatar_shoot2 = expyriment.stimuli.Picture(avatar2_shoot_im)

# Text: respond, money
text_respond = expyriment.stimuli.TextLine(text="Reageer",text_size=64,text_colour=(0,0,0),position=(0,-20), background_colour=(85,85,85))
text_lowreward = expyriment.stimuli.TextLine(text="\u20ac0.10",text_size=64,text_colour=(0,0,0),position=(0,-200), background_colour=(85,85,85))
text_highreward = expyriment.stimuli.TextLine(text="\u20ac0.50",text_size=64,text_colour=(0,0,0),position=(0,-200), background_colour=(85,85,85))
  
# Fixation cross
fixcross = expyriment.stimuli.FixCross()

# Audio
stim_soft_noise = expyriment.stimuli.Audio(soft_noise)
stim_loud_noise = expyriment.stimuli.Audio(loud_noise)

text_r = "hoi"

# Text ready 
text_ready_start = expyriment.stimuli.TextScreen("",text=text_r, text_size=30,text_colour=(255,255,255),position=(0,0))

# Create stimuli: Subjective rating scale
#------------------------------------------------------------------------------
# Create bar
barLength = 500
barThick = 10
posBar=(0,-100)
bar = expyriment.stimuli.Rectangle((barLength,barThick),corner_rounding=None,position=posBar)
barEndLeft = expyriment.stimuli.Rectangle((5,barThick*3),position=((-(barLength+2)/2), posBar[1]))
barEndRight = expyriment.stimuli.Rectangle((5,barThick*3),position=(((barLength+2)/2), posBar[1]))

# Create text stimuli
text0 = expyriment.stimuli.TextLine(text="0",text_size=30,text_colour=(85,85,85),position=(-250,-150))
text1 = expyriment.stimuli.TextLine(text="1",text_size=30,text_colour=(85,85,85),position=(-200,-150))
text2 = expyriment.stimuli.TextLine(text="2",text_size=30,text_colour=(85,85,85),position=(-150,-150))
text3 = expyriment.stimuli.TextLine(text="3",text_size=30,text_colour=(85,85,85),position=(-100,-150))
text4 = expyriment.stimuli.TextLine(text="4",text_size=30,text_colour=(85,85,85),position=(-50,-150))
text5 = expyriment.stimuli.TextLine(text="5",text_size=30,text_colour=(85,85,85),position=(0,-150))
text6 = expyriment.stimuli.TextLine(text="6",text_size=30,text_colour=(85,85,85),position=(50,-150))
text7 = expyriment.stimuli.TextLine(text="7",text_size=30,text_colour=(85,85,85),position=(100,-150))
text8 = expyriment.stimuli.TextLine(text="8",text_size=30,text_colour=(85,85,85),position=(150,-150))
text9 = expyriment.stimuli.TextLine(text="9",text_size=30,text_colour=(85,85,85),position=(200,-150))
text10 = expyriment.stimuli.TextLine(text="10",text_size=30,text_colour=(85,85,85),position=(250,-150))
text_verymuch = expyriment.stimuli.TextLine(text="Heel erg",text_size=30,text_colour=(85,85,85),position=(250,-180))
text_notatall = expyriment.stimuli.TextLine(text="Helemaal niet",text_size=30,text_colour=(85,85,85),position=(-250,-180))
text_instruction = expyriment.stimuli.TextScreen("",text="Beweeg de cursor met het linker en rechter pijltje van het toetsenbord, bevestig uw keuze met ENTER",text_size=18,text_colour=(85,85,85),position=(0,-250))
text_lowreward_sq = expyriment.stimuli.TextLine(text="\u20ac0.10",text_size=30,text_colour=(0,0,0),position=(0,0), background_colour=(85,85,85))
text_highreward_sq = expyriment.stimuli.TextLine(text="\u20ac0.50",text_size=30,text_colour=(0,0,0),position=(0,0), background_colour=(85,85,85))

text_val_LT = expyriment.stimuli.TextScreen("",text="Hoe vervelend vond u het zachte geluid?",text_size=30,text_colour=(85,85,85),position=(0,50))
text_val_HT = expyriment.stimuli.TextScreen("",text="Hoe vervelend vond u het harde geluid?",text_size=30,text_colour=(85,85,85),position=(0,50))
text_val_LR = expyriment.stimuli.TextScreen("",text="Hoe plezierig vond u de beloning van \u20ac0.10?",text_size=30,text_colour=(85,85,85),position=(0,50))
text_val_HR = expyriment.stimuli.TextScreen("",text="Hoe plezierig vond u de beloning van \u20ac0.50?",text_size=30,text_colour=(85,85,85),position=(0,50))

text_expectancy_negative = expyriment.stimuli.TextScreen("",text="In hoeverre verwachtte u een NEGATIEVE uitkomst wanneer u bij het onderstaande poppetje ervoor koos om te benaderen?",text_size=30,text_colour=(85,85,85),position=(0,100))
text_expectancy_positive = expyriment.stimuli.TextScreen("",text="In hoeverre verwachtte u een POSITIEVE uitkomst wanneer u bij het onderstaande poppetje ervoor koos om te benaderen?",text_size=30,text_colour=(85,85,85),position=(0,100))

text_notext = expyriment.stimuli.TextLine(text="",text_size=30,text_colour=(85,85,85),position=(0,0))
text_nopicture = expyriment.stimuli.TextLine(text="",text_size=30,text_colour=(85,85,85),position=(0,50))

# Avatar: handback
stim_avatar_handback1_sq = expyriment.stimuli.Picture(avatar1_handback_im, position=(0,150))
stim_avatar_handback2_sq = expyriment.stimuli.Picture(avatar2_handback_im, position=(0,150))

# Preload all stimuli: Fearful Avoidance Task
#------------------------------------------------------------------------------    
scalefactor=(.8,.8) 
               
# Backgrounds
stim_background1.scale(scalefactor)
stim_background1.preload()
#stim_background2.scale(scalefactor)
#stim_background2.preload()
            
# Avatars: handback
stim_avatar_handback1.scale(scalefactor)
stim_avatar_handback1.preload()
stim_avatar_handback2.scale(scalefactor)
stim_avatar_handback2.preload()   
        
            
# Avatar: money 
stim_avatar_money1.scale(scalefactor) 
stim_avatar_money1.preload()
stim_avatar_money2.scale(scalefactor) 
stim_avatar_money2.preload()
    
# Avatar: shoot (negative)
stim_avatar_shoot1.scale(scalefactor) # negative outcome (shoot)
stim_avatar_shoot1.preload()
stim_avatar_shoot2.scale(scalefactor) # negative outcome (shoot)
stim_avatar_shoot2.preload() 

# Text respond, money
text_respond.preload()
text_lowreward.preload()
text_highreward.preload()  
         
# Fixation cross (ITI)
fixcross.preload()

# Audio
stim_soft_noise.preload()
stim_loud_noise.preload()

# Outcome overview
composition_outcomeoverview = expyriment.stimuli.BlankScreen()

# Text ready
text_ready_start.preload()

# Preload all stimuli: Subjective rating scale
#------------------------------------------------------------------------------    
scalefactor_sq=(.2,.2) 
                      
# Avatars: handback
stim_avatar_handback1_sq.scale(scalefactor_sq)
stim_avatar_handback1_sq.preload()
stim_avatar_handback2_sq.scale(scalefactor_sq)
stim_avatar_handback2_sq.preload()   

bar.preload()
barEndLeft.preload()
barEndRight.preload()
text0.preload()
text1.preload()
text2.preload()
text3.preload()
text4.preload()
text5.preload()
text6.preload()
text7.preload()
text8.preload()
text9.preload()
text10.preload()
text_notatall.preload()
text_verymuch.preload()
text_instruction.preload()
text_lowreward_sq.preload()
text_highreward_sq.preload()
text_val_LT.preload()
text_val_HT.preload()
text_val_LR.preload()
text_val_HR.preload()
text_expectancy_negative.preload()
text_expectancy_positive.preload()
text_notext.preload()
text_nopicture.preload()


# Define responses
#------------------------------------------------------------------------------
keys = expyriment.io.Keyboard()
keys.set_quit_key(expyriment.misc.constants.K_ESCAPE) # quit with ESC 
responsekey=[expyriment.misc.constants.K_UP,
             expyriment.misc.constants.K_DOWN] # UP = approach, DOWN = avoid
experimenterkey=expyriment.misc.constants.K_5 # participant cannot accidently press space and continue
     

# Define functions      
#------------------------------------------------------------------------------
# When presenting stimuli on top of each other you need to present it twice
def doublepresent(stim,clear,update):
    # Twice for double buffering
    stim.present(clear=clear,update=update)
    stim.present(clear=clear,update=update)
    
# Slider
posSlider = (0,posBar[1]) # initial position of the slider

# Sliding function
def sliding(pos,commit):
    while commit==0: # when the subject did not press 'enter' to confirm yet
        # create a composition to show multiple elements at the same time
        composition = expyriment.stimuli.BlankScreen()
        bar.plot(composition)
        barEndLeft.plot(composition)
        barEndRight.plot(composition)
        text_question.plot(composition)
        picture.plot(composition)
        text_reward.plot(composition)
        text0.plot(composition)
        text1.plot(composition)
        text2.plot(composition)
        text3.plot(composition)
        text4.plot(composition)
        text5.plot(composition)
        text6.plot(composition)
        text7.plot(composition)
        text8.plot(composition)
        text9.plot(composition)
        text10.plot(composition)
        text_verymuch.plot(composition)
        text_notatall.plot(composition)
        text_verymuch.plot(composition)
        text_instruction.plot(composition)
        slider = expyriment.stimuli.Rectangle((3,30),position=pos, colour = (194, 24, 7))
        slider.plot(composition)
        composition.present()
        # participants can use left and right arrow to adjust slider position & commit with enter
        key, rt = exp.keyboard.wait(process_control_events=True)
        if key == 13:
            commit = 1 # when the subject pressed 'enter' to confirm choice
            return pos[0]
        elif key == 275: # right
            pos = (pos[0]+50, pos[1])
            if pos[0] > barLength/2: # fixes upper end of the scale
                pos = (barLength/2,pos[1])
        elif key == 276: # left
            pos = (pos[0]-50, pos[1])
            if pos[0] < -barLength/2: # fixes lower end of the scale
                pos = (-barLength/2,pos[1])
        

# Design
#------------------------------------------------------------------------------
# Create design (blocks and trials)
# Create stimuli (and put them into trials)
# Create input/output devices (like button boxes etc.)

#for blocks in ["block one", "block two"]:
block = expyriment.design.Block("block_one") # currently one block
    
for trialtypes in ["LRLT", "LRHT", "HRLT", "HRHT"]: # for each trial type
    trial = expyriment.design.Trial() # create trials
    trial.set_factor("trialtypes", trialtypes) 
    block.add_trial(trial, copies=10) # add trial to block (5 per trial type = 5 min task, 10 per trial type = 8 min task)
block.shuffle_trials(max_repetitions=3) # shuffle trials: max. 3 reps of the same trial type
exp.add_block(block) # add block to experiment
       
expyriment.control.start(skip_ready_screen=True)
expyriment.control.stop_audiosystem()
expyriment.control.start_audiosystem()



## CODE FOR INSTRUCTIONS ##

total_reward = 0 # total reward counter
total_shoot = 0 # total shoot counter
c_trials = 1 # trial counter
    
text_ready_start.present() # after the instructions, ask whether the participant is ready to continue to the practice trials
key,rt = exp.keyboard.wait(keys=responsekey)

for block in exp.blocks:
    for trial in block.trials:
                            
        # Determine trial type   
        #------------------------------------------#
        if trial.get_factor("trialtypes") == "LRLT":
            reward = "lowreward"        
            threat = "lowthreat"
        elif trial.get_factor("trialtypes") == "LRHT":
            reward = "lowreward"
            threat = "highthreat"
        elif trial.get_factor("trialtypes") == "HRLT":
            reward = "highreward"
            threat = "lowthreat"
        elif trial.get_factor("trialtypes") == "HRHT":
            reward = "highreward" 
            threat = "highthreat"      
        
        
        # Add stimuli to trial
        #------------------------------------------#
        # stim 0: background
        trial.add_stimulus(stim_background1) 

        # stim 1: reward level
        if reward == "lowreward":
            trial.add_stimulus(text_lowreward)
        elif reward == "highreward":
            trial.add_stimulus(text_highreward)
        
        # IF THE SUBJECT NUMBER IS EVEN
        if exp.subject % 2 == 0 : # if the subject number is EVEN
            taskversion = 'A'
            # stim 2: avatar handback
            if threat == "lowthreat":
                trial.add_stimulus(stim_avatar_handback1)
            elif threat == "highthreat":
                trial.add_stimulus(stim_avatar_handback2)
            
            # stim 3: avatar money
            if threat == "lowthreat":
                trial.add_stimulus(stim_avatar_money1)
            elif threat == "highthreat":
                trial.add_stimulus(stim_avatar_money2)
            
            # stim 4: avatar shoot 
            if threat == "lowthreat":
                trial.add_stimulus(stim_avatar_shoot1)
            elif threat == "highthreat":
                trial.add_stimulus(stim_avatar_shoot2)
                
        # IF THE SUBJECT NUMBER IS ODD
        elif exp.subject % 2 == 1 : # if the subject number is ODD
            taskversion = 'B'
            if threat == "lowthreat":
                trial.add_stimulus(stim_avatar_handback2)
            elif threat == "highthreat":
                trial.add_stimulus(stim_avatar_handback1)
            
            # stim 3: avatar money
            if threat == "lowthreat":
                trial.add_stimulus(stim_avatar_money2)
            elif threat == "highthreat":
                trial.add_stimulus(stim_avatar_money1)
            
            # stim 4: avatar shoot 
            if threat == "lowthreat":
                trial.add_stimulus(stim_avatar_shoot2)
            elif threat == "highthreat":
                trial.add_stimulus(stim_avatar_shoot1)    
                
        # stim 5: text respond            
        trial.add_stimulus(text_respond) 
        
        # stim 6: white noise (soft/loud)
        if threat == "lowthreat":
            trial.add_stimulus(stim_soft_noise)
        elif threat == "highthreat":
            trial.add_stimulus(stim_loud_noise)


        # Determine duration of anticipation, ITI...
        #------------------------------------------#
        dur_anticipation = expyriment.design.randomize.rand_int(3000,5000)
        dur_outcome = 2000
        dur_ITI = expyriment.design.randomize.rand_int(5000,6000)         
        
        
        # Present background + avatar (anticipation)
        #------------------------------------------#
        doublepresent(trial.stimuli[0],True,True) # background 
        doublepresent(trial.stimuli[2],False,True) # avatar handback
        doublepresent(trial.stimuli[1],False,True) # text reward
        exp.clock.wait(dur_anticipation)
          
        
        # Present background + avatar (respond)
        #------------------------------------------#
        doublepresent(trial.stimuli[0],True,True) # background
        doublepresent(trial.stimuli[2],False,True) # avatar handback
        doublepresent(trial.stimuli[1],False,True) # text reward
        doublepresent(trial.stimuli[5],False,True) # respond text
        key,rt = exp.keyboard.wait(keys=responsekey, duration=1000)
                   
        # Determine whether the subject receives a predictable outcome (i.e.
        # positive/negative outcome when approach, neutral outcome when avoid) or
        # unpredictable outcome (i.e. neutral outcome when approach, positive/negative
        # outcome when avoid)        
        #------------------------------------------#          
        
        luck = expyriment.design.randomize.rand_norm(0,1) 
        predictable = expyriment.design.randomize.rand_norm(0,1) 
     
        
        # Present background + outcome
        #------------------------------------------#
        if key == responsekey[0]: # if the subject approached  
            response = 'approach'
            if predictable < 0.80: # ... and receives predictable outcome
                exp_outcome = 'expected' # LOG: outcome expected/unexpected
                if luck < 0.50: # ... and has NO luck
                    outcome = 'shoot' # LOG: outcome shoot/money/neutral
                    doublepresent(trial.stimuli[0],True,True) # background
                    doublepresent(trial.stimuli[4],False,True) # avatar shoot
                    trial.stimuli[6].present() # play white noise
                    exp.clock.wait(dur_outcome)
                else: # ... and has luck
                    outcome = 'money' # LOG: outcome shoot/money/neutral
                    doublepresent(trial.stimuli[0],True,True) # background
                    doublepresent(trial.stimuli[3],False,True) # avatar money
                    doublepresent(trial.stimuli[1],False,True) # reward level
                    exp.clock.wait(dur_outcome)
            else: # ... and receives an unpredictable outcome
                exp_outcome = 'unexpected' # LOG: outcome expected/unexpected
                doublepresent(trial.stimuli[0],True,True) # background
                doublepresent(trial.stimuli[2],False,True) # avatar handback
                exp.clock.wait(dur_outcome) 
                                      
        elif key == responsekey[1]: # if the subject avoided
            response = 'avoid'
            if predictable < 0.80: # ... and receives predictable outcome
                   exp_outcome = 'expected' # LOG: outcome expected
                   outcome = 'neutral' # LOG: outcome shoot/money/neutral
                   doublepresent(trial.stimuli[0],True,True) # background
                   doublepresent(trial.stimuli[2],False,True) # avatar handback
                   exp.clock.wait(dur_outcome)
            else: # ... and receives an unpredictable outcome
                   exp_outcome = 'unexpected'# LOG: outcome unexpected
                   if luck < 0.50: # ... and has NO luck 
                    outcome = 'shoot' # LOG: outcome shoot/money/neutral
                    doublepresent(trial.stimuli[0],True,True) # background
                    doublepresent(trial.stimuli[4],False,True) # avatar shoot
                    trial.stimuli[6].present()
                    exp.clock.wait(dur_outcome)
                   else: # ... and has luck
                    outcome = 'money' # LOG: outcome shoot/money/neutral
                    doublepresent(trial.stimuli[0],True,True) # background
                    doublepresent(trial.stimuli[3],False,True) # avatar money
                    doublepresent(trial.stimuli[1],False,True) # reward level
                    exp.clock.wait(dur_outcome)
                            
        else: # if subject did not respond in time
            response = 'no_response' 
            outcome = 'None'
            exp_outcome = 'None'
            doublepresent(trial.stimuli[0],True,True) # background
            doublepresent(trial.stimuli[4],False,True) # avatar shoot
            trial.stimuli[6].present() # play white noise
            exp.clock.wait(dur_outcome)   
             
        # Present ITI
        #------------------------------------------#            
        fixcross.present()
        exp.clock.wait(dur_ITI)
        
        # Calculate the total amount of money that the participant received  
        #------------------------------------------#
        if outcome == "money" and reward == "lowreward":
            reward_amount = 0.10
        elif outcome == "money" and reward == "highreward":
            reward_amount = 0.50  
        else:
            reward_amount = 0
        
        total_reward = total_reward + reward_amount
        
        # Calculate the total amount of shots that the avatar fired
        #------------------------------------------#
        if outcome == "shoot" or outcome == "None":
            total_shoot = total_shoot + 1
                    
        # For every trial, the output is written in the output file
        #------------------------------------------#
        exp.data.add([c_trials, taskversion, reward, threat, response, rt, outcome, reward_amount, exp_outcome, dur_anticipation, dur_ITI, total_reward, total_shoot])
        c_trials = c_trials + 1
    
    # At the end of the FAT, feedback is given regarding the amount of money that the participant received and the amount of shots that the avatar fired
    #------------------------------------------#
    text_outcome = expyriment.stimuli.TextScreen("", text="De totale beloning die u heeft ontvangen is €" + str(total_reward) + ". De avatar heeft in totaal " + str(total_shoot) + " keer geschoten. Druk op het pijltje naar boven of beneden om door te gaan naar de vragen over de taak.", text_size=30,text_colour=(85,85,85),position=(0,0))
    text_outcome.plot(composition_outcomeoverview)                        
    composition_outcomeoverview.present()
    key,rt = exp.keyboard.wait(keys=responsekey)
    
exp.data.add(["##########"]) # separate output from fearful avoidance task and subjective questions
exp.data.add(["Subjective questions"]) # separate output from fearful avoidance task and subjective questions

# Subjective Questions
#------------------------------------------#
for subjective_question in range (1,9):
    if subjective_question == 1: 
        text_question = text_val_LT # 1 question: unpleasant soft noise
        text_reward = text_notext
        picture = text_nopicture
        
    elif subjective_question == 2:
        text_question = text_val_HT # 2 question: unpleasant loud noise
        text_reward = text_notext
        picture = text_nopicture
        
    elif subjective_question == 3:
        text_question = text_val_LR # 3 question: pleasant low reward
        text_reward = text_notext
        picture = text_nopicture
        
    elif subjective_question == 4:
        text_question = text_val_HR # 4 question: pleasant high reward
        text_reward = text_notext
        picture = text_nopicture
        
    elif subjective_question == 5:
        text_question = text_expectancy_negative # 5 question: expectancy negative outcome low threat
        text_reward = text_notext      
        if exp.subject % 2 == 0: # if the subject number is EVEN
            picture = stim_avatar_handback1_sq
        elif exp.subject % 2 == 1 : # if the subject number is ODD
            picture = stim_avatar_handback2_sq
    
    elif subjective_question == 6:
        text_question = text_expectancy_negative # 6 question: expectancy negative outcome high threat
        text_reward = text_notext    
        if exp.subject % 2 == 0: # if the subject number is EVEN
            picture = stim_avatar_handback2_sq
        elif exp.subject % 2 == 1 : # if the subject number is ODD
            picture = stim_avatar_handback1_sq
    
    elif subjective_question == 7:
        text_question = text_expectancy_positive # 9 question: expectancy positive low threat
        text_reward = text_notext     
        if exp.subject % 2 == 0: # if the subject number is EVEN
            picture = stim_avatar_handback1_sq
        elif exp.subject % 2 == 1 : # if the subject number is ODD
            picture = stim_avatar_handback2_sq
    
    elif subjective_question == 8:
        text_question = text_expectancy_positive # 10 question: expectancy positive high threat
        text_reward = text_notext      
        if exp.subject % 2 == 0: # if the subject number is EVEN
            picture = stim_avatar_handback2_sq
        elif exp.subject % 2 == 1 : # if the subject number is ODD
            picture = stim_avatar_handback1_sq
    
                    
    sliding(posSlider, posSlider) # calls the function 'slider'
    SubjectiveRating = ((sliding(posSlider,0)-(-barLength/2))/50) # calculates the subjective rating
    exp.data.add([subjective_question, SubjectiveRating]) # prints the number of the question and the rating


expyriment.control.end()