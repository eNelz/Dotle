import numpy as np
import random
import time

name_match = ''
attr_match = ''
range_match = ''

class Hero:
    def __init__(self, name, attr, range):
        self.name = name
        self.attr = attr
        self.range = range

    def printName(self):
        print(self.name)

def compare(guessed, correct):
    global name_match
    if guessed.name == correct.name:
        name_match = 'O'
    else: name_match = 'X'

    global attr_match
    if guessed.attr == correct.attr:
        attr_match = 'O'
    else: attr_match = 'X'

    global range_match
    if guessed.range == correct.range:
        range_match = 'O'
    else: range_match = 'X'

    print('Name\t ' +  'Attribute\t ' + 'Range\n' + name_match + '\t\t' + attr_match + '\t\t' + range_match)
    if name_match == 'O':
        return True
    else: return False

abaddon = Hero('Abaddon', 'STR', 'melee')
alchemist = Hero('Alchemist', 'STR', 'melee')
ancient_apparition = Hero('Ancient Apparition', 'INT', 'ranged')
antimage = Hero('Anti-Mage', 'AGI', 'melee')
arc_warden = Hero('Arc Warden', 'AGI', 'ranged')
axe = Hero('Axe', 'STR', 'melee')
bane = Hero('Bane', 'INT', 'ranged')
batrider = Hero('Batrider', 'INT', 'ranged')
beastmaster = Hero('Beastmaster', 'STR', 'melee')
bloodseeker = Hero('Bloodseeker', 'AGI', 'melee')

hero_list = [abaddon, alchemist, ancient_apparition, antimage, arc_warden, axe, bane, batrider, beastmaster, bloodseeker]

secret_hero = hero_list[random.randint(0,len(hero_list))]

guess = ''

while guess != secret_hero.name:  # some redundancy in this condition
    guess = input("Guess the hero: ")
    for hero in hero_list:
        if hero.name == guess:
            guessed_hero = hero
            compare(guessed_hero, secret_hero)

print("You got it!")
time.sleep(10)

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
