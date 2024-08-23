# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:41:35 2020

@author: Anneloes Hulsman (anneloes_hulsman@hotmail.com)
"""
# Import libraries
import expyriment


# Global settings
#------------------------------------------------------------------------------
exp = expyriment.design.Experiment(name="Fearful Avoidance Task Practice") # create new experiment
expyriment.control.initialize(exp) # initialize experiment
exp.add_data_variable_names(["trial", "taskversion", "reward", "threat", "response", "rt", "outcome", "reward_amount", "exp_outcome", "dur_anticipation", "dur_ITI"])


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
instruction_vA_vid = "../Stimuli/" + "InstructionVideo_vA.mp4"
instruction_vB_vid = "../Stimuli/" + "InstructionVideo_vB.mp4"
#loud_noise = "../Stimuli/" + "loud_noise.wav"
#soft_noise = "../Stimuli/" + "soft_noise.wav"
    

# Create stimuli: Fearful Avoidance Task
#------------------------------------------------------------------------------
# Instruction video
stim_instruction_vA = expyriment.stimuli.Video(instruction_vA_vid)
stim_instruction_vB = expyriment.stimuli.Video(instruction_vB_vid)

# Text ready?
text_ready = expyriment.stimuli.TextScreen("",text="Indien u geen vragen heeft, kunt u op het pijltje naar boven of beneden drukken om de oefenrondes te starten. Let op: de oefenrondes starten meteen.",text_size=30,text_colour=(85,85,85),position=(0,0))

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

# Audio: no audio during practice
#stim_soft_noise = expyriment.stimuli.Audio(soft_noise)
#stim_loud_noise = expyriment.stimuli.Audio(loud_noise)


# Preload all stimuli: Fearful Avoidance Task
#------------------------------------------------------------------------------    
scalefactor=(.8,.8) 
# Instruction video
stim_instruction_vA.preload()
stim_instruction_vB.preload()
text_ready.preload()
              
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
#stim_soft_noise.preload()
#stim_loud_noise.preload()


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
    
       

# Design
#------------------------------------------------------------------------------
# Create design (blocks and trials)
# Create stimuli (and put them into trials)
# Create input/output devices (like button boxes etc.)

#for blocks in ["block one", "block two"]:
block = expyriment.design.Block("block_practice") # currently one block
    
for trialtypes in ["LRLT", "LRHT", "HRLT", "HRHT"]: # for each trial type
    trial = expyriment.design.Trial() # create trials
    trial.set_factor("trialtypes", trialtypes) 
    block.add_trial(trial, copies=1) # add trial to block (for 'real task' 5 copies, for practice 1)
block.shuffle_trials(max_repetitions=3) # shuffle trials: max. 3 reps of the same trial type
exp.add_block(block) # add block to experiment
       
expyriment.control.start(skip_ready_screen=True)
expyriment.control.start_audiosystem()

c_trials = 1 # trial counter
    
for block in exp.blocks:
    if exp.subject % 2 == 0 : # if the subject number is EVEN
        stim_instruction_vA.play() # play instruction video version A
        stim_instruction_vA.present()
        video_presentation_time = exp.clock.time
        stim_instruction_vA.wait_end()
        stim_instruction_vA.stop
        text_ready.present() # after the instructions, ask whether the participant is ready to continue to the practice trials
        key,rt = exp.keyboard.wait(keys=responsekey)
        
    elif exp.subject % 2 == 1 : # if the subject number is ODD
        stim_instruction_vB.play() # play instruction video version B
        stim_instruction_vB.present()
        video_presentation_time = exp.clock.time
        stim_instruction_vB.wait_end()
        stim_instruction_vB.stop        
        text_ready.present() # after the instructions, ask whether the participant is ready to continue to the practice trials
        key,rt = exp.keyboard.wait(keys=responsekey)
        
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
        #if threat == "lowthreat":
        #    trial.add_stimulus(stim_soft_noise)
        #elif threat == "highthreat":
        #    trial.add_stimulus(stim_loud_noise)


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
                    #trial.stimuli[6].present() # play white noise
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
                    #trial.stimuli[6].present()
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
            #trial.stimuli[6].present() # play white noise
            exp.clock.wait(dur_outcome)    
        
        # Present ITI
        #------------------------------------------#            
        fixcross.present()
        exp.clock.wait(dur_ITI)


        if outcome == "money" and reward == "lowreward":
            reward_amount = 0.10
        elif outcome == "money" and reward == "highreward":
            reward_amount = 0.50  
        else:
            reward_amount = 0
              
        # OUTPUT FEARFUL AVOIDANCE TASK
        exp.data.add([c_trials, taskversion, reward, threat, response, rt, outcome, reward_amount, exp_outcome, dur_anticipation, dur_ITI])
        c_trials = c_trials + 1

expyriment.control.end()