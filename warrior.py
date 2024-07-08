from random import randint,choice,random as chance
characters=[dict(name="Scaven",hp=2137,deffence=198,attack=341,sp_attack=49,sp_deffence=21,classed="Slayer",ability="Special Attack",luck=1),
            dict(name="Vortex",hp=2581,deffence=259,attack=292,sp_attack=22,sp_deffence=47,classed="Guardian",ability="Special Deffence",luck=1),
            dict(name="Aurora",hp=2326,deffence=228,attack=312,sp_attack=27,sp_deffence=30,classed="Oracle",ability="Battle Healer",luck=1),
            dict(name="Shadow",hp=2300,deffence=230,attack=329,sp_attack=31,sp_deffence=28,classed="Scout",ability="Critical Hit",luck=1),
            dict(name="Clover",hp=2237,deffence=213,attack=321,sp_attack=24,sp_deffence=29,classed="Gambler",ability="Luck Collector",luck=3)]
for _ in range(len(characters)):
    idol=characters[_]
    print(f"{_+1}. ",end='')
    for __ in idol:
        print(f"{__.capitalize()}: {idol[__]} ",end='| ')
    print()
idol=characters[int(input("Index of the Character you want: "))-1]
class player:
    def __init__(self,name,hp,deffence,attack,sp_deffence,sp_attack,classed,luck):
        self.name=name
        self.hp=hp
        self.max_hp=hp
        self.attack=attack
        self.deffence=deffence
        self.sp_deffence=sp_deffence
        self.sp_attack=sp_attack
        self.classed=classed
        self.luck=luck
        self.gold=0
        self.xp=0
        self.weapon=dict(level=1,name='sword')
        self.armoury=dict(level=1,health=500,max_health=500)
        self.potions=[]
    def dodge(self):
        return chance()<(((self.luck+1)/2)*0.0162)
    def luckify(self,loot):
        return round(randint(*loot)*((self.luck/100)+1.2),0)
class enemy:
    def __init__(self,name,hp,deffence,attack,gold,xp):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.deffence=deffence
        self.gold=gold
        self.xp=xp
    def dodge(self):
        return chance()<=0.04
def shop(player):
    while True:
        store=input("Press :\n(a) for Armoury\n(p) for Potions\n(e) for Exit-Shop\n-->").lower()
        if store=='a':
            print(f"{'__'*10}Weapons{'__'*10}\n{player.weapon['name'].capitalize()}")
        if store=='e':
            break
enemies=[dict(name="Phoenix",hp=(4200,4500),attack=(250,300),deffence=(30,50),gold=(200,350),xp=(100,150))]
player=player(idol['name'],idol['hp'],idol['deffence'],idol['attack'],idol['sp_deffence'],idol['sp_attack'],idol['classed'],idol['luck'])
while True:
    beast=choice(enemies)
    beast=enemy(beast['name'],beast['hp'],beast['deffence'],beast['attack'],player.luckify(beast['gold']),player.luckify(beast['xp']))
    break
