#!/usr/bin/python3
import random

# Pronoun
columnA = []

# Adjective
columnB = []

# Noun
columnC = []

# Places
columnD = []


# Male
listA1 = ["Mr", "Sir", "Lord", "Sire", "Professor", "Doctor", "Master", "Count", "Baron", "Magistrate", "Chief"]
# Female
listA2 = ["Mrs", "Queen", "Princess", "Lady", "Widow", "Miss", "Madame", "Mistress", "Countess", "Baroness", "Magistrix"]
# Non-binary
listA3 = ["Non-Euclidian", "Invertebrate", "Tenticular", "Other-Worldly", "The", "Mre", "Myr", "Ser", "Princet", "Barony", "Minister", "Sovereign", "Imperial", "Magistor", "Counciler", "Ensign", "Shadow"]
# All
listA4 = ["Arch", "Noble"]


# Good
listB1 = ["Glorious", "Just", "Fair", "Pure", "Light", "Kind", "Generous", "Gentle", "Graceful", "Humble", "Grand", "Great", "Immaculate", "Benevolent", "Didactic", "Brave"]
# Neutral
listB2 = ["Capricious", "Fair", "Mercurial", "Calm", "Fickle", "Ambivalent", "Colloquial", "Wise", "Elusive", "Lone"]
# Evil
listB3 = ["Malevolent", "Admonitory", "Callous", "Monstrous", "Deceitful", "Lazy", "Ambitious", "Pompous", "Rude", "Vain", "Compulsive", "Dire", "Broken", "Cold", "Nemesis"]


# Born someone, list of places
listC1 = ["Durak Mithal", "Lion's Gate", "Serpantine Isle", "Black Sea", "Guilded Coast Castle", "Blood Throne"]
# Became someone, list of deeds
listC2 = ["Heart", "Hero", "Author"]
# No one, list of commoners
listC3 = ["Wanderer", "Smith", "Stoneman", "Shoemaker"]

# names, male
namesm = ["Sherlock", "Simon", "Stoney", "Sai"]

# names, female
namesf = ["Xia", "Xaya", "Lily", "Violet", "Fiora", "Flower", "Rose", "Diamond", "Jewel", "Ruby", "Rita", "Liliana", "Morgana", "Victoria", "Lisa"]

# names, indifferent
namesi = ["Jessie", "Alex", "Atlas", "Aspen"]

# gender
print("[1]: Male")
print("[2]: Female")
print("[3]: Non-binary")
print("Enter 1, 2, or 3:")
question1 = int(input())
if (question1 < 1):
	print("invalid response, exiting")
	exit()
if (question1 > 3):
	print("invalid response, exiting")
	exit()
if (question1 == 1):
	columnA = listA1
	names = namesm + namesi
if (question1 == 2):
	columnA = listA2
	names = namesf + namesi
if (question1 == 3):
	columnA = listA3
	names = namesi

columnA = columnA + listA4

# alignment
print("[1]: Good")
print("[2]: Neutral")
print("[3]: Evil")
print("Enter 1, 2, or 3:")
question2 = int(input())
if (question2 < 1):
	print("invalid response, exiting")
	exit()
if (question2 > 3):
	print("invalid response, exiting")
	exit()
if (question2 == 1):
	columnB = listB1
if (question2 == 2):
	columnB = listB2
if (question2 == 3):
	columnB = listB3

# noun
print("[1]: Born someone")
print("[2]: Became someone")
print("[3]: No one")
print("Enter 1, 2, or 3:")
question3 = int(input())
if (question3 < 1):
	print("invalid response, exiting")
	exit()
if (question3 > 3):
	print("invalid response, exiting")
	exit()
if (question3 == 1):
	columnC = listC1
if (question3 == 2):
	columnC = listC2
if (question3 == 3):
	columnC = listC3


if (question3 == 1):
	print(random.choice(columnA), random.choice(names), "of", random.choice(columnC))
	exit()
elif (question3 == 2):
	print(random.choice(names), ", the ", random.choice(columnB), " ", random.choice(columnC), sep="")
else:
	print(random.choice(names), random.choice(columnC))
