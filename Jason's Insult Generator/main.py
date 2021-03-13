# I got these insults from an article (multiple articles), don't judge me

import random
import linecache

insult_start_list = [
    "You're",
    "Your mom's",
    "You",
]

def insult_start():
    global random_start, insult_startstr
    random_start = random.randint(0, 2)
    insult_startstr = insult_start_list[random_start]


def insult_middle():
    global insult_middlestr
    random_adj = random.randint(1, 137)
    insult_middlestr = linecache.getline('adjectives.txt', random_adj)


def insult_end():
    random_noun = random.randint(1, 86)
    insult_endstr = linecache.getline('nouns.txt', random_noun)
    return insult_endstr

insult_start()
insult_middle()

if random_start == 2:
    connect = ' '
elif insult_middlestr.startswith("a") or insult_middlestr.startswith("e") or insult_middlestr.startswith("i") or insult_middlestr.startswith("o") or insult_middlestr.startswith("u"):
    connect = " an "
else:
    connect = " a "

print(insult_startstr + connect + insult_middlestr[:-1] + " " + insult_end()[:-1])