import json
import random
from js import fetch
import asyncio


async def load_json(path):

    response = await fetch(path)
    text = await response.text()

    return json.loads(text)


async def init():

    global verbs
    global voc
    global particles

    verbs = await load_json("verbs.json")
    voc = await load_json("voc.json")
    particles = await load_json("particles.json")


memory = []


def random_person(particles):

    persone = particles["persone"]

    index = random.randrange(len(persone))

    return persone[index], index


def random_verb(verbs, index):

    keys = list(verbs["verbi"].keys())

    verbo_key = random.choice(keys)

    forms = verbs["verbi"][verbo_key]["presente"]

    return verbo_key, forms[index]


def random_city(voc):

    return random.choice(voc["cities"])


def article(word):

    vowels = ["a","e","i","o","u"]

    if word[0] in vowels:
        return "l'"

    if word.startswith(("s","z","gn","ps")):
        return "lo"

    if word.endswith("a"):
        return "la"

    return "il"


def word_score(city, word):

    score = 0

    score += city["mare"] * word["acqua"]
    score += city["montagna"] * word["terra"]
    score += city["sole"] * word["fuoco"]
    score += city["verde"] * word["natura"]

    return score


def semantic_word(voc, city):

    scored = []

    for word in voc["words"]:

        score = word_score(city, word)

        scored.append((score, word))

    scored.sort(key=lambda x: x[0], reverse=True)

    top = scored[:10]

    return random.choice(top)[1]["word"]


def build_object(word):

    art = article(word)

    if art == "l'":
        return art + word

    return art + " " + word


templates = [

"{persona} {verbo} {oggetto}",

"{persona} {verbo} {oggetto} {prep} {citta}",

"{citta}, {persona} {verbo} {oggetto}",

"{persona} {verbo} {oggetto} vicino {oggetto2}",

"{persona} {verbo} {oggetto} sotto {oggetto2}",

"{persona} {verbo} {oggetto} tra {oggetto2} e {oggetto3}",

"{citta}, {persona} {verbo} {oggetto} {prep} {oggetto2}"

]


def generate_sentence():

    global memory

    persona, index = random_person(particles)

    verbo_key, verbo = random_verb(verbs, index)

    city = random_city(voc)

    city_name = city["name"]

    w1 = semantic_word(voc, city)
    w2 = semantic_word(voc, city)
    w3 = semantic_word(voc, city)

    oggetto = build_object(w1)
    oggetto2 = build_object(w2)
    oggetto3 = build_object(w3)

    preps = list(particles["preposizioni_semplici"].keys())

    prep = random.choice(preps)

    template = random.choice(templates)

    frase = template.format(
        persona=persona,
        verbo=verbo,
        oggetto=oggetto,
        oggetto2=oggetto2,
        oggetto3=oggetto3,
        citta=city_name,
        prep=prep
    )

    frase = frase.capitalize() + "."

    if frase not in memory:
        memory.append(frase)

    if len(memory) > 10:
        memory.pop(0)

    return frase