# Things to add:
# - More properties of heros to give comparison on
# - Clean up game loop
# - Import heroes in smoother way
# - Create aliases for hero names (common misspellings, shorthands, etc.)

# ↑↓√

import numpy as np
import random
import time

from Hero import *

name_match = ''
attr_match = ''
range_match = ''
ms_match =  ''

def compare(guessed, correct):
    global name_match
    if guessed.name.lower() == correct.name.lower():
        name_match = True
    else: name_match = False

    global attr_match
    if guessed.attr == correct.attr:
        attr_match = '√'
    else: attr_match = 'X'

    global range_match
    if guessed.range == correct.range:
        range_match = '√'
    else: range_match = 'X'

    global ms_match
    hero_ms = ' (' + str(guessed.ms) + ')'
    if guessed.ms == correct.ms:
        ms_match = '√' + hero_ms
    elif guessed.ms > correct.ms:
        ms_match = '↓' + hero_ms
    else: ms_match = '↑' + hero_ms

    print('Hero\t\t\t\t' +  'Attribute\t' + 'Range\t' + 'Move Speed\n' + guessed.name + '\t\t\t\t' + attr_match + '\t\t' + range_match + '\t' + ms_match)
    # fix print statement to be equal with all lengths of hero names
    return name_match

abaddon = Hero('Abaddon', 'STR', 'melee', 325)
alchemist = Hero('Alchemist', 'STR', 'melee', 305)
ancient_apparition = Hero('Ancient Apparition', 'INT', 'ranged', 285)
antimage = Hero('Anti-Mage', 'AGI', 'melee', 310)
arc_warden = Hero('Arc Warden', 'AGI', 'ranged', 285)
axe = Hero('Axe', 'STR', 'melee', 310)
bane = Hero('Bane', 'INT', 'ranged', 305)
batrider = Hero('Batrider', 'INT', 'ranged', 300)
beastmaster = Hero('Beastmaster', 'STR', 'melee', 305)
bloodseeker = Hero('Bloodseeker', 'AGI', 'melee', 300)

hero_list = [abaddon, alchemist, ancient_apparition, antimage, arc_warden, axe, bane, batrider, beastmaster, bloodseeker]

secret_hero = hero_list[random.randint(0,len(hero_list))]

guess = ''

while guess.lower() != secret_hero.name.lower():  # some redundancy in this condition
    guess = input("Guess the hero: ")
    for hero in hero_list:
        if hero.name.lower() == guess.lower():
            guessed_hero = hero
            compare(guessed_hero, secret_hero)

print("You got it!")
# time.sleep(10)

"""
bounty_hunter = 
brewmaster = 
bristleback = 
broodmother = 
centaur_warrunner = 
chaos_knight = 
chen = 
clinkz = 
clockwerk = 
crystal_maiden =  
dark_seer = 
dark_willow = 
dawnbreaker = 
dazzle = 
death_prophet = 
disruptor = 
doom = 
dragon_knight = 
drow_ranger = 
earth_spirit = 
earthshaker = 
elder_titan = 
ember_spirit = 
enchantress = 
enigma = 
faceless_void = 
grimstroke = 
gyrocopter = 
hoodwink = 
huskar = 
invoker = 
io = 
jakiro = 
juggernaut = 
keeper_of_the_light = 
kunkka = 
legion_commander = 
leshrac = 
lich = 
lifestealer = 
lina = 
lion = 
lone_druid = 
luna = 
lycan = 
magnus = 
marci = 
mars = 
medusa = 
meepo = 
mirana = 
monkey_king = 
morphling = 
naga_siren = 
natures_prophet = 
necrophos = 
night_stalker = 
nyx_assassin = 
ogre_magi = 
omniknight = 
oracle = 
outworld_destroyer = 
pangolier = 
phantom_assassin = 
phantom_lancer = 
phoenix = 
puck = 
pudge = 
pugna = 
queen_of_pain = 
razor = 
riki = 
rubick = 
sand_king = 
shadow_demon = 
shadow_fiend = 
shadow_shaman = 
silencer = 
skywrath_mage = 
slardar = 
slark = 
snapfire = 
sniper = 
spectre = 
spirit_breaker = 
storm_spirit = 
sven = 
techies = 
templar_assassin = 
terrorblade = 
tidehunter = 
timbersaw = 
tinker = 
tiny = 
treant_protector = 
troll_warlord = 
tusk = 
underlord = 
undying = 
ursa = 
vengeful_spirit = 
venomancer = 
viper = 
visage = 
void_spirit = 
warlock = 
weaver = 
windranger = 
winter_wyvern = 
witch_doctor = 
wraith_king = 
zeus = 
"""
