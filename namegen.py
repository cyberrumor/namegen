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
listA3 = ["Non-Euclidian", "Invertebrate", "Tenticular", "Other-Worldly", "Mre", "Myr", "Ser", "Princet", "Barony", "Minister", "Sovereign", "Imperial", "Magister", "Counciler", "Ensign"]
# All
listA4 = ["Arch", "Noble", "Augur", "Seer", "Prelat", "Oligarch", "Tilde"]


# Good adjectives
listB1 = ["Glorious", "Just", "Fair", "Pure", "Light", "Kind", "Imperious", "Generous", "Gentle", "Graceful", "Humble", "Grand", "Great", "Immaculate", "Benevolent", "Didactic", "Brave", "Dawn", "Worthy", "White", "Cenobite"]
# Neutral adjectives
listB2 = ["Capricious", "Fair", "Mercurial", "Calm", "Fickle", "Ambivalent", "Colloquial", "Wise", "Elusive", "Lone", "Dusk", "Twilight", "Immortal", "Gray", "Litany"]
# Evil adjectives
listB3 = ["Malevolent", "Admonitory", "Callous", "Monstrous", "Deceitful", "Lazy", "Ambitious", "Pompous", "Rude", "Vain", "Compulsive", "Dire", "Broken", "Cold", "Darkest", "Night", "Midnight", "Wicked", "Black", "Aphotic"]


# Born someone, list of places
listC1 = ["Durak Mithal", "Lion's Gate", "the Serpantine Isle", "the Black Sea", "the Guilded Coast Castle", "the Blood Throne", "the Western Coast", "the Eastern Marsh", "the Southern Wastes", "the Northern Woods", "the Dry Sea", "the Sweltering Isles", "Dragon's Cliff", "the Shrieking Bog", "the Misty Caverns", "the Merciless Abyss", "the Forgotten Paths", "Elder Grove", "Charred Thicket", "Forbidden Orchard", "the Corrupted Mines", "Sheltered Glen", "the World's Coffin", "Last Garden", "Ol' Marine", "Ladder of Vines", "Obsidian Crater", "the Cabal Archives"]
# Became someone, list of deeds, nouns
listC2 = ["Heart", "Hero", "Author", "Savior", "Figure", "Luminary", "Sympathizer", "Advocate", "Patron", "Guardian", "Subjugator", "Icon", "Paragon", "Wizard", "Rogue", "Whisperer", "Conspirator", "Shadow", "Silhouette", "Negotiator", "Ghost", "Stranger"]


# No one, list of last names
listC3 = ["Stoneman", "Shoemaker", "Brewmaster", "Ranger", "Tutor", "Tailor", "Seeker", "Stitcher", "Gambler", "Baker", "Brewer", "Fisher", "Fletcher", "Skinner", "Glover", "Tapper", "Turner", "Woodward", "Bowmaker", "Slaymaker", "Lister", "Potter",  "Sumner", "Kitemaker", "Forseer", "Architect"]

# names, male
namesm = ["Sherlock", "Simon", "Stoney", "Edward", "August", "Maximus", "Ormel", "Blaine", "James", "Arthur", "Ernest", "William", "Gregory", "Samuel", "Byron", "Augustus", "Zachariah", "Elijah" ]

# names, female
namesf = ["Xia", "Xaya", "Violet", "Fiora", "Flower", "Rose", "Diamond", "Jewel", "Ruby", "Rita", "Liliana", "Morgana", "Victoria", "Lisa", "Elena", "Iona", "Rozalia", "Mariposa", "Marina", "Orchid", "Daphne", "Teresa", "Jane", "Jillian", "Magnolia", "Paige", ]

# names, indifferent
namesi = ["Alex", "Atlas", "Aspen", "Sai", "Afton", "River", "Jade", "Kelcee", "Onyx", "Ray", "Brynn", "Brion", "Euros", "Clark", "Crucible", "Thorn", "Sean"]

# evil names, indifferent
enames = ["Nemesis", "Guile", "Lich", "Hass", "Hatred", "Mal Coeur", "Coeur de Noir", "Hostility", "Rona", "Gloom", "Abominable", "Pride", "Vanity", "Sloth", "Lust", "Gluttony", "Envy", "Wrath", "Bones", "Revenge", "Emptiness", "Pain", "Litterer"]



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
	names = enames

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


# generate name
if (question3 == 1):
	print()
	print(random.choice(columnA), random.choice(names), "of", random.choice(columnC))
	print()
	input('[Enter] to exit')
	exit()
elif (question3 == 2):
	print()
	print(random.choice(names), ", the ", random.choice(columnB), " ", random.choice(columnC), sep="")
	print()
	input('[Enter] to exit')
	exit()
else:
	# Evil nobody
	if (question2 == 3):
		print()
		print(random.choice(enames), ", the ", random.choice(columnB), " ", random.choice(columnC), sep="")
		print()
		input('[Enter] to exit')
		exit()
	# Other nobody
	else:
		print()
		print(random.choice(names), random.choice(columnC))
		print()
		input('[Enter] to exit')
		exit()
