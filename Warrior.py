from random import randint,choice,random as chance
from os import system
yes=False
def clear():
    if yes:
        system("cls")
def Start():
    characters = [dict(name="Scaven",hp=3700,deffence=90,attack=420,luck=2,ability="Special Attack",classed="Slayer"),
    dict(name="Ragnar",hp=3600,deffence=85,attack=430,luck=3,ability="Special Attack",classed="Slayer"),
    dict(name="Thorne",hp=3800,deffence=95,attack=410,luck=2,ability="Special Attack",classed="Slayer"),
    dict(name="Vortex",hp=4300,deffence=130,attack=370,luck=2,ability="Special Deffence",classed="Guardian"),
    dict(name="Aegis",hp=4200,deffence=125,attack=380,luck=3,ability="Special Deffence",classed="Guardian"),
    dict(name="Titan",hp=4400,deffence=135,attack=360,luck=2,ability="Special Deffence",classed="Guardian"),
    dict(name="Aurora",hp=4000,deffence=110,attack=400,luck=2,ability="Battle Healer",classed="Oracle"),
    dict(name="Celeste",hp=3900,deffence=105,attack=410,luck=3,ability="Battle Healer",classed="Oracle"),
    dict(name="Lumia",hp=4100,deffence=115,attack=390,luck=2,ability="Battle Healer",classed="Oracle"),
    dict(name="Shadow",hp=3900,deffence=100,attack=420,luck=2,ability="Accuracte Hitter",classed="Scout"),
    dict(name="Nyx",hp=3800,deffence=95,attack=430,luck=3,ability="Accuracte Hitter",classed="Scout"),
    dict(name="Wraith",hp=4000,deffence=105,attack=410,luck=2,ability="Accuracte Hitter",classed="Scout"),
    dict(name="Clover",hp=3800,deffence=105,attack=410,luck=4,ability="Luck Collector",classed="Gambler"),
    dict(name="Fortune",hp=3700,deffence=100,attack=420,luck=5,ability="Luck Collector",classed="Gambler"),
    dict(name="Dice",hp=3900,deffence=110,attack=400,luck=4,ability="Luck Collector",classed="Gambler")]
    max_name = max(len(char['name']) for char in characters)
    max_ability = max(len(char['ability']) for char in characters)
    for i,char in enumerate(characters,start=1):
        print(f"{0 if i<10 else ''}{i}. Name: {char['name']:<{max_name}} | Hp: {char['hp']} | Deffence:{0 if char['deffence']<100 else ''}{char['deffence']} | Attack: {char['attack']} | Luck: {char['luck']} | Ability: {char['ability']:<{max_ability}} | Classed: {char['classed']}")
    idol=characters[int(input("Index of the Character you want:"))-1]
    clear()
    stats=""
    print(f"__________Character__________")
    for key,value in idol.items():
        print(f"{key.capitalize()}:{str(value).capitalize()}")
    print(f"\n\n___________Weapon___________")
    weapons=[dict(name="Mace",attack=14,deffence=8),dict(name="Sword",attack=17,deffence=5),dict(name="Axe",attack=11,deffence=11)]
    max_name = max(len(char['name']) for char in characters)
    max_ability = max(len(char['ability']) for char in characters)
    for _ in range(len(weapons)):
        w=weapons[_]
        print(f"{_+1}. ",end='')
        for __ in w:
            print(f"{__.capitalize()}:{w[__]} ",end='| ')
        print()
    weapon=weapons[int(input("Index of the Weapon you want:"))-1]
    clear()
    return idol,weapon
class DATA:
    def __init__(self):
        self.data={}
        with open("Data/Memory/Resume.txt") as data:
            if saved:=data.read()=='':
                return
            for i in saved.split(";"):
                s=i.split("=")
                self.data[s[0]]=s[1]
    def update(self,name,classed,hp,attack,deffence,luck,level,gold,xp,score,armour_level,armour_hp,weapon_level,potions):
        pass
    def clear(self):
        with open("data.txt",'w') as f:
            f.write("")
class Player:
    def __init__(self,name,hp,deffence,attack,classed,luck,weapon,updated=False):
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
        self.max_luck=6 if classed.lower()=='gambler' else 4
        self.level=1
        self.gold=0
        self.xp=0
        self.weapon=weapon
        if updated:
            self.weapon['level']=1
            self.weapon['cost']=1000
            self.armour=dict(level=1,hp=300,max_hp=300,cost=1000)
        else:
            self.armour=dict(level=1,hp=300,max_hp=300,cost=1000)
        self.upgrade_list=[0,0,500,750,850,900,950,1000,1050,1100,1200]
        self.potions=[]
        self.score=0
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
    def gen_attack(self):
        attack=randint(((self.attack*35)//100),self.attack)
        weaponized=randint(((self.weapon['attack']*50)//100),self.weapon['attack'])
        total=attack+weaponized
        crit=''
        if self.critical():
            crit+="Critical hit !\n"
            total=(total*140)//100
        print(f"Attack strength : {attack}\nWeapon strength : {weaponized}\n{crit}Total attack strength : {total}")
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
        else:
            print(f"Damage deffended : {dmg}")
        arm=dmg//10
        if self.armour['hp']>=arm:
            print(f"Damage absorbed by armour : {arm}")
            self.armour['hp']-=arm
            self.hp-=(dmg-arm)
            print(f"Damage caused to {self.name} : {dmg-arm}")
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
class Enemy:
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
    def gen_attack(self):
        attack=randint(((self.attack*50)//100),self.attack)
        sp_attack=randint(((self.sp_attack*80)//100),self.sp_attack)
        total=sp_attack+attack
        crit=''
        if self.critical():
            crit+='Critical hit !\n'
            total=(total*140)//100
        print(f"Attack strength : {attack}\nSpecial attack strength : {sp_attack}\n{crit}Total attack strength : {total}")
        return total
    def take_dmg(self,dmg):
        if self.dodge():
            print("Attack dodged !")
            return False
        deffence=randint(((self.deffence*35)//100),self.deffence)
        print(f"Damage deffended : {deffence}")
        sp_deffence=randint(((self.sp_deffence*50)//100),self.sp_deffence)
        print(f"Special deffence : {sp_deffence}")
        dmg-=(deffence+sp_deffence)
        if dmg<=0:
            print(f"Damage caused to {self.name.capitalize()} : 0")
            return            
        print(f"Damage caused to {self.name.capitalize()} : {dmg}")
        self.hp-=dmg
        return True
def Weaponry(player):
    print(f"{'__'*6}Weaponry{'__'*6}\n")
def Armoury(player):
    pass
def Shop(player):
    while True:
        if store:=input("(e) to Exit-Shop\n-->")=='e':
            break
def UseItems(player):
    pass
def in_fight(player):
        beast=choice(enemies[player.level] if player.level<7 else enemies[4]+enemies[5]+enemies[6]+enemies[7])
        beast=Enemy(beast['name'],randint(*beast['hp']),randint(*beast['deffence']),randint(*beast['attack']),randint(*beast['sp_deffence']),randint(*beast['sp_attack']),player.luckify(beast['gold']),player.luckify(beast['xp']))
        print(f"Beast appeard, {beast.name} !\nHealth: {beast.hp}\nAttack: {beast.attack}\nSp.Attack: {beast.sp_attack}\nDeffence: {beast.deffence}\nSp. Deffence: {beast.sp_deffence}")
        while beast.alive():
            usr=input("\n\nPress :\n(a) to Attack\n(u) to use Potions\n")
            clear()
            if usr=='a':
                print(f"{player.name} is attacking {beast.name} !\n ")
                beast_dmg=player.gen_attack();print()
                beast.take_dmg(beast_dmg)
                if beast.alive() is False:
                    clear()
                    print(f"{beast.name} is dead !\nXP earned : {beast.xp}\nGold looted : {beast.gold}")
                    player.xp+=beast.xp
                    player.gold+=beast.gold
                    input("Press any key to continue...")
                    clear()
                    break
                print("__"*18)
                print(f"{beast.name} is attacking {player.name} !\n ")
                player_dmg=beast.gen_attack();print()
                player.take_dmg(player_dmg)
                if player.alive() is False:
                    break
                print("__"*18)
                print(f"\n{player.name}'s health: {player.hp}\n{beast.name}'s health: {beast.hp}")
            elif usr=='u':
                UseItems(player)
def RPG(idol,weapon):
    player=Player(idol['name'],idol['hp'],idol['deffence'],idol['attack'],idol['classed'],idol['luck'],weapon)
    while player.alive():
        usr=input("Press :\n(s) to go to Shop\n(a) to go to Armoury\n(w) to go to Weaponry\n(t) for Traveling\n(e) to explore\n-->")
        clear()
        if usr=='a':
            in_fight(player,)
        
def endgame():
    print("Game Over !")
    with open("HighScore.txt",'w+') as hi:
        if hs:=int(hi.read())<score:
            print(f"New High Score: {score} !!! ")
            hi.write(str(score))
        else:
            print(f"Score: {score}\nHigh Score: {hs}")
    input()
Data=DATA()
RPG(*Start())
endgame()
