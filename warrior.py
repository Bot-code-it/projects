from random import randint,choice,random as chance
from os import system
yes=False
def clear():
    if yes==True:
        system("cls")
characters=[dict(name="Scaven",hp=2137,deffence=71,attack=341,luck=1,ability="Special Attack",classed="Slayer"),
            dict(name="Vortex",hp=2581,deffence=98,attack=292,luck=1,ability="Special Deffence",classed="Guardian"),
            dict(name="Aurora",hp=2326,deffence=87,attack=312,luck=1,ability="Battle Healer",classed="Oracle"),
            dict(name="Shadow",hp=2300,deffence=76,attack=329,luck=1,ability="Skill",classed="Scout"),
            dict(name="Clover",hp=2237,deffence=80,attack=321,luck=3,ability="Luck Collector",classed="Gambler")]
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
    def __init__(self,name,hp,deffence,attack,classed,luck,weapon):
        maxed={"Slayer":[1.2,1.3],"Guardian":[1.3,1.2],"Oracle":[1.27,1.23],"Scout":[1.23,1.27],"Gambler":[1.25,1.25]}
        self.name=name
        self.hp=hp
        self.max_hp=hp
        self.attack=attack
        self.max_attack=attack*maxed[classed][1]
        self.deffence=deffence
        self.max_deffence=deffence*maxed[classed][0]
        self.classed=classed
        self.luck=luck
        self.max_luck=luck
        self.level=1
        self.gold=0
        self.xp=0
        self.weapon=weapon
        self.weapon['level']=1
        self.weapon['cost']=1000
        self.armour=dict(level=1,hp=300,max_hp=300,cost=1000)
        self.upgrade_list=[0,0,500,750,850,900,950,1000,1050,1100,1200]
        self.costing
        self.potions=[]
        self.maxed=dict(armour=False,weapon=False,deffence=False,attack=False,luck=False)
    def dodge(self):
        return chance()<0.06
    def luckify(self,loot):
        return round(randint(*loot)*((self.luck/100)+1.2),0)
    def alive(self):
        return self.hp>0
    def critical(self):
        num=0.07
        if self.classed.lower()=='scout':
            num=0.09
        return chance()<=num
    def level_up(self):
        pass
    def attack(self):
        attack=randint(((self.attack*35)//100),self.attack)
        weaponized=randint(((self.weapon['attack']*50)//100),self.weapon['attack'])
        total=attack+weaponized
        crit=''
        if self.critical():
            crit+="Critical hit !\n"
            total=(total*140)//100
        print(f"Attack strength : {attack}\nWeapon strength : {weaponized}\n{crit}Total strength : {total}")
        return total
    def take_dmg(self,dmg):
        if self.dodge():
            print("Attack dodged !")
            return False
        deffence=randint(((self.deffence*35)//100),self.deffence)
        weaponized=randint(((self.weapon['deffence']*50)//100),self.weapon['deffence'])
        dmg=dmg-(deffence+weaponized)
        if dmg<=0:
            print(f"Damage taken by {self.name.capitalize()} : 0")
            return 0
        arm=dmg//10
        if self.armour['hp']>=arm:
            print(f"Damage absorbed by armour : {arm}")
            self.armour['hp']-=arm
            return dmg-arm
        arm-=self.armour['hp']
        self.armour['hp']=0
        print(f"Damage absorbed by armour : {arm}")
        self.hp-=(dmg-arm)
        print(f"Damage caused : {dmg-arm}")
        return True
    def upgrade_weapon(self):
        if self.weapon['level']==10:
            self.maxed['armour']=True
            return False
        elif self.weapon['cost']>self.gold:
            return
        self.gold-=self.weapon['cost']
        self.weapon['level']+=1
        self.weapon['cost']=((self.weapon['cost']*115)//100)
        self.weapon['attack']+=1
        self.weapon['deffence']+=1
        return True
    def upgrade_armour(self):
        if self.armour['level']==10:
            self.maxed['armour']=True
            return False
        elif self.armour['cost']>self.gold:
            return
        self.gold-=self.armour['cost']
        self.armour['level']+=1
        self.armour['cost']=((self.armour['cost']*115)//100)
        health={i:((self.armour['max_hp']*i)//100) for i in [10,20,30,40,50,60,70,80,90,100]}
        self.armour['max_hp']=self.upgrade_list[self.armour['level']]
        for per,hp in health.items():
            if hp>=self.armour['hp']:
                self.armour['hp']=((self.armour['max_hp']*per)//100)
                break
        return True
    def mend_armour(self):
        if self.armour['max_hp']==self.armour['hp']:
            return False
        num=self.armour['max_hp']//10
        if self.armour['hp']+num>=self.armour['max_hp']:
            self.armour['hp']=self.armour['max_hp']
        else:
            self.armour['hp']+=num
        return True
class enemy:
    def __init__(self,name,hp,deffence,attack,sp_deffence,sp_attack,gold,xp):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.deffence=deffence
        self.sp_attack=sp_attack
        self.sp_deffence=sp_deffence
        self.gold=gold
        self.xp=xp
    def dodge(self):
        return chance()<=0.055
    def alive(self):
        return self.hp>0
    def critical(self):
        return chance()<=0.065
    def attack(self):
        attack=randint(((self.attack*50)//100))
        sp_attack=randint(((self.attack*80)//100))
        total=sp_attack+attack
        crit=''
        if self.critical():
            crit+='Critical hit !\n'
            total=(total*140)//100
        print(f"Attack strength : {attack}\nSpecial attack strength : {sp_attack}\n{crit}Total strength : {total}")
        return total
    def take_dmg(self,dmg):
        pass
def shop(player):
    while True:
        store=input("Press :\n(a) for Armoury\n(p) for Potions\n(i) for Items\n(e) for Exit-Shop\n-->").lower()
        if store=='a':
            print(f"{'__'*10}Weapons{'__'*10}\n{player.weapon['name'].capitalize()}")
        if store=='e':
            break
enemies=[dict(name="Phoenix",hp=(4200,4500),attack=(250,300),deffence=(30,50),sp_attack=(50,70),sp_deffence=(20,30),gold=(200,350),xp=(100,150))]
player=player(idol['name'],idol['hp'],idol['deffence'],idol['attack'],idol['classed'],idol['luck'],weapon)
while player.alive():
    beast=choice(enemies)
    beast=enemy(beast['name'],randint(*beast['hp']),randint(*beast['deffence']),randint(*beast['attack']),randint(*beast['sp_deffence']),randint(*beast['sp_attack']),player.luckify(beast['gold']),player.luckify(beast['xp']))
    break
