# abit by type
# abit by cl4ss
# some unholy combination thereof
# inventory random
# loot pool random
# magic loot pool
# type based descriptions
# naming convention
# descriptions


import random
from math import ceil
from tkinter import *
import os
level = 0
counter = 0
rarit = ''
cl4ss = ''
cwd = os.getcwd()
new_string = cwd + '\monster_repository.txt'
damage_index = ['acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning', 'necrotic', 'piercing', 'poison', 'psychic', 'celestial', 'slashing', 'thunder',]
element_index = ['acid', 'cold', 'fire', 'force', 'lightning', 'necrotic', 'poison', 'psychic', 'celestial', 'thunder',]
condition_index = ['blinded', 'charmed', 'deafened', 'frightened', 'grappled', 'incapacitated', 'invisible', 'paralyzed', 'petrified', 'poisoned', 'prone', 'restrained', 'stunned', 'unconcious', 'exhaustion']
limb_index = ['hand', 'foot', 'leg', 'arm', 'head', 'torso', 'mouth', 'finger', 'toe', 'tail', 'wing', 'forearm', 'calf', 'upper arm', 'thigh', 'eye', 'ear', 'nose', 'throat']
state_of_wear_index = ['resplendent', 'tarnished', 'well worn', 'well maintained', 'recently damaged', 'exotic', 'colorful', 'draped', 'decorative', 'expensive', 'intimidating', 'imposing', 'better than yours', 'inoperable']
terrain_index = ['']
movement_index = ['']
being_modifier_index = ['pregnant', 'young', 'old', 'adult', 'sick', 'diseased', 'mutated', 'corrupted', 'blind', 'dying', 'agressive', 'kind', 'crippled', 'fused', 'two headed', 'three headed', 'hydra headed', 'tail', 'ethereal', 'six limbs', 'eight limbs', 'mortally wounded', 'dumb', 'deaf', 'hungry', 'undead', 'angelic']
humans_index = ['man', 'woman', 'herme']
animals_index = ['alligator', 'crocodile', 'reptilian', 'draconic', 'turtle', 'tortise', 'lion', 'cat', 'dog', 'wolf', 'hyena', 'elephant', 'hippo', 'hawk', 'eagle', 'mouse', 'tiger', 'horse']
senses_index = ['smell', 'sight', 'hearing', 'touch', 'taste']
senses_exotic_index = ['otherworldly' 'true', 'empathetic', 'tremor', 'blind', 'echolocation', 'superior']
sense_descriptor_mundane_index = ['keen', 'dulled'] # 'dark', might consider this. meaning superior in the dark.
damage = random.choice(damage_index)
element = random.choice(element_index)
condition = random.choice(condition_index)
limb1, limb2, limb3, limb4, limb5, limb6, limb7, limb8 = random.choices(limb_index, k = 8)
state_of_wear = random.choice(state_of_wear_index)
mythical_inspiration = [random.choice(humans_index), random.choice(animals_index), random.choice(being_modifier_index)]


ind_ability_vision = [f'{random.choice(sense_descriptor_mundane_index)} {random.choice(senses_index)}']
ind_ability_vision_exotic = ["Telepathy", "Devil's Sight", "Eye of the Law", "Detect Life", "Detect Death", "Detect Undeath", "Speak with Dead", "Speak with Plants", "Speak with Animals", "Treasure Sense", "Labrynthine Recall", f'{random.choice(senses_exotic_index)}', f'{random.choice(senses_exotic_index)}', f'{random.choice(senses_index)}']
ind_ability_movement = ["Flight", "Swim", "Burrow", "Climb", "Tunneler", "Earth Glide", "Aggressive", "Flyby", "Spider Climb", "Stone Step", "Water Walk", "Cloud Perch", "Gaseous Form", f"{element} Form", "Amorphous", "Incorporeal", "Shadow Step", "Planar Jaunt", "Teleportation", "Wild Teleportation"]     
ind_ability_tier_5 = ["Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", f'{element} weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_4 = ["Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Frightful Presence", f"Apply {condition}", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", f'{element} Element', f'{element} Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_3 = ["Magic Resistance", "Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Frightful Presence", f"Apply {condition}", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", f'{condition} Immunity', f'{condition} Resistance', f'{condition} Presence', f'{condition} Gaze', f'{damage} Resistance', f'{damage} Immunity', f'{element} Element', f'{element} Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_2 = ["Antimagic Cone", "Magic Resistance", "Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Frightful Presence", f"Apply {condition}", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", f'{condition} Immunity', f'{condition} Resistance', f'{condition} Presence', f'{condition} Gaze', f'{damage} Resistance', f'{damage} Immunity', f'{element} Element', f'{element} Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_1 = [f'{condition} Immunity', f'{condition} Resistance', f'{condition} Presence', f'{condition} Gaze', f'{damage} Resistance', f'{damage} Immunity', f'{element} Element', f'{element} Weapons', "Antimagic Cone", "Magic Resistance", "Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Apply {condition}", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_types = ["aberration", "beast", "celestial", "construct", "dragon", "elemental", "fey", "fiend", "giant", "humanoid", "monstrosity", "ooze", "plant", "undead"]
ind_rarit = ['common', 'uncommon', 'rare']
ind_cl4ss = ["arcanist", "frontliner", "tank", "sniper", "minion"]
ind_size = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan']
ind_cosmetic = ['Weapons from the Body', 'Covered in Mold, Fungus or Mushrooms', 'Maggots Crawl', 'Infested', 'Acidic Slimy Trail', 'Hallucinations', 'Mandibles', f'Scythe {limb1}']
aberration_cosmetic = []
beast_cosmetic = []
celestial_cosmetic = []
construct_cosmetic = []
dragon_cosmetic = []
elemental_cosmetic = []
fey_cosmetic = []
fiend_cosmetic = []
giant_cosmetic = []
humanoid_cosmetic = []
monstrosity_cosmetic = []
ooze_cosmetic = []
plant_cosmetic = []
undead_cosmetic = []


print('''
      This is the Monster Maker, monsters will be returned to a new text document.
      The first prompt is mode. Enter random to generate random monsters automatically.
      Enter anything else to input parameters manually.
      Monster Level is an integer between 1 and 20.
      Monster Rarity is Common, Uncommon or Rare.
      Monster Class is Arcanist, Frontliner, Tank, Sniper or Minion.
      Monster type can be Aberration, Beast, Celestial, Construct, Dragon, Elemental, Fey, Fiend, Giant, Humanoid, Monstrosity, Ooze, Plant or Undead.
      You can input random for any of these parameters.
      If you want to end the program, type 'end' when prompted.
      If you don't wish to end the program, input anything other than the word end. Case is not sensitive.
      ''')


def set_vars():
    return random.randint(1,20), random.choice(ind_rarit), random.choice(ind_cl4ss), random.sample(ind_types, k=2)


def set_stats(x, y, z):
    match x: # x is level variable
        case 1:
            dmg = 4
        case 2:
            dmg = 5
        case 3:
            dmg = 6
        case 4:
            dmg = 8
        case 5:
            dmg = 10
        case 6:
            dmg = 12
        case 7:
            dmg = 14
        case 8:
            dmg = 16
        case 9:
            dmg = 18
        case 10:
            dmg = 20
            dc = 18
        case 11:
            dmg = 22
            dc = 19
        case 12:
            dmg = 24
            dc = 20
        case 13:
            dmg = 26
            dc = 21
        case 14:
            dmg = 28
            dc = 22
        case 15:
            dmg = 30
            dc = 23
        case 16:
            dmg = 32
            dc = 24
        case 17:
            ac = 16
            dmg = 34
            dc = 25
        case 18:
            ac = 16
            dmg = 36
            dc = 26
        case 19:
            ac = 17
            dmg = 38
            dc = 27
        case 20:
            ac = 17
            dmg = 40
            dc = 28
    hp = x * 5
    atk = ceil(x / 2) + 3
    if x < 9:
        ac = 13
    if x < 13:
        ac = 14
    if x < 17:
        ac = 15
    if x < 10:
        dc = ceil(x / 2) + 12
    senses = random.choice(ind_ability_vision)
    senses_exotic = random.choice(ind_ability_vision_exotic)
    movement = random.choice(ind_ability_movement)
    match y.lower(): # y is rarit variable
        case "common":
            hp *= 0.7
            ac -= 1
            dmg *= 0.5
            dc -= 1
        case "uncommon":
            pass
        case "rare":
            atk *= 2
            dmg *= 1.75
            dc += 1
            movement = random.sample(ind_ability_movement, k=2)
    hp = ceil(hp)
    ac = ceil(ac)
    atk = ceil(atk)
    dmg = ceil(dmg)
    dc = ceil(dc)
    match z.lower(): # z is cl4ss variable
        case "arcanist":
            hp *= 0.75
            ac -= 2
        case "frontliner":
            hp *= 1.2
            ac += 1
            atk += 1
        case "tank":
            hp *= 1.5
            ac += 3
        case "sniper":
            hp *= 0.9
            atk += 1
            dmg *= 2
        case "minion":
            hp = 1
            ac = 10
            atk +=1
            dmg += 2
            dc = 12
    hp = ceil(hp)
    ac = ceil(ac)
    atk = ceil(atk)
    dmg = ceil(dmg)
    dc = ceil(dc)
    if x < 5:
        tier = 5
        tier_ability = random.sample(ind_ability_tier_5, k=2)
    elif x < 9:
        tier = 4
        tier_ability = random.sample(ind_ability_tier_4, k=3)
    elif x < 13:
        tier = 3
        tier_ability = random.sample(ind_ability_tier_3, k=4)
    elif x < 17:
        tier = 4
        tier_ability = random.sample(ind_ability_tier_2, k=5)
    elif x < 21:
        tier = 1
        tier_ability = random.sample(ind_ability_tier_1, k=6)
    return hp, ac, atk, dmg, dc, senses, senses_exotic, movement, tier, tier_ability


def call_random():
    while counter < 10:
        level, rarit, cl4ss, types = set_vars()
        cosmetic = random.sample(ind_cosmetic, k=2)
        size = random.choice(ind_size)
        hp, ac, atk, dmg, dc, senses, senses_exotic, movement, tier, tier_ability = set_stats(level, rarit, cl4ss)
        with open(f"{new_string}", "a") as f:
            write_var = f'''
            Level {level} {rarit} {cl4ss}
            
            hp {hp} ac {ac} atk {atk} dmg {dmg} dc {dc}
            
            {senses} {senses_exotic} {movement}
            
            {tier_ability}
            
            {types}
            
            {size}
            
            {cosmetic}
            
            tier {tier}
            '''
            f.write(write_var)
        counter_control()


def call_manual():
    level = input("Monster Level: ")
    rarit = input("Monster Rarity: ")
    cl4ss = input("Monster Class: ")
    types = input("Monster Type: ")
    if level.lower() == "random":
        level = random.randint(1,20)
    else:
        level = int(level)
    if rarit.lower() == "random":
        rarit = random.choice(ind_rarit)
    if cl4ss.lower() == "random":
        cl4ss = random.choice(ind_cl4ss)
    if types.lower() == "random":
        types = random.sample(ind_types, k=2)
        # all the lines prior to this determine the input variables
    cosmetic = random.sample(ind_cosmetic, k=2)
    size = random.choice(ind_size)
    hp, ac, atk, dmg, dc, senses, senses_exotic, movement, tier, tier_ability = set_stats(level, rarit, cl4ss)
        # the prior two line set all of our stats
    with open("f{new_string}", "a") as wf:
        write_var = f'''
        Level {level} {rarit} {cl4ss}
        
        hp {hp} ac {ac} atk {atk} dmg {dmg} dc {dc}
        
        {senses} {senses_exotic} {movement}
        
        {tier_ability}
        
        {types}
        
        {size}
        
        {cosmetic}
        
        tier {tier}
        '''
        wf.write(write_var)
        print(write_var)


def counter_control():
    global counter
    counter += 1
    print(counter)


def call_program():
    run = True
    while run == True:
        mode = input()
        match mode.lower():
            case 'random':
                global counter
                counter = 0
                call_random()
            case 'manual':
                call_manual()
            case 'end':
                run = False


call_program()


# our program works until we are dones
# we have every attribute in play, up to basic implementation
# what else do we want
# post the current version on github?
# give it one more read
# have this install itself in a known folder?







# root = Tk()

# randomButton = Button(root, text="random", command=call_random, fg="#ffffff", bg="#000000", padx=10)

# manualButton = Button(root, text="manual", command=call_manual, fg="#ffffff", bg="#000000", padx=10)
# root.mainloop()

# randomButton.grid(row=0, column=0)
# manualButton.grid(row=0, column=1)
