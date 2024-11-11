import random
def lazyAbility(**kwargs):
    def abilityFunction():
        return Ability(**kwargs) 
    return abilityFunction
def plural(text,quantity):
    if(quantity>1):
        return text
    else:
        return ""
def singPlural(text,quantity,text2):
    if(quantity.isnumeric()):
        if(int(quantity)==1):
            return text
    return text2
def toNumberWord(numberText):
    if numberText.isnumeric():
        return numberWords[int(numberText)-1]
    return ""
def ifNumeric(text,number):
    if(number.isNumeric()):
        return text
    return ""
def isCreature(x):

    return x.cardType=="creature"
def getNbr(bound=5):

    return random.randint(1,bound)
def getNbrWord(bound=5):

    return numberWords[random.randint(0,bound-1)]
def getNbrFunction(bound=5):
    def n():
        return random.randint(1,bound)
    return n
def choiceFunction(choices):
    def cf():
        return random.choice(choices)
    return cf
def targetPlayer():

    return random.choice(["you","you","you","you","you","target player","target opponent","each opponent","each player"])
def targetPlayerP():

    return random.choice(["your","your","your","your","your","target players","target opponents","each opponents","each players"])
def aPlayerSelector():

    return random.choice(["you","you","you","a player","an opponent"])
def aPlayerSelectorP():

    return random.choice(["your","your","your","each players","each opponents"])
def cardSelector(plural=""):
    text="card"+plural
    if(random.random()<0.5):
        types=cardTypes[:]+["basic land"]
        if(random.random()<0.5):
            types+=superTypes
        text=random.choice(types)+" "+text
    if(text!="land card" and text!="basic land card"):
        if(random.random()<0.25):
            text+=" with mana value "+random.choice(["greater than ","less than "])+str(getNbr())
        if(random.random()<0.1):
            text=random.choice(colorNames)+" "+text
    return text
def permanentSelector(plural=""):
    return "permanent"+plural
def creatureSelector(plural=""):
    return "creature"+plural
def planeswalkerSelector(plural=""):
    return "planeswalker"+plural
def spellSelector():
    return "spell"
def playerActionSelector():
    possibleTriggers=[f"draws a card","plays a land","casts a "+spellSelector(),"gains life","loses life","becomes the target of a spell or ability"]
    if(random.random()<0.1):
        return " or ".join(random.sample(possibleTriggers,2))
    return random.choice(possibleTriggers)
def phaseSelector():
    
    return random.choice(["upkeep","end step","draw step","first main phase","combat phase"])
def numberSelector():
    if(random.random()<0.4):
        return str(getNbr(bound=3))
    if(random.random()<0.4):
        return str(getNbr(bound=5))
    text="equal to the "
    text+=random.choice([
        "number of cards in "+targetPlayerP()+" hand",
        "number of "+cardSelector(plural="s")+" in "+targetPlayerP()+" graveyard",
        "number of cardtypes among cards in "+targetPlayerP()+" graveyard",
        "greatest "+random.choice(["manavalue among"+permanentSelector(plural="s")+"you control","power among "+creatureSelector(plural="s")+" you control","toughess"+creatureSelector(plural="s")+" you control"]),
        targetPlayerP()+" life total",
        "number of "+permanentSelector(plural="s")+random.choice([" you control"," on the battlefield"])
        ])
    return text
def creatureTriggerSelector():
    possibleTriggers=["attacks","enters the battlefield","leaves the battlefield","dies","becomes tapped","becomes untapped","blocks","deals combat damage to a player","deals damage","deals combat damage","becomes the target of spell or ability","is dealt damage"]
    if(random.random()<0.3):
        return " or ".join(random.sample(possibleTriggers,2))
    return random.choice(possibleTriggers)
def makeActivatedCost():
    text=""
    return text
keywords={
    "Flash":{"requirements":isCreature,"colors":"u"},
    "Reach":{"requirements":isCreature,"colors":"g"},
    "Shroud":{"requirements":isCreature,"colors":"u"},
    "Trample":{"requirements":isCreature,"colors":"gr"},
    "Vigilance":{"requirements":isCreature,"colors":"uw"},
    "Menace":{"requirements":isCreature,"colors":"br"},
    "Double strike":{"requirements":isCreature,"colors":"wr"},
    "First strike":{"requirements":isCreature,"colors":"wb"},
    "Deathtouch":{"requirements":isCreature,"colors":"bg"},
    "Defender":{"requirements":isCreature,"colors":"wubg"},
    "Flying":{"requirements":isCreature,"colors":"wubr"},
    "Haste":{"requirements":isCreature,"colors":"rgb"},
    "Hexproof":{"requirements":isCreature,"colors":"wug"},
    "Indestructible":{"requirements":isCreature,"colors":"w"},
    "Intimidate":{"requirements":isCreature,"colors":"b"},
    "Lifelink":{"requirements":isCreature,"colors":"wb"},
    #"Living weapon"
    #   "Jump-start",
    #   "Basic landcycling",
    #   "Commander ninjutsu",
    #   "Legendary landwalk",
    #   "Nonbasic landwalk",
    #   "Totem armor",
    #   "Megamorph",
    #   "Haunt",
    #   "Forecast",
    #   "Graft",
    #   "Fortify",
    #   "Frenzy",
    #   "Gravestorm",
    #   "Hideaway",
    #   "Level Up",
    #   "Infect",
    #   "Protection",
    #   "Rampage",
    #   "Phasing",
    #   "Multikicker",
    #   "Morph",
    #   "Provoke",
    #   "Modular",
    #   "Offering",
    #   "Ninjutsu",
    #   "Replicate",
    #   "Recover",
    #   "Poisonous",
    #   "Prowl",
    #   "Reinforce",
    #   "Persist",
    #   "Retrace",
    #   "Rebound",
    #   "Miracle",
    #   "Overload",
    #   "Outlast",
    #   "Prowess",
    #   "Renown",
    #   "Myriad",
    #   "Shadow",
    #   "Storm",
    #   "Soulshift",
    #   "Splice",
    #   "Transmute",
    #   "Ripple",
    #   "Suspend",
    #   "Vanishing",
    #   "Transfigure",
    #   "Wither",
    #   "Unearth",
    #   "Undying",
    #   "Soulbond",
    #   "Unleash",
    #   "Ascend",
    #   "Assist",
    #   "Afterlife",
    #   "Companion",
    #   "Fabricate",
    #   "Embalm",
    #   "Escape",
    #   "Fuse",
    #   "Ingest",
    #   "Melee",
    #   "Improvise",
    #   "Mentor",
    #   "Partner",
    #   "Mutate",
    #   "Scavenge",
    #   "Tribute",
    #   "Surge",
    #   "Skulk",
    #   "Undaunted",
    #   "Riot",
    #   "Spectacle",
    #   "Forestwalk",
    #   "Islandwalk",
    #   "Mountainwalk",

    #   "Cumulative upkeep",

    #   "Encore",
    #   "Sunburst",

    #   "Foretell",
    #   "Amplify",
    #   "Affinity",
    #   "Bushido",
    #   "Convoke",
    #   "Bloodthirst",
    #   "Absorb",
    #   "Aura Swap",
    #   "Changeling",
    #   "Conspire",
    #   "Cascade",
    #   "Annihilator",
    #   "Battle Cry",
    #   "Cipher",
    #   "Bestow",
    #   "Dash",
    #   "Awaken",
    #   "Crew",
    #   "Aftermath",
    #   "Afflict",
    #   "Flanking",
    #   "Echo",
    #   "Fading",
    #   "Fear",
    #   "Eternalize",
    #   "Entwine",
    #   "Epic",
    #   "Dredge",
    #   "Delve",
    #   "Evoke",
    #   "Exalted",
    #   "Evolve",
    #   "Extort",
    #   "Dethrone",
    #   "Exploit",
    #   "Devoid",
    #   "Emerge",
    #   "Escalate",

    #   "Horsemanship",
    #   "Kicker",
    #   "Madness",
    #   "Hidden agenda",
    #   "Swampwalk",
    #   "Desertwalk",
    #   "Wizardcycling",
    #   "Slivercycling",
    #   "Cycling",
    #   "Landwalk",
    #   "Plainswalk",
    #   "Champion",
    #   "Enchant",
    #   "Plainscycling",
    #   "Islandcycling",
    #   "Swampcycling",
    #   "Mountaincycling",
    #   "Forestcycling",
    #   "Landcycling",
    #   "Typecycling",
    #   "Split second",
    #   "Banding",
    #   "Augment",
    #   "Double agenda",
    #   "Partner with",
    #   "Hexproof from",
    #   "Boast",
    #   "Buyback",
    #   "Ward",
    #   "Demonstrate",
    #   "Devour",
    #   "Flashback",
    #   "Equip",
    #   "Reconfigure",
    #   "Compleated",
    #   "Daybound",
    #   "Nightbound",
    #   "Decayed",
    #   "Disturb",
    #   "Training",
    #   "Cleave",
    #   "Intensity",
    #   "Blitz",
    #   "Casualty",
    #   "Friends forever"
}
positiveStuff=[
    lazyAbility(name="draw",colors="ubg",
        outputLambda=lambda ab,card:f"{ab.targets[0]} draw{ab.targets[1].isnumeric()*(' '+toNumberWord(ab.targets[1]))} card{singPlural('',ab.targets[1],'s')}{(' '+ab.targets[1])*( not ab.targets[1].isnumeric())}.",
        targetReqs=["player","number"],
        ),
    lazyAbility(name="scry",colors="u",),
    lazyAbility(name="search",colors="wubrg",
        outputLambda=lambda ab,card:f"search {ab.targets[0]} library for a {ab.targets[1]} and reveal it. Shuffle that players library and put it {ab.targets[2]}",
        targetReqs=["players","card","zone"],
        ),
    lazyAbility(name="damage",colors="r",
        outputLambda=lambda ab,card:f"<This> deals{ab.targets[1].isnumeric()*(' '+ab.targets[1])} damage to {ab.targets[0]}{(not ab.targets[1].isnumeric())*(' '+ab.targets[1])}",
        targetReqs=["damagable","number",],
        ),
    ]
triggeredAbilities=[
    lazyAbility(name="another",colors="wubrg",
        outputLambda=lambda ab,card:f"Whenever a {ab.targets[0]} {ab.targets[1]}, ",
        requirements=isCreature,
        targetReqs=[creatureSelector,creatureTriggerSelector],
        ),
    lazyAbility(name="this",colors="wubrg",
        outputLambda=lambda ab,card:f"When <this> {ab.targets[0]}, ",
        requirements=isCreature,
        targetReqs=[creatureTriggerSelector],
        ),
    lazyAbility(name="etb",colors="wubrg",
        outputLambda=lambda ab,card:f"When <this> {ab.targets[0]}, ",
        targetReqs=[choiceFunction(["enters the battlefield","leaves the battlefield","enters or leaves the battlefield",])],
        ),
    lazyAbility(name="otheretb",colors="wubrg",
        outputLambda=lambda ab,card:f"Whenever {ab.targets[2]} {ab.targets[0]} {ab.targets[1]}, ",
        targetReqs=["permanent",choiceFunction(["enters the battlefield","leaves the battlefield","enters or leaves the battlefield",]),choiceFunction(["a","one or more"])],
        ),
    lazyAbility(name="player action",colors="wubrg",
        outputLambda=lambda ab,card:f"Whenever {ab.targets[0]} {ab.targets[1]}, ",
        targetReqs=[aPlayerSelector,playerActionSelector],
        ),
    lazyAbility(name="phase",colors="wubrg",
        outputLambda=lambda ab,card:f"At the beginning of {ab.targets[0]} {ab.targets[1]}, ",
        targetReqs=[aPlayerSelectorP,phaseSelector],
        ),

    ]
[
    #lifegain
    #lifeloss
    #Bolster
    #Fateseal
    #Manifest
    #Monstrosity
    #Populate
    #Proliferate
    #"Support",
    #"Detain",
    #"Explore",
    #"Fight",
    #"Amass",
    #"Adapt",
    #"Attach",
    #"Cast",
    #"Counter",
    #"Create",
    #"Destroy",
    #"Discard",
    #"Double",
    #"Exchange",
    #"Exile",
    #"Investigate",
    #"Play",
    #"Regenerate",
    #"Reveal",
    #"Sacrifice",
    #"Shuffle",
    #"Tap",
    #"Untap",
    #"Surveil",
    #"Goad",
    #"Mill",
    #"Learn",
    #"Exert",
    #"Connive",
    ]
targetSelectors={
    "player":targetPlayer,
    "players":targetPlayerP,
    "zone":choiceFunction(["into play under you control","into hand","into that players graveyard","onto the top that players library"]),
    "card":cardSelector,
    "permanent":permanentSelector,
    "number":numberSelector,
    "numeric":lambda :str(getNbr()),
    "damagable":choiceFunction(["any target","target creature or planeswalker","target player","each player","each opponent","target "+creatureSelector(),"target "+planeswalkerSelector()]),
}
creatureTypes= [
    "Advisor",
    "Aetherborn",
    "Alien",
    "Ally",
    "Angel",
    "Antelope",
    "Ape",
    "Archer",
    "Archon",
    "Army",
    "Artificer",
    "Assassin",
    "Assembly-Worker",
    "Astartes",
    "Atog",
    "Aurochs",
    "Avatar",
    "Azra",
    "Badger",
    "Barbarian",
    "Bard",
    "Basilisk",
    "Bat",
    "Bear",
    "Beast",
    "Beeble",
    "Beholder",
    "Berserker",
    "Bird",
    "Blinkmoth",
    "Boar",
    "Bringer",
    "Brushwagg",
    "Camarid",
    "Camel",
    "Caribou",
    "Carrier",
    "Cat",
    "Centaur",
    "Cephalid",
    "Chicken",
    "Chimera",
    "Citizen",
    "Cleric",
    "Cockatrice",
    "Construct",
    "Coward",
    "Crab",
    "Crocodile",
    "Cyclops",
    "Dauthi",
    "Demigod",
    "Demon",
    "Deserter",
    "Devil",
    "Dinosaur",
    "Djinn",
    "Dog",
    "Dragon",
    "Drake",
    "Dreadnought",
    "Drone",
    "Druid",
    "Dryad",
    "Dwarf",
    "Efreet",
    "Egg",
    "Elder",
    "Eldrazi",
    "Elemental",
    "Elephant",
    "Elf",
    "Elk",
    "Eye",
    "Faerie",
    "Ferret",
    "Fish",
    "Flagbearer",
    "Fox",
    "Fractal",
    "Frog",
    "Fungus",
    "Gargoyle",
    "Germ",
    "Giant",
    "Gith",
    "Gnoll",
    "Gnome",
    "Goat",
    "Goblin",
    "God",
    "Golem",
    "Gorgon",
    "Graveborn",
    "Gremlin",
    "Griffin",
    "Guest",
    "Hag",
    "Halfling",
    "Hamster",
    "Harpy",
    "Head",
    "Hellion",
    "Hippo",
    "Hippogriff",
    "Homarid",
    "Homunculus",
    "Hornet",
    "Horror",
    "Horse",
    "Human",
    "Hydra",
    "Hyena",
    "Illusion",
    "Imp",
    "Incarnation",
    "Inkling",
    "Insect",
    "Jackal",
    "Jellyfish",
    "Juggernaut",
    "Kavu",
    "Kirin",
    "Kithkin",
    "Knight",
    "Kobold",
    "Kor",
    "Kraken",
    "Lamia",
    "Lammasu",
    "Leech",
    "Leviathan",
    "Lhurgoyf",
    "Licid",
    "Lizard",
    "Manticore",
    "Masticore",
    "Mercenary",
    "Merfolk",
    "Metathran",
    "Minion",
    "Minotaur",
    "Mole",
    "Monger",
    "Mongoose",
    "Monk",
    "Monkey",
    "Moonfolk",
    "Mouse",
    "Mutant",
    "Myr",
    "Mystic",
    "Naga",
    "Nautilus",
    "Nephilim",
    "Nightmare",
    "Nightstalker",
    "Ninja",
    "Noble",
    "Noggle",
    "Nomad",
    "Nymph",
    "Octopus",
    "Ogre",
    "Ooze",
    "Orb",
    "Orc",
    "Orgg",
    "Otter",
    "Ouphe",
    "Ox",
    "Oyster",
    "Pangolin",
    "Peasant",
    "Pegasus",
    "Pentavite",
    "Performer",
    "Pest",
    "Phelddagrif",
    "Phoenix",
    "Phyrexian",
    "Pilot",
    "Pincher",
    "Pirate",
    "Plant",
    "Praetor",
    "Prism",
    "Processor",
    "Rabbit",
    "Raccoon",
    "Ranger",
    "Rat",
    "Rebel",
    "Reflection",
    "Reveler",
    "Rhino",
    "Rigger",
    "Rogue",
    "Sable",
    "Salamander",
    "Samurai",
    "Sand",
    "Saproling",
    "Satyr",
    "Scarecrow",
    "Scion",
    "Scorpion",
    "Scout",
    "Sculpture",
    "Serf",
    "Serpent",
    "Servo",
    "Shade",
    "Shaman",
    "Shapeshifter",
    "Shark",
    "Sheep",
    "Siren",
    "Skeleton",
    "Slith",
    "Sliver",
    "Slug",
    "Snake",
    "Soldier",
    "Soltari",
    "Spawn",
    "Specter",
    "Spellshaper",
    "Sphinx",
    "Spider",
    "Spike",
    "Spirit",
    "Splinter",
    "Sponge",
    "Squid",
    "Squirrel",
    "Starfish",
    "Surrakar",
    "Survivor",
    "Tentacle",
    "Tetravite",
    "Thalakos",
    "Thopter",
    "Thrull",
    "Tiefling",
    "Treefolk",
    "Trilobite",
    "Triskelavite",
    "Troll",
    "Turtle",
    "Unicorn",
    "Vampire",
    "Vedalken",
    "Viashino",
    "Volver",
    "Wall",
    "Walrus",
    "Warlock",
    "Warrior",
    "Wasp",
    "Weird",
    "Werewolf",
    "Whale",
    "Wizard",
    "Wolf",
    "Wolverine",
    "Wombat",
    "Worm",
    "Wraith",
    "Wurm",
    "Yeti",
    "Zombie",
    "Zubera",]
colors=["w","u","b","r","g"]
colorNames=["white","blue","black","red","green"]
rarities=["common","uncommon","rare","mythic rare"]
cardTypes=["creature","instant","sorcery","enchantment","planeswalker","artifact","land"]
superTypes=["snow","legendary"]
basicTypes=["plains","island","swamp","mountain","forest"]
numberWords=["a","two","three","four","five","six","seven","eight","nine","ten"]
class Ability():
    def __init__(self,name="",colors="wubrg",power=1,requirements=lambda x:True,cost=None,outputLambda=(lambda ab,card:f"{ab.name} {ab.targets[0]}"),scope=1,targetReqs=["numeric"]):
        self.name,self.colors,self.power,self.scope=name,colors,power,scope
        if(cost):

            pass
        if(requirements):

            self.requirements=requirements
        if(targetReqs):
            self.targets=self.getTargets(targetReqs)
        if(outputLambda):
            self.outputLambda=outputLambda
    def getTargets(self,targetReqs):
        targets=[]
        for target in targetReqs:
            if(isinstance(target,str)):
                targets.append(targetSelectors[target]())
            if(callable(target)):
                targets.append(target())
            if(isinstance(target,tuple)):
                targets.append(target[0])
                self.scope*=target[1]            

        return targets
    def getOutput(self,card):

        return self.outputLambda(self,card)

class Card():
    def __init__(self, color=None,cardType=None,cmc=None,rarity=None):
        self.color,self.cardType,self.cmc,self.rarity=color,cardType,cmc,rarity
        if(not self.cardType):
            self.cardType=random.choice(cardTypes)
        if(not self.color):
            self.color=random.choice(colors)
        if(not self.cmc):
            self.cmc=self.randomCmc()
        if(not self.rarity):
            self.rarity=random.choice(rarities)
        self.name="CARDNAME"  # markov generation 
        self.typeLine=self.cardType
        self.cost=self.makeCost()
        self.stats=self.createPT()
        self.attributeList=[]
        self.cardText=self.createOracle()
        self.flavorText = "flvourtezr"
    def randomCmc(self):

        return random.randint(random.randint(0,2),random.randint(3,random.randint(4,random.randint(6,15))))

    def makeCost(self):
        colored=1+sum([int(random.random()<1/9) for i in range(self.cmc-1)]) # different per color maybe black=higher
        return  ("{"+str(self.cmc-colored)+"}")*(self.cmc-colored>0)+("{"+self.color+"}")*(colored)
    def toString(self):

        return f"{self.name} {self.cost}\n{self.typeLine}\n{self.rarity}\n{self.cardText}\n{self.stats}\n"        

    def createOracle(self):
        oracleText = ""
        if(self.cardType=="creature"):
            oracleText+=random.choice([self.createKeyword,self.createTrigger,self.createActivated,self.createStatic])()
        elif(self.cardType=="land"):
            oracleText+=random.choice([self.createActivated])()
        elif(self.cardType=="planeswalker"):
            pass
            #oracleText+=random.choice([self.createActivated])()
        elif(self.cardType=="artifact"):
            oracleText+=random.choice([self.createTrigger,self.createActivated,self.createStatic])()
        elif(self.cardType=="enchantment"):
            oracleText+=random.choice([self.createTrigger,self.createStatic])()
        elif(self.cardType=="sorcery"):
            oracleText+=random.choice([self.createDoSomething])()
        elif(self.cardType=="instant"):
            oracleText+=random.choice([self.createDoSomething])()
        return f"{oracleText}"
    def createTrigger(self):
        possibleAbilities=[abilityF for abilityF in triggeredAbilities if (abilityF().requirements(self) and self.color in abilityF().colors)]
        if(possibleAbilities):
            
            ab=random.choice(possibleAbilities)()
            return ab.outputLambda(ab,self)+self.createDoSomething()
        else:
            return ""
    def createStatic(self):

        return "all something have nothing"
    def createActivated(self):

        return "{cost}: "+self.createDoSomething()
    def createDoSomething(self):
        possibleAbilities=[abilityF for abilityF in positiveStuff if (abilityF().requirements(self) and self.color in abilityF().colors)]
        if(possibleAbilities):
            
            ab=random.choice(possibleAbilities)()
            return ab.outputLambda(ab,self)
        else:
            return ""
        return "do something "+str(self.createNumeric())
    def createKeyword(self):
        possibleKeywords={key:value for (key,value) in keywords.items() if (value["requirements"](self) and self.color in value["colors"])}
        if(possibleKeywords):
            
            kw=random.choice(list(possibleKeywords.keys()))
            return kw
        else:
            return ""
    def createPT(self):
        if(self.cardType=="creature"):
            allocated=max(random.randint(random.randint(self.cmc,self.cmc*2),self.cmc*2+self.cmc//2),1)
            p,t=0,0
            for k in range(allocated):
                if(random.random()>0.5):
                    p+=1
                else:
                    t+=1
            if(t==0):
                t+=1
                p-=1
            return f"{p}/{t}"
        else:
            return ""
print(Card(cardType="creature").toString())

