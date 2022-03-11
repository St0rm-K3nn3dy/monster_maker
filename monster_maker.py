# abit by type
# abit by class
# some unholy combination thereof
# inventory random
# loot pool random
# magic loot pool
# type based descriptions
#
#
# naming convention
# descriptions

import random
var_level = 0
end_program_var = ''
damage_index = ['Acid', 'Bludgeoning', 'Cold', 'Fire', 'Force', 'Lightning', 'Necrotic', 'Piercing', 'Poison', 'Psychic', 'Celestial', 'Slashing', 'Thunder',]
element_index = ['Acid', 'Cold', 'Fire', 'Force', 'Lightning', 'Necrotic', 'Poison', 'Psychic', 'Celestial', 'Thunder',]
condition_index = ['Blinded', 'Charmed', 'Deafened', 'Frightened', 'Grappled', 'Incapacitated', 'Invisible', 'Paralyzed', 'Petrified', 'Poisoned', 'Prone', 'Restrained', 'Stunned', 'Unconcious', 'Exhaustion']
limb_index = ['Hand', 'Foot', 'Leg', 'Arm', 'Head', 'Torso', 'Mouth', 'Finger', 'Toe', 'Tail', 'Wing', 'Forearm', 'Calf', 'Upper Arm', 'Thigh', 'Eye', 'Ear', 'Nose', 'Throat']
state_of_wear_index = ['Resplendent', 'Tarnished', 'Well Worn', 'Well Maintained', 'Recently Damaged', 'Exotic', 'Colorful', 'Draped', 'Decorative', 'Expensive', 'Intimidating', 'Imposing', 'Better Than Yours', 'Inoperable']
ind_ability_vision = ["Darkvision", "Superior Darkvision", "Keen Smell", "Keen Sight", "Keen Ears", "Keen Touch", "Keen Taste", "Blindsight", "Tremor Sense", "Echolocation"]
ind_ability_vision_exotic = ["Otherworldly Perception", "Telepathy", "True Sight", "Devil's Sight", "Eye of the Law", "Detect Life", "Detect Death", "Detect Undeath", "Speak with Dead", "Speak with Plants", "Speak with Animals", "Treasure Sense", "Labrynthine Recall"]
ind_ability_movement = ["Flight", "Swim", "Burrow", "Climb", "Tunneler", "Earth Glide", "Aggressive", "Flyby", "Spider Climb", "Stone Step", "Water Walk", "Cloud Perch", "Gaseous Form", "Elemental Form", "Amorphous", "Incorporeal", "Shadow Step", "Planar Jaunt", "Teleportation", "Wild Teleportation"]     
ind_ability_tier_5 = ["Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", 'Acid Weapons', 'Cold Weapons', 'Fire Weapons', 'Force Weapons', 'Lightning Weapons', 'Necrotic Weapons', 'Poison Weapons', 'Psychic Weapons', 'Celestial Weapons', 'Thunder Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_4 = ["Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Frightful Presence", "Apply Condition", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", '{element} Element', '{element} Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_3 = ["Magic Resistance", "Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Frightful Presence", "Apply Condition", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", '{condition} Immunity', '{condition} Resistance', '{condition} Presence', '{condition} Gaze', '{damage} Resistance', '{damage} Immunity', '{element} Element', '{element} Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_2 = ["Antimagic Cone", "Magic Resistance", "Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Frightful Presence", "Apply Condition", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", '{condition} Immunity', '{condition} Resistance', '{condition} Presence', '{condition} Gaze', '{damage} Resistance', '{damage} Immunity', '{element} Element', '{element} Weapons', 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_ability_tier_1 = ['{condition} Immunity', '{condition} Resistance', '{condition} Presence', '{condition} Gaze', '{damage} Resistance', '{damage} Immunity', '{element} Element', '{element} Weapons', "Antimagic Cone", "Magic Resistance", "Multiattack", "Spellcasting", "Regeneration", "Magic Weapons", "Apply Condition", "Reckless", "Rust Cloak", "Petrifying Gaze", "Action Surge", "Parry", "Second Wind", "Unyielding Fortitude", "Chain Strikes", "Surprise Attack", "Burst Extra Attack", "Pact Tactics", "Spectral Duplicate", "Death Throes", "Spellcasting", 'Reverse Amalgamation', 'Splitting Ooze', 'Swarm Mother', 'Brood Mare', 'Spawner', 'Nightmares', 'Nausea', 'Environmental Ally', 'Reflection Stride', 'Integrated Armor', 'Auto Cannibalization', 'Disadvantage on Incoming Attacks', 'Vacuum Chamber', 'Amalgamation', 'Second Form', 'Independent Limbs', 'Mounted', 'Mount', 'Tentacles', '1d4 Extra Arms', 'Planar Split Presence']
ind_types = ["Aberration", "Beast", "Celestial", "Construct", "Dragon", "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead"]
ind_rarit = ['common', 'uncommon', 'rare']
ind_class = ["arcanist", "frontliner", "tank", "sniper", "minion"]
ind_size = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan']
ind_cosmetic = ['Weapons from the Body', 'Covered in Mold, Fungus or Mushrooms', 'Maggots Crawl', 'Infested', 'Acidic Slimy Trail', 'Hallucinations', 'Mandibles', 'Scythe Limbs']
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
damage = random.choice(damage_index)
element = random.choice(element_index)
condition = random.choice(condition_index)
limb1, limb2, limb3, limb4, limb5, limb6, limb7, limb8 = random.choices(limb_index, k = 8)
state_of_wear = random.choice(state_of_wear_index)


print('''
      This is the Monster Maker, monsters will be returned to a new text document.
      The first prompt is mode. Enter random to generate random monsters automatically.
      Enter anything else to input parameters manually.
      Monster Level is an integer between 1 and 20.
      Monster Rarity is common, uncommon or rare.
      Monster Class is Arcanist, Frontliner, Tank, Sniper or Minion.
      Monster type can be Aberration, Beast, Celestial, Construct, Dragon, Elemental, Fey, Fiend, Giant, Humanoid, Monstrosity, Ooze, Plant, Undead.
      You can select random for any of these parameters. Use lowercase.
      If you want to end the program, type 'end' when prompted.
      If you don't wish to end the program, input anything other than the word end. Case is not sensitive.
      ''')


while end_program_var.lower() != 'end' or '3nd':
    var_2 = input('Mode: ')
    var_counter = 0
    while var_2.lower() == "random" and var_counter < 1000:
        var_level = random.randint(1,20)
        var_rarit = random.choice(ind_rarit)
        var_class = random.choice(ind_class)
        var_types = random.sample(ind_types, k=2)
        var_cosmetic = random.choices(ind_cosmetic, k=2)
        var_size = random.choice(ind_size)
        hp = var_level * 5
        ac= 0
        atk = 0
        dmg = 0
        dc = 0
        var_ability = 0
        match var_level:
            case 1:
                ac = 13
                atk = 4
                dmg = 4
                dc = 13
                var_ability = 1
            case 2:
                ac = 13
                atk = 4
                dmg = 4
                dc = 14
                var_ability = 1
            case 3:
                ac = 13
                atk = 5
                dmg = 6
                dc = 14
                var_ability = 2
            case 4:
                ac = 13
                atk = 5
                dmg = 8
                dc = 14
                var_ability = 2
            case 5:
                ac = 13
                atk = 6
                dmg = 10
                dc = 15
                var_ability = 3
            case 6:
                ac = 13
                atk = 6
                dmg = 12
                dc = 15
                var_ability = 3
            case 7:
                ac = 13
                atk = 7
                dmg = 14
                dc = 16
                var_ability = 4
            case 8:
                ac = 13
                atk = 7
                dmg = 16
                dc = 16
                var_ability = 4
            case 9:
                ac = 14
                atk = 8
                dmg = 18
                dc = 17
                var_ability = 5
            case 10:
                ac = 14
                atk = 8
                dmg = 20
                dc = 18
                var_ability = 5
            case 11:
                ac = 14
                atk = 9
                dmg = 22
                dc = 19
                var_ability = 6
            case 12:
                ac = 14
                atk = 9
                dmg = 24
                dc = 20
                var_ability = 6
            case 13:
                ac = 15
                atk = 10
                dmg = 26
                dc = 21
                var_ability = 7
            case 14:
                ac = 15
                atk = 10
                dmg = 28
                dc = 22
                var_ability = 7
            case 15:
                ac = 15
                atk = 11
                dmg = 30
                dc = 23
                var_ability = 8
            case 16:
                ac = 15
                atk = 11
                dmg = 32
                dc = 24
                var_ability = 8
            case 17:
                ac = 16
                atk = 12
                dmg = 34
                dc = 25
                var_ability = 9
            case 18:
                ac = 16
                atk = 12
                dmg = 36
                dc = 26
                var_ability = 9
            case 19:
                ac = 17
                atk = 13
                dmg = 38
                dc = 27
                var_ability = 10
            case 20:
                ac = 17
                atk = 13
                dmg = 40
                dc = 28
                var_ability = 10
        match var_rarit.lower():
            case "common":
                hp *= 0.7
                ac -= 1
                dmg *= 0.5
                dc -= 1
                var_senses = random.choice(ind_ability_vision)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "uncommon":
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "rare":
                atk *= 2
                dmg *= 1.75
                dc += 1
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choices(ind_ability_movement, k=2)
        match var_class.lower():
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
        if var_level < 5:
            tier = 5
            var_tier_ability = random.sample(ind_ability_tier_5, k=2)
        elif var_level < 9:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_4, k=3)
        elif var_level < 13:
            tier = 3
            var_tier_ability = random.sample(ind_ability_tier_3, k=4)
        elif var_level < 17:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_2, k=5)
        elif var_level < 21:
            tier = 1
            var_tier_ability = random.sample(ind_ability_tier_1, k=6)
        with open("monster_repository.txt", "a") as f:
            f.write(f"\n Level {var_level} {var_rarit} {var_class} \n hp {hp} ac {ac} atk {atk} dmg {dmg} dc {dc} \n {var_senses} {var_senses_exotic} \n {var_movement} \n {var_tier_ability} \n {var_types} \n 'tier' {tier}")
        var_counter += 1
        print(var_counter)
    else:
        var_level = input("Monster Level: ")
        var_rarit = input("Monster Rarity: ")
        var_class = input("Monster Class: ")
        var_types = input("Monster Type: ")
        if var_level.lower() != "random":
            var_level_int = int(var_level)
            var_level = var_level_int
        if var_level == "random":
            var_level = random.randint(1,20)
        if var_rarit.lower() == "random":
            var_rarit = random.choice(ind_rarit)
        if var_class.lower() == "random":
            var_class = random.choice(ind_class)
        if var_types.lower() == "random":
            var_types = random.sample(ind_types, k=2)
        var_cosmetic = random.choices(ind_cosmetic, k=2)
        var_size = random.choice(ind_size)
        hp = var_level * 5
        ac= 0
        atk = 0
        dmg = 0
        dc = 0
        var_ability = 0
        match var_level:
            case 1:
                ac = 13
                atk = 4
                dmg = 4
                dc = 13
                var_ability = 1
            case 2:
                ac = 13
                atk = 4
                dmg = 4
                dc = 14
                var_ability = 1
            case 3:
                ac = 13
                atk = 5
                dmg = 6
                dc = 14
                var_ability = 2
            case 4:
                ac = 13
                atk = 5
                dmg = 8
                dc = 14
                var_ability = 2
            case 5:
                ac = 13
                atk = 6
                dmg = 10
                dc = 15
                var_ability = 3
            case 6:
                ac = 13
                atk = 6
                dmg = 12
                dc = 15
                var_ability = 3
            case 7:
                ac = 13
                atk = 7
                dmg = 14
                dc = 16
                var_ability = 4
            case 8:
                ac = 13
                atk = 7
                dmg = 16
                dc = 16
                var_ability = 4
            case 9:
                ac = 14
                atk = 8
                dmg = 18
                dc = 17
                var_ability = 5
            case 10:
                ac = 14
                atk = 8
                dmg = 20
                dc = 18
                var_ability = 5
            case 11:
                ac = 14
                atk = 9
                dmg = 22
                dc = 19
                var_ability = 6
            case 12:
                ac = 14
                atk = 9
                dmg = 24
                dc = 20
                var_ability = 6
            case 13:
                ac = 15
                atk = 10
                dmg = 26
                dc = 21
                var_ability = 7
            case 14:
                ac = 15
                atk = 10
                dmg = 28
                dc = 22
                var_ability = 7
            case 15:
                ac = 15
                atk = 11
                dmg = 30
                dc = 23
                var_ability = 8
            case 16:
                ac = 15
                atk = 11
                dmg = 32
                dc = 24
                var_ability = 8
            case 17:
                ac = 16
                atk = 12
                dmg = 34
                dc = 25
                var_ability = 9
            case 18:
                ac = 16
                atk = 12
                dmg = 36
                dc = 26
                var_ability = 9
            case 19:
                ac = 17
                atk = 13
                dmg = 38
                dc = 27
                var_ability = 10
            case 20:
                ac = 17
                atk = 13
                dmg = 40
                dc = 28
                var_ability = 10
        match var_rarit.lower():
            case "common":
                hp *= 0.7
                ac -= 1
                dmg *= 0.5
                dc -= 1
                var_senses = random.choice(ind_ability_vision)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "uncommon":
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "rare":
                atk *= 2
                dmg *= 1.75
                dc += 1
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choices(ind_ability_movement, k=2)
        match var_class.lower():
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
        if var_level < 5:
            tier = 5
            var_tier_ability = random.sample(ind_ability_tier_5, k=2)
        elif var_level < 9:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_4, k=3)
        elif var_level < 13:
            tier = 3
            var_tier_ability = random.sample(ind_ability_tier_3, k=4)
        elif var_level < 17:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_2, k=5)
        elif var_level < 21:
            tier = 1
            var_tier_ability = random.sample(ind_ability_tier_1, k=6)
        print("Level", var_level, var_rarit, var_class)
        print("hp:", hp, "ac:", ac, "atk:", atk, "dmg:", dmg, "dc:", dc)
        print("number of abilities:", var_ability)
        print(var_senses, ",", var_senses_exotic, ",", var_movement)
        print(var_tier_ability)
        print(var_types)
        print("tier", tier)
        with open("monster_repository.txt", "a") as f:
            f.write(f"\n Level {var_level} {var_rarit} {var_class} \n hp {hp} ac {ac} atk {atk} dmg {dmg} dc {dc} \n {var_senses} {var_senses_exotic} \n {var_movement} \n {var_tier_ability} \n {var_types} \n 'tier' {tier}")
        end_program_var = input("End Program? ")
    var_2 = input('Mode: ')
    var_counter = 0
    while var_2.lower() == "random" and var_counter < 1000:
        var_level = random.randint(1,20)
        var_rarit = random.choice(ind_rarit)
        var_class = random.choice(ind_class)
        var_types = random.choices(ind_types, k=2)
        var_cosmetic = random.choices(ind_cosmetic, k=2)
        var_size = random.choice(ind_size)
        hp = var_level * 5
        ac= 0
        atk = 0
        dmg = 0
        dc = 0
        var_ability = 0
        match var_level:
            case 1:
                ac = 13
                atk = 4
                dmg = 4
                dc = 13
                var_ability = 1
            case 2:
                ac = 13
                atk = 4
                dmg = 4
                dc = 14
                var_ability = 1
            case 3:
                ac = 13
                atk = 5
                dmg = 6
                dc = 14
                var_ability = 2
            case 4:
                ac = 13
                atk = 5
                dmg = 8
                dc = 14
                var_ability = 2
            case 5:
                ac = 13
                atk = 6
                dmg = 10
                dc = 15
                var_ability = 3
            case 6:
                ac = 13
                atk = 6
                dmg = 12
                dc = 15
                var_ability = 3
            case 7:
                ac = 13
                atk = 7
                dmg = 14
                dc = 16
                var_ability = 4
            case 8:
                ac = 13
                atk = 7
                dmg = 16
                dc = 16
                var_ability = 4
            case 9:
                ac = 14
                atk = 8
                dmg = 18
                dc = 17
                var_ability = 5
            case 10:
                ac = 14
                atk = 8
                dmg = 20
                dc = 18
                var_ability = 5
            case 11:
                ac = 14
                atk = 9
                dmg = 22
                dc = 19
                var_ability = 6
            case 12:
                ac = 14
                atk = 9
                dmg = 24
                dc = 20
                var_ability = 6
            case 13:
                ac = 15
                atk = 10
                dmg = 26
                dc = 21
                var_ability = 7
            case 14:
                ac = 15
                atk = 10
                dmg = 28
                dc = 22
                var_ability = 7
            case 15:
                ac = 15
                atk = 11
                dmg = 30
                dc = 23
                var_ability = 8
            case 16:
                ac = 15
                atk = 11
                dmg = 32
                dc = 24
                var_ability = 8
            case 17:
                ac = 16
                atk = 12
                dmg = 34
                dc = 25
                var_ability = 9
            case 18:
                ac = 16
                atk = 12
                dmg = 36
                dc = 26
                var_ability = 9
            case 19:
                ac = 17
                atk = 13
                dmg = 38
                dc = 27
                var_ability = 10
            case 20:
                ac = 17
                atk = 13
                dmg = 40
                dc = 28
                var_ability = 10
        match var_rarit.lower():
            case "common":
                hp *= 0.7
                ac -= 1
                dmg *= 0.5
                dc -= 1
                var_senses = random.choice(ind_ability_vision)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "uncommon":
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "rare":
                atk *= 2
                dmg *= 1.75
                dc += 1
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choices(ind_ability_movement, k=2)
        match var_class.lower():
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
        if var_level < 5:
            tier = 5
            var_tier_ability = random.sample(ind_ability_tier_5, k=2)
        elif var_level < 9:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_4, k=3)
        elif var_level < 13:
            tier = 3
            var_tier_ability = random.sample(ind_ability_tier_3, k=4)
        elif var_level < 17:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_2, k=5)
        elif var_level < 21:
            tier = 1
            var_tier_ability = random.sample(ind_ability_tier_1, k=6)
        with open("monster_repository.txt", "a") as f:
            f.write(f"\n Level {var_level} {var_rarit} {var_class} \n hp {hp} ac {ac} atk {atk} dmg {dmg} dc {dc} \n {var_senses} {var_senses_exotic} \n {var_movement} \n {var_tier_ability} \n {var_types} \n 'tier' {tier}")
        var_counter += 1
        print(var_counter)
    else:
        var_level = input("Monster Level: ")
        var_rarit = input("Monster Rarity: ")
        var_class = input("Monster Class: ")
        var_types = input("Monster Type: ")
        if var_level.lower() != "random":
            var_level_int = int(var_level)
            var_level = var_level_int
        if var_level == "random":
            var_level = random.randint(1,20)
        if var_rarit.lower() == "random":
            var_rarit = random.choice(ind_rarit)
        if var_class.lower() == "random":
            var_class = random.choice(ind_class)
        if var_types.lower() == "random":
            var_types = random.choices(ind_types, k=2)
        var_cosmetic = random.choices(ind_cosmetic, k=2)
        var_size = random.choice(ind_size)
        hp = var_level * 5
        ac= 0
        atk = 0
        dmg = 0
        dc = 0
        var_ability = 0
        match var_level:
            case 1:
                ac = 13
                atk = 4
                dmg = 4
                dc = 13
                var_ability = 1
            case 2:
                ac = 13
                atk = 4
                dmg = 4
                dc = 14
                var_ability = 1
            case 3:
                ac = 13
                atk = 5
                dmg = 6
                dc = 14
                var_ability = 2
            case 4:
                ac = 13
                atk = 5
                dmg = 8
                dc = 14
                var_ability = 2
            case 5:
                ac = 13
                atk = 6
                dmg = 10
                dc = 15
                var_ability = 3
            case 6:
                ac = 13
                atk = 6
                dmg = 12
                dc = 15
                var_ability = 3
            case 7:
                ac = 13
                atk = 7
                dmg = 14
                dc = 16
                var_ability = 4
            case 8:
                ac = 13
                atk = 7
                dmg = 16
                dc = 16
                var_ability = 4
            case 9:
                ac = 14
                atk = 8
                dmg = 18
                dc = 17
                var_ability = 5
            case 10:
                ac = 14
                atk = 8
                dmg = 20
                dc = 18
                var_ability = 5
            case 11:
                ac = 14
                atk = 9
                dmg = 22
                dc = 19
                var_ability = 6
            case 12:
                ac = 14
                atk = 9
                dmg = 24
                dc = 20
                var_ability = 6
            case 13:
                ac = 15
                atk = 10
                dmg = 26
                dc = 21
                var_ability = 7
            case 14:
                ac = 15
                atk = 10
                dmg = 28
                dc = 22
                var_ability = 7
            case 15:
                ac = 15
                atk = 11
                dmg = 30
                dc = 23
                var_ability = 8
            case 16:
                ac = 15
                atk = 11
                dmg = 32
                dc = 24
                var_ability = 8
            case 17:
                ac = 16
                atk = 12
                dmg = 34
                dc = 25
                var_ability = 9
            case 18:
                ac = 16
                atk = 12
                dmg = 36
                dc = 26
                var_ability = 9
            case 19:
                ac = 17
                atk = 13
                dmg = 38
                dc = 27
                var_ability = 10
            case 20:
                ac = 17
                atk = 13
                dmg = 40
                dc = 28
                var_ability = 10
        match var_rarit.lower():
            case "common":
                hp *= 0.7
                ac -= 1
                dmg *= 0.5
                dc -= 1
                var_senses = random.choice(ind_ability_vision)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "uncommon":
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choice(ind_ability_movement)
            case "rare":
                atk *= 2
                dmg *= 1.75
                dc += 1
                var_senses = random.choices(ind_ability_vision, k=2)
                var_senses_exotic = random.choice(ind_ability_vision_exotic)
                var_movement = random.choices(ind_ability_movement, k=2)
        match var_class.lower():
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
        if var_level < 5:
            tier = 5
            var_tier_ability = random.sample(ind_ability_tier_5, k=2)
        elif var_level < 9:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_4, k=3)
        elif var_level < 13:
            tier = 3
            var_tier_ability = random.sample(ind_ability_tier_3, k=4)
        elif var_level < 17:
            tier = 4
            var_tier_ability = random.sample(ind_ability_tier_2, k=5)
        elif var_level < 21:
            tier = 1
            var_tier_ability = random.sample(ind_ability_tier_1, k=6)
        print("Level", var_level, var_rarit, var_class)
        print("hp:", hp, "ac:", ac, "atk:", atk, "dmg:", dmg, "dc:", dc)
        print("number of abilities:", var_ability)
        print(var_senses, ",", var_senses_exotic, ",", var_movement)
        print(var_tier_ability)
        print(var_types)
        print("tier", tier)
        with open("monster_repository.txt", "a") as f:
            f.write(f"\n Level {var_level} {var_rarit} {var_class} \n hp {hp} ac {ac} atk {atk} dmg {dmg} dc {dc} \n {var_senses} {var_senses_exotic} \n {var_movement} \n {var_tier_ability} \n {var_types} \n 'tier' {tier}")
        end_program_var = input("End Program? ")