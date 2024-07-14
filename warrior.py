from random import randint,choice,random as chance
from os import system
yes=True
def clear():
    if yes:
        system("cls")
characters=[dict(name="Scaven",hp=3700,deffence=90,attack=420,luck=2,ability="Special Attack",classed="Slayer"),
            dict(name="Vortex",hp=4300,deffence=130,attack=370,luck=2,ability="Special Deffence",classed="Guardian"),
            dict(name="Aurora",hp=4000,deffence=110,attack=400,luck=2,ability="Battle Healer",classed="Oracle"),
            dict(name="Shadow",hp=3900,deffence=100,attack=420,luck=2,ability="Accuracte Hitter",classed="Scout"),
            dict(name="Clover",hp=3800,deffence=105,attack=410,luck=4,ability="Luck Collector",classed="Gambler")]
for _ in range(len(characters)):
    idol=characters[_]
    print(f"{_+1}. ",end='')
    for __ in idol:
        print(f"{__.capitalize()}:{idol[__]} ",end='| ')
    print()
idol=characters[int(input("Index of the Character you want:"))-1]
clear()
stats=""
print(f"__________Character__________")
for key,value in idol.items():
    print(f"{key.capitalize()}:{str(value).capitalize()}")
print(f"\n\n___________Weapon___________")
weapons=[dict(name="Mace",attack=14,deffence=8),dict(name="Sword",attack=17,deffence=5),dict(name="Axe",attack=11,deffence=11)]
for _ in range(len(weapons)):
    w=weapons[_]
    print(f"{_+1}. ",end='')
    for __ in w:
        print(f"{__.capitalize()}:{w[__]} ",end='| ')
    print()
weapon=weapons[int(input("Index of the Weapon you want:"))-1]
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
        self.max_luck=6 if classed.lower()=='gambler' else 4
        self.level=7
        self.gold=0
        self.xp=0
        self.weapon=weapon
        self.weapon['level']=1
        self.weapon['cost']=1000
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
def Armoury(player):
    pass
def Shop(player):
    while True:
        if store:=input("(e) to Exit-Shop\n-->")=='e':
            break
def UseItems(player):
    pass
enemies = {1: [dict(name="Goblin",hp=(1200,1500),attack=(150,180),deffence=(60,80),sp_attack=(40,60),sp_deffence=(30,50),gold=(50,100),xp=(30,50)),dict(name="Skeleton",hp=(800,1000),attack=(120,140),deffence=(50,70),sp_attack=(30,50),sp_deffence=(20,40),gold=(30,60),xp=(20,40)),dict(name="Imp",hp=(1000,1200),attack=(130,160),deffence=(55,75),sp_attack=(35,55),sp_deffence=(25,45),gold=(40,80),xp=(25,45)),dict(name="Bandit",hp=(1200,1400),attack=(140,170),deffence=(58,78),sp_attack=(38,58),sp_deffence=(28,48),gold=(45,90),xp=(28,48))],2: [dict(name="Orc",hp=(1600,1900),attack=(180,230),deffence=(70,90),sp_attack=(50,70),sp_deffence=(40,60),gold=(100,150),xp=(70,100)),dict(name="Dark Elf",hp=(1400,1800),attack=(200,240),deffence=(60,80),sp_attack=(40,60),sp_deffence=(30,50),gold=(100,150),xp=(60,90)),dict(name="Hobgoblin",hp=(1500,1900),attack=(190,220),deffence=(65,85),sp_attack=(45,65),sp_deffence=(35,55),gold=(110,160),xp=(65,95)),dict(name="Slime",hp=(1300,1600),attack=(140,170),deffence=(50,70),sp_attack=(35,55),sp_deffence=(25,45),gold=(60,110),xp=(35,60))],3: [dict(name="Troll",hp=(2100,2500),attack=(220,270),deffence=(80,100),sp_attack=(50,70),sp_deffence=(40,60),gold=(140,200),xp=(90,130)),dict(name="Werewolf",hp=(1900,2300),attack=(200,250),deffence=(70,90),sp_attack=(50,70),sp_deffence=(30,50),gold=(120,180),xp=(80,120)),dict(name="Harpy",hp=(1800,2200),attack=(210,260),deffence=(75,95),sp_attack=(45,65),sp_deffence=(35,55),gold=(130,190),xp=(85,125)),dict(name="Zombie",hp=(1700,2100),attack=(190,240),deffence=(70,90),sp_attack=(40,60),sp_deffence=(30,50),gold=(110,170),xp=(75,110))],4: [dict(name="Lich",hp=(2400,2800),attack=(250,290),deffence=(100,120),sp_attack=(70,90),sp_deffence=(50,70),gold=(150,250),xp=(120,170)),dict(name="Vampire",hp=(2200,2600),attack=(240,280),deffence=(90,110),sp_attack=(60,80),sp_deffence=(40,60),gold=(140,210),xp=(100,140)),dict(name="Dwarf Berserker",hp=(2000,2400),attack=(230,270),deffence=(85,105),sp_attack=(55,75),sp_deffence=(35,55),gold=(130,200),xp=(90,130)),dict(name="Witch",hp=(2300,2700),attack=(250,290),deffence=(90,110),sp_attack=(65,85),sp_deffence=(40,60),gold=(160,230),xp=(110,150))],5: [dict(name="Griffin",hp=(3200,3600),attack=(320,370),deffence=(90,110),sp_attack=(80,100),sp_deffence=(50,70),gold=(250,350),xp=(170,220)),dict(name="Hydra",hp=(3000,3400),attack=(310,360),deffence=(80,100),sp_attack=(70,90),sp_deffence=(40,60),gold=(230,320),xp=(160,210)),dict(name="Golem",hp=(2800,3200),attack=(300,350),deffence=(75,95),sp_attack=(65,85),sp_deffence=(35,55),gold=(210,300),xp=(140,190)),dict(name="Basilisk",hp=(2900,3300),attack=(305,355),deffence=(80,100),sp_attack=(68,88),sp_deffence=(40,60),gold=(220,310),xp=(150,200))],6: [dict(name="Phoenix",hp=(3400,3600),attack=(320,370),deffence=(90,110),sp_attack=(70,90),sp_deffence=(40,60),gold=(200,350),xp=(100,150)),dict(name="Minotaur",hp=(3200,3400),attack=(330,380),deffence=(100,120),sp_attack=(75,95),sp_deffence=(45,65),gold=(180,270),xp=(120,170)),dict(name="Yeti",hp=(3100,3300),attack=(325,375),deffence=(95,115),sp_attack=(73,93),sp_deffence=(43,63),gold=(170,260),xp=(110,160)),dict(name="Centaur",hp=(3300,3500),attack=(335,385),deffence=(100,120),sp_attack=(77,97),sp_deffence=(45,65),gold=(190,280),xp=(130,180))],7: [dict(name="Ancient Dragon",hp=(4000,4400),attack=(370,420),deffence=(110,130),sp_attack=(90,110),sp_deffence=(50,70),gold=(300,400),xp=(200,250)),dict(name="Behemoth",hp=(3800,4200),attack=(360,410),deffence=(100,120),sp_attack=(80,100),sp_deffence=(50,70),gold=(280,380),xp=(190,240)),dict(name="Chimera",hp=(3600,4000),attack=(350,400),deffence=(95,115),sp_attack=(75,95),sp_deffence=(45,65),gold=(260,360),xp=(180,230)),dict(name="Sphinx",hp=(3700,4100),attack=(355,405),deffence=(100,120),sp_attack=(78,98),sp_deffence=(45,65),gold=(270,370),xp=(185,235))]}
player=player(idol['name'],idol['hp'],idol['deffence'],idol['attack'],idol['classed'],idol['luck'],weapon)
while player.alive():
    beast=choice(enemies[player.level] if player.level<7 else enemies[4]+enemies[5]+enemies[6]+enemies[7])
    beast=enemy(beast['name'],randint(*beast['hp']),randint(*beast['deffence']),randint(*beast['attack']),randint(*beast['sp_deffence']),randint(*beast['sp_attack']),player.luckify(beast['gold']),player.luckify(beast['xp']))
    print(f"Beast appeard, {beast.name} !\nHealth: {beast.hp}\nAttack: {beast.attack}\nSp.Attack: {beast.sp_attack}\nDeffence: {beast.deffence}\nSp. Deffence: {beast.sp_deffence}")
    while beast.alive():
        usr=input("\n\nPress :\n(a) to Attack\n(u) to use Potions\n(m) to go to Armoury\n(s) to go to Shop\n-->")
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
        elif usr=='s':
            Shop(player)
        elif usr=='m':
            Armoury(player)
        elif usr=='u':
            UseItems(player)
def endgame(score):
    with open("HighScore.txt",'w+') as hi:
        if hs:=int(hi.read())<score:
            print(f"New High Score: {score} !!! ")
            hi.write(str(score))
        else:
            print(f"Score: {score}\nHigh Score: {hs}")
print("Game Over !")
endgame(player.score)
input()
