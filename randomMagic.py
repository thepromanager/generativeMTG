import random

def isCreature(x):
    return x.cardType=="creature"
def noReq(x):
    return True
def getNbr(x):
    return x.createNumeric()
def lazyAbility(**kwargs):
    def abilityFunction():
        return Ability(**kwargs) 
    return abilityFunction
def plural(text,quantity):
    if(quantity>1):
        return text
    else:
        return ""
def singular(text,quantity):
    if(quantity==1):
        return text
    else:
        return ""
def choiceFunction(choices):
    def cf():
        return random.choice(choices)
    return cf
colors=["w","u","b","r","g"]
rarities=["common","uncommon","rare","mythic rare"]
cardTypes=["creature","instant","sorcery","enchantment","planeswalker","artifact","land"]
keywords={
    "Flash":{"power":2,"requirements":isCreature,"colors":"u","cost":None,"number":None,"afterEffect":None},
    "Reach":{"power":1,"requirements":isCreature,"colors":"g","cost":None,"number":None,"afterEffect":None},
    #"Shroud":{"power":1,requirements:lambda x:x.cardType=="creature",cost:None,"number":None,"afterEffect":None}
    "Trample":{"power":1,"requirements":isCreature,"colors":"gr","cost":None,"number":None,"afterEffect":None},
    "Vigilance":{"power":1,"requirements":isCreature,"colors":"uw","cost":None,"number":None,"afterEffect":None},
    "Menace":{"power":1,"requirements":isCreature,"colors":"br","cost":None,"number":None,"afterEffect":None},
    "Double strike":{"power":3,"requirements":isCreature,"colors":"wr","cost":None,"number":None,"afterEffect":None},
    # maybe power:lambda x:x.power*2
    "First strike":{"power":1,"requirements":isCreature,"colors":"wb","cost":None,"number":None,"afterEffect":None},
    "Deathtouch":{"power":2,"requirements":isCreature,"colors":"bg","cost":None,"number":None,"afterEffect":None},
    "Defender":{"power":-2,"requirements":isCreature,"colors":"wubg","cost":None,"number":None,"afterEffect":None},
    "Flying":{"power":2,"requirements":isCreature,"colors":"wubr","cost":None,"number":None,"afterEffect":None},
    "Haste":{"power":1,"requirements":isCreature,"colors":"rgb","cost":None,"number":None,"afterEffect":None},
    "Hexproof":{"power":3,"requirements":isCreature,"colors":"wug","cost":None,"number":None,"afterEffect":None},
    #"Indestructible":{"power":5,requirements:lambda x:x.cardType=="creature",cost:None,"number":None,"afterEffect":None}
    "Intimidate":{"power":1,"requirements":isCreature,"colors":"b","cost":None,"number":None,"afterEffect":None},
    "Lifelink":{"power":1,"requirements":isCreature,"colors":"wb","cost":None,"number":None,"afterEffect":None},
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
        outputLambda=lambda ab,card:f"{ab.targets[0]}draw{'s'*(not not ab.targets[0])} {singular('a',ab.number)}{plural(str(ab.number),ab.number)} card{plural('s',ab.number)}.",
        targetReqs=["player"],
        ),
    lazyAbility(name="scry",colors="wubrg",),
    lazyAbility(name="search",colors="wubrg",
        power=3,
        number=lambda x:x.createNumeric(bound=2),
        outputLambda=lambda ab,card:f"{ab.targets[0]}search{'es'*(not not ab.targets[0])} {ab.targets[1]} library for {singular('a',ab.number)}{plural(str(ab.number),ab.number)} {ab.targets[2]} card{plural('s',ab.number)}.",
        targetReqs=["player","player","cardType","zone"],
        ),
    ]

class Ability():
    def __init__(self,name="",colors="wubrg",power=1,powerLambda=(lambda ab,card:ab.number*ab.power*ab.scope),requirements=noReq,cost=None,number=getNbr,outputLambda=(lambda ab,card:f"{ab.name} {ab.number}"),scope=1,targetReqs=[]):
        self.name,self.colors,self.power,self.scope=name,colors,power,scope
        if(cost):
            pass
        if(requirements):
            self.requirements=requirements
        if(number):
            self.number=number(self)
        if(targetReqs):
            self.targets=self.getTargets(targetReqs)
        if(powerLambda):
            self.powerLambda=powerLambda
        if(outputLambda):
            self.outputLambda=outputLambda
        

    def getPower(self,card):
        return self.powerLambda(self,card)
    def getTargets(self,targetReqs):
        targets=[]
        for target in targetReqs:
            if(isinstance(target,str)):
                #target=targetNames[target]
                pass
            if(callable(target)):
                target=target()
            if(isinstance(target,tuple)):
                targets.append(target[0])
                self.scope*=target[1]            

        return targets
    def getOutput(self,card):

        return self.outputLambda(self,card)

    def createNumeric(self,bound=5):
        nbr = random.randint(1,random.randint(1,bound))
        return nbr

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
        self.points=max(2*self.cmc+rarities.index(self.rarity)+random.randint(0,rarities.index(self.rarity)//2+1)-1,1)
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
        self.points+=colored
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
        return "whenever something happens, "+self.createDoSomething()
    def createStatic(self):
        return "all something have nothing"
    def createActivated(self):
        return "{cost}: "+self.createDoSomething()
    def createDoSomething(self):
        possibleAbilities=[abilityF for abilityF in positiveStuff if (abilityF().requirements(self) and self.color in abilityF().colors)]
        if(possibleAbilities):
            
            ab=random.choice(possibleAbilities)()
            self.points-=ab.powerLambda(ab,self)
            print(self.points)
            return ab.outputLambda(ab,self)
        else:
            return ""
        return "do something "+str(self.createNumeric())
    def createNumeric(self):
        nbr = random.randint(1,5)
        return nbr
    def createKeyword(self):
        possibleKeywords={key:value for (key,value) in keywords.items() if (value["requirements"](self) and self.color in value["colors"])}
        if(possibleKeywords):
            
            kw=random.choice(list(possibleKeywords.keys()))
            self.points-=possibleKeywords[kw]["power"]
            return kw
        else:
            return ""
    def createPT(self):
        if(self.cardType=="creature"):
            allocated=max(random.randint(random.randint(self.cmc,self.cmc*2),self.cmc*2+self.cmc//2),1)
            self.points-=allocated
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


