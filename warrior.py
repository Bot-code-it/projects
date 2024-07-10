from random import randint,choice,random as chance
from os import system 
def clear():
    system("cls")
characters=[dict(name="Scaven",hp=2137,deffence=198,attack=341,sp_attack=49,sp_deffence=21,luck=1,ability="Special Attack",classed="Slayer"),
            dict(name="Vortex",hp=2581,deffence=259,attack=292,sp_attack=22,sp_deffence=47,luck=1,ability="Special Deffence",classed="Guardian"),
            dict(name="Aurora",hp=2326,deffence=228,attack=312,sp_attack=27,sp_deffence=30,luck=1,ability="Battle Healer",classed="Oracle"),
            dict(name="Shadow",hp=2300,deffence=230,attack=329,sp_attack=31,sp_deffence=28,luck=1,ability="Critical Hit",classed="Scout"),
            dict(name="Clover",hp=2237,deffence=213,attack=321,sp_attack=24,sp_deffence=29,luck=3,ability="Luck Collector",classed="Gambler")]
for _ in range(len(characters)):
    idol=characters[_]
    print(f"{_+1}. ",end='')
    for __ in idol:
        print(f"{__.capitalize()}: {idol[__]} ",end='| ')
    print()
idol=characters[int(input("Index of the Character you want: "))-1]
clear()
stats=""
print(f"__________Character__________")
for key,value in idol.items():
    print(f"{key.capitalize()}: {str(value).capitalize()}")
print(f"\n\n___________Weapon___________")
weapons=[dict(name="Mace",attack=14,deffence=8),dict(name="Sword",attack=17,deffence=5),dict(name="Axe",attack=11,deffence=11)]
for _ in range(len(weapons)):
    w=weapons[_]
    print(f"{_+1}. ",end='')
    for __ in w:
        print(f"{__.capitalize()}: {w[__]} ",end='| ')
    print()
weapon=weapons[int(input("Index of the Weapon you want: "))-1]
clear()
class player:
    def __init__(self,name,hp,deffence,attack,sp_deffence,sp_attack,classed,luck,weapon):
        maxed={"Slayer":[1.2,1.3],"Guardian":[1.3,1.2],"Oracle":[1.27,1.23],"Scout":[1.23,1.27],"Gambler":[1.25,1.25]}
        self.name=name
        self.hp=hp
        self.max_hp=hp
        self.attack=attack
        self.max_attack=attack*maxed[classed][1]
        self.sp_attack=sp_attack
        self.max_sp_attack=attack*maxed[classed][1]
        self.deffence=deffence
        self.max_deffence=deffence*maxed[classed][0]
        self.sp_deffence=sp_deffence
        self.max_sp_deffence=deffence*maxed[classed][0]
        self.classed=classed
        self.luck=luck
        self.level=1
        self.gold=0
        self.xp=0
        self.weapon=weapon
        self.weapon['level']=1
        self.weapon['cost']=1000
        self.armour=dict(level=1,hp=300,max_hp=300,cost=1000)
        self.upgrade_list=[0,0,500,750,850,900,950,1000,1050,1100,1200]
        
        self.potions=[]
    def dodge(self):
        return chance()<(((self.luck+1)/2)*0.016)
    def luckify(self,loot):
        return round(randint(*loot)*((self.luck/100)+1.2),0)
    def alive(self):
        return self.hp>0
    def crirtical(self):
        return chance()<=0.009
    def level_up(self):
        pass
    def upgrade_weapon(self):
        self.weapon['level']+=1
        self.weapon['cost']=((self.weapon['cost']*115)//100)
        self.weapon['attack']+=1
        self.weapon['deffence']+=1
    def upgrade_armour(self):
        self.armour['level']+=1
        self.armour['cost']=((self.armour['cost']*115)//100)
        health={i:((self.armour['max_hp']*i)//100) for i in [10,20,30,40,50,60,70,80,90,100]}
        self.armour['max_hp']=self.upgrade_list[self.armour['level']]
        for per,hp in health:
            if hp>=self.armour['hp']:
                self.armour['hp']=((self.armour['max_hp']*per)//100)
                break
    def mend_armour(self):
        pass
class enemy:
    def __init__(self,name,hp,deffence,attack,gold,xp):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.deffence=deffence
        self.gold=gold
        self.xp=xp
    def dodge(self):
        return chance()<=0.035
    def alive(self):
        return self.hp>0
    def crirtical(self):
        return chance()<=0.009
def shop(player):
    while True:
        store=input("Press :\n(a) for Armoury\n(p) for Potions\n(i) for Items\n(e) for Exit-Shop\n-->").lower()
        if store=='a':
            print(f"{'__'*10}Weapons{'__'*10}\n{player.weapon['name'].capitalize()}")
        if store=='e':
            break
enemies=[dict(name="Phoenix",hp=(4200,4500),attack=(250,300),deffence=(30,50),gold=(200,350),xp=(100,150))]
player=player(idol['name'],idol['hp'],idol['deffence'],idol['attack'],idol['sp_deffence'],idol['sp_attack'],idol['classed'],idol['luck'],weapon)
while True:
    beast=choice(enemies)
    beast=enemy(beast['name'],randint(*beast['hp']),randint(*beast['deffence']),randint(*beast['attack']),player.luckify(beast['gold']),player.luckify(beast['xp']))
    break
