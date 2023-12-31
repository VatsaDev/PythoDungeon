# -*- coding: utf-8 -*-
"""PythoDungeon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1estIeBTfvoI8x_ZawXznQQHxd2lLIwgZ
"""

import random

colors = [
    'alice_blue',
    'antique_white',
    'aqua',
    'aquamarine',
    'azure',
    'beige',
    'bisque',
    'black',
    'blanched_almond',
    'blue',
    'blue_violet',
    'brown',
    'burlywood',
    'cadet_blue',
    'chartreuse',
    'chocolate',
    'coral',
    'cornflower_blue',
    'crimson',
    'cyan',
    'dark_blue',
    'dark_green',
    'dark_khaki',
    'deep_pink',
    'deeppurple',
    'dodger_blue',
    'firebrick',
    'floral_white',
    'forest_green',
    'fuchsia',
    'ghost_white',
    'gold',
    'goldenrod',
    'gray',
    'grey',
    'green',
    'green_yellow',
    'honeydew',
    'hot_pink',
    'indigo',
    'ivory',
    'jasmine',
    'kelley_green',
    'lavender',
    'lemon_chiffon',
    'light_blue',
    'light_coral',
    'light_green',
    'light_pink',
    'light_sky_blue',
    'lime',
    'linen',
    'magenta',
    'maroon',
    'mint',
    'misty_rose',
    'mocha',
    'navy_blue',
    'olive',
    'orange',
    'orchid',
    'pale_goldenrod',
    'pale_green',
    'pale_tan',
    'peach',
    'periwinkle',
    'pink',
    'plum',
    'powder_blue',
    'purple',
    'red_orange',
    'red_violet',
    'rosy_brown',
    'royal_blue',
    'sage',
    'salmon',
    'sandy',
    'seashell',
    'sienna',
    'silver',
    'smoke',
    'spring_green',
    'steel_grey',
    'summer_sky',
    'sunset',
    'tangerine',
    'teal',
    'thistle',
    'tomato',
    'turquoise',
    'violet',
    'wheat',
    'whiskey',
    'white',
    'wisteria',
    'yellow',
    'yellow_green',
    'yolk_ yellow'
]

room_sizes = [
    "small",
    "medium",
    "large",
    "extra_large",
    "nano",
    "micro",
    "mini",
    "tiny",
    "compact",
    "cozy",
    "spacious",
    "expansive",
    "massive",
    "gigantic",
    "humongous",
    "enormous",
    "colossal",
    "legendary",
    "mythical",
    "epic",
    "huge",
    "immense",
    "infinite",
    "unlimited",
    "boundless",
    "endless",
    "gargantuan",
    "tremendous",
    "stupendous",
    "prodigious",
    "phenomenal",
    " extraordinary",
    "incredible",
    "unbelievable",
    "unimaginable",
    "unconceivable"]

treasures = [
    "Pile of glittering dubloons",
    "Magic goblet filled with sparkling elixir",
    "Dark ring imbued with malevolent power",
    "Adamantium sword with intricate runes",
    "Gilded crown set with precious gems",
    "Ancient tome bound in supple leather",
    "Mysterious crystal orb that glows with an otherworldly light",
    "Chest overflowing with gold coins and precious artifacts",
    "Enchanted staff that crackles with arcane energy",
    "Fabled amulet said to grant immense strength",
    "Shimmering cloak woven from the finest silk and embroidered with silver thread",
    "Rare gemstone that radiates a powerful magical aura",
    "Sceptre adorned with gleaming jewels and symbols of ancient royalty",
    "Armor forged from the very metals of the earth itself",
    "Ethereal harp that plays melodies from another realm",
    "Spellbook containing forbidden knowledge and incantations",
    "Talisman that channels the primal forces of nature",
    "Holy relic imbued with divine power and blessings",
    "Infinity gauntlet that grants the wearer unparalleled mastery over time and space",
    "Ornate mirror that reveals hidden truths and secrets",
    "Luminous feather that allows its bearer to soar through the skies",
    "Amulet of protection that deflects harm and negativity",
    "Decanter that never runs dry of fine vintages and rare spirits",
    "Cursed idol that whispers maddening temptations to its owner",
    "Fae blade that cuts through any material without dulling",
    "Philosopher's stone that holds the secret to transmutation and eternal life",
    "Robe of levitation that allows its wearer to defy gravity",
    "Book of shadows that contains the secrets of dark magic and necromancy",
    "Signet ring bearing the seal of a long-lost civilization",
    "Intricately carved ivory comb that unlocks forgotten memories",
    "Set of enchanted throwing knives that always find their mark",
    "Golden compass that points towards hidden riches and untold wealth",
    "Crystal pendant that amplifies the wearer's magical abilities",
    "Grimoire bound in human skin and written in blood",
    "Wand made from a branch of the sacred tree of life",
    "Scarab brooch that holds the essence of an ancient deity",
    "Vial of dragon's breath that ignites flames of purification",
    "Coin of fate that always lands on the side of destiny",
    "Ritual mask that summons forth ancestral spirits",
    "Whispering woodwind that speaks secrets of the wildwood",
    "Bottle of pure water from the fountain of youth",
    "Key that unlocks portals to alternate dimensions"
]

monsters = [
    "Double-sworded orc",
    "Giant of Bonehands",
    "Flaming skull of vengeance",
    "Mistress of shadowy illusions",
    "Crawling chaos of tentacles",
    "Wolf-king of the frozen wastes",
    "Harpy with razor-sharp talons",
    "Golem of granite flesh",
    "Necromancer with a army of undead minions",
    "Dragonkin with scales of pure obsidian",
    "Hydra of poisonous fangs",
    "Gorgon with snakes for hair",
    "Minotaur with a maze of deadly corridors",
    "Mermaid with a voice that lures sailors to their doom",
    "Kraken with tentacles as long as ships",
    "Wyvern with wings of fiery destruction",
    "Behemoth with armored plates and a tail of devastation",
    "Sphinx with riddles that can drive men mad",
    "Chimera with heads of fire, ice, and lightning",
    "Manticore with venomous barbs and wings of darkness",
    "Basilisk with a gaze that turns enemies to stone",
    "Cockatrice with a deadly glance",
    "Bogeyman who haunts children's nightmares",
    "Gashadokuro, the giant skeleton with an insatiable hunger for human souls",
    "Yuki-onna, the spirit of the snow who freezes her victims solid",
    "Jikininki, the man-eating demon with an endless stomach",
    "Kappa, the mischievous water spirit with a beak-like mouth and a shell on his back",
    "Tsukumogami, the animate tool that seeks revenge against its former master",
    "Oni, the horned demon who brings misfortune and disaster",
    "Baku, the dream eater who feeds on nightmares",
    "Kitsune, the fox spirit with multiple tails and magical powers",
    "Nekomata, the cat creature with supernatural agility and claws",
    "Tanuki, the shape-shifting raccoon dog with a penchant for mischief",
    "Yokai, the mysterious spirit that inhabits the forest and mountains",
    "Onryo, the vengeful ghost who haunts those who have wronged it",
    "Gashadokuro, the giant skeleton with an insatiable hunger for human souls",
    "Slime, the amorphous blob that consumes everything in its path"
]

def gen_room(color, room_size,treasure,monster):
  print(f"you have enter a {room_size}, {color} room, where there is a {treasure}, but its guarded by {monster}!")
  print("you can [A] try to run [B] try to fight [C] try to loot")

print("===========================")
print("PythoDungeon")
print("===========================")
print("whats your name?")
p_name = input('> ')
print(f'welcome to the dungeon of Doom {p_name}, I dread your chances of leaving alive...')
score=0
fight_chance = 50
while True:
  global p_name
  global score
  global fight_chance

  gen_room(random.choice(colors), random.choice(room_sizes),random.choice(treasures),random.choice(monsters))
  p_choice = input('> ')
  if p_choice == 'A':
    chance = random.randint(1, 100)
    if chance > 80:
      print(f"You died {p_name} better luck next time...")
      break
    else:
      print("you escaped this room, but will you make it through the next one?")
      continue
  if p_choice == 'B':
    if fight_chance > 50:
      print(f"Your brains got bashed {p_name} better luck next time...")
      break
    else:
      chance_inc = random.randint(-2,5)
      fight_chance += chance_inc
      if chance_inc > 0:
        print(f"You got skills {p_name}! your new Fight Power is {fight_chance}")
        continue
      else:
        print(f"you got the win, but with a touch of brain damage! your new Fight Power is {fight_chance}")
        continue
  if p_choice == 'C':
    chance = random.randint(1, 100)
    if chance > 50:
      print(f"You died {p_name} better luck next time...")
      break
    else:
      print("you got the gold, how much more can you get?")
      score += 10
      print(f"your score is {score}")
      continue
  if p_choice == 'E':
    print("Exiting Game...")
    break