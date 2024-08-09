from random import randint,choice,random as chance
from os import system
from json import loads as json
from time import sleep
from sys import modules as MODS
#@@@@
yes='idlelib' in MODS
def clear():
    if not yes:
        system("cls")
#@@@@
def ascii_art():
    SPrint(lined=True,chars=" __                                      _______\n ||        ________   _____ ________    ||‾‾‾‾‾\\\\   ______   _____   __       ___    ___   _____ \n ||       //‾‾‾‾‾‾\\\\ //‾‾‾‾ ‾‾‾||‾‾‾    ||     ||  ||‾‾‾‾‾ //‾‾‾‾‾\\\\ ||      //‾\\\\  //‾\\\\ //‾‾‾‾ \n ||       ||      || \\\\____    ||       ||_____//  ||____  ||_____|| ||      ||  \\\\//  || \\\\____ \n ||       ||      ||  ‾‾‾‾\\\\   ||       ||‾‾‾‾‾\\\\  ||‾‾‾‾  ||‾‾‾‾‾|| ||      ||   ‾‾   ||  ‾‾‾‾\\\\\n ||______ \\\\______// _____//   ||       ||      \\\\ ||_____ ||     || ||_____ ||        || _____//\n ‾‾‾‾‾‾‾‾  ‾‾‾‾‾‾‾‾  ‾‾‾‾‾‾    ‾‾       ‾‾      ‾‾ ‾‾‾‾‾‾‾ ‾‾     ‾‾ ‾‾‾‾‾‾‾ ‾‾        ‾‾ ‾‾‾‾‾‾")
    print(f"+{'-'*97}+\n")
    SPrint(lined=True,chars='\n                         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n                         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀\n                         ⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀\n                         ⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀\n                         ⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀\n                         ⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀\n                         ⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀\n                         ⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆\n                         ⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄\n                         ⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷\n                         ⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹\n                         ⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸\n                         ⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼\n                         ⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁\n                         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n                         ')
    input()
    clear()
def SPrint(chars,speed=0.055,pause_at=[],end='\n',lined=False):
    a=0
    chart=chars+f"{end}"
    if lined:
        chart=chart.split('\n')
    for i in chart:
        if lined:
            i+='\n'
        print(i,end='',flush=True)
        if i in pause_at:
            a=0.8
        sleep(speed+a)
        a=0
def SInput(chars,speed=0.055):
    for i in chars:
        print(i,end='',flush=True)
        sleep(speed)
    return input()
class DATA:
    def __init__(self,name):
        self.data={}
        self.identity=name.capitalize()
        try:
            open(f"Data/Memory/Resume/{self.identity}.txt",'x')
        except:
            pass
        with open(f"Data/Memory/Resume/{self.identity}.txt") as data:
            saved=data.read()
            print(saved)
            if saved=='':
                return
            for i in saved.split("&"):
                s=i.split("=")
                if "{" in s[1] or "[" in s[1]:
                    s[1]=json(s[1])
                self.data[s[0]]=s[1]
    def update(self,name,classed,max_hp,current_hp,attack,deffence,luck,level,gold,xp,score,armour_level,armour_hp,weapon_level,potions,quest):
        potions=str(potions).replace("'",'"')
        quest=str(quest).replace("'",'"')
        with open(f"Data/Memory/Resume/{self.identity}.txt",'w') as f:
            f.write(f"name={name}&classed={classed}&max_hp={max_hp}&curent_hp={current_hp}&attack={attack}&deffence={deffence}&luck={luck}&gold={gold}&xp={xp}&score={score}&armour_level={armour_level}&armour_hp={armour_hp}&weapon_level={weapon_level}&potions={potions}&quest={quest}")
    def clear(self):
        with open(f"Data/Memory/Resume/{self.identity}.txt",'w') as f:
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
        self.level=1
        self.gold=0
        self.xp=0
        self.weapon=weapon
        self.invetory=[]
        if updated:
            self.weapon['level']=1
            self.weapon['cost']=1000
            self.armour=dict(level=1,hp=300,max_hp=300,cost=1000)
        else:
            self.armour=dict(level=1,hp=300,max_hp=300,cost=1000)
        self.upgrade_list=[0,0,500,750,850,900,950,1000,1050,1100,1200]
        self.potions=[]
        self.score=0
        self.place=''
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
        self.loot=''
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
##talk=dict(name="Steve",options=[""],"1":)

##class NPC:
##    def __init__(self,name,talk,quest=False):
##        self.name=name
##        self.talk=talk
##        self.quest=quest
##    def interact(self,player):
##        if self.quest is False:
##            print(conv:=f"{self.name}: {choice(['Hello','Hey'])}! I'm {self.name}. {choice(['Anything I can do','How can I help you'])}?")
##            for num,opt in enumerate(talk['options'],start=1):
##                print(f"{num}. {opt}")
##            usr=input("->")
##            clear()
##            conv:=conv+f"\n{player.name}: {talk[usr]}"
##            
##        else:
##            print(f"{choice(['Hello','Hey'])}! My name is {self.name}. {choice(['Can you help me out','Can you do me a favour'])}?")
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
def in_fight(player,beast):
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
def Screen():
    usr=SInput("What would you like to do ::\n1. --Play\n2. --Resume\n\n-->",speed=0.04)
    while True:
        try:
            user=int(usr)
            if user in [1,2]:
                return (user-1)
        except:
            print('error')
        clear()
        usr=input("What would you like to do ::\n1. --Play\n2. --Resume\n\nWrong input-->")
def Start():
    characters=[dict(name="Scaven",hp=3700,deffence=90,attack=420,luck=2,ability="Special Attack",classed="Slayer"),
    dict(name="Ragnar",hp=3600,deffence=85,attack=430,luck=3,ability="Special Attack",classed="Slayer"),
    dict(name="Thorne",hp=3800,deffence=95,attack=410,luck=2,ability="Special Attack",classed="Slayer"),
    dict(name="Vortex",hp=4300,deffence=130,attack=370,luck=2,ability="Special Deffence",classed="Guardian"),
    dict(name="Aegis",hp=4200,deffence=125,attack=380,luck=3,ability="Special Deffence",classed="Guardian"),
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
        SPrint(speed=0.0001,chars=f"{0 if i<10 else ''}{i}. Name: {char['name']:<{max_name}} | Hp: {char['hp']} | Deffence:{0 if char['deffence']<100 else ''}{char['deffence']} | Attack: {char['attack']} | Luck: {char['luck']} | Ability: {char['ability']:<{max_ability}} | Classed: {char['classed']}")
    idol=characters[int(SInput("\nIndex of the Character you want:"))-1]
    clear()
    stats=""
    SPrint(f"__________Character__________",speed=0.03)
    for key,value in idol.items():
        SPrint(f"{key.capitalize()}: {str(value).capitalize()}",speed=0.03)
    SInput("\n\nPress any key to continue . . .",speed=0.03)
    clear()
    SPrint(f"\n\n__________________Weapon__________________",speed=0.03)
    weapons=[dict(name="Mace",attack=14,deffence=8),dict(name="Sword",attack=17,deffence=5),dict(name="Axe",attack=11,deffence=11)]
    max_name=max(len(char['name']) for char in weapons)
    for i,char in enumerate(weapons,start=1):
        SPrint(f"{i}. Name: {char['name']:<{max_name}} | Attack: {char['attack']} | Deffence: {0 if char['deffence']<10 else ''}{char['deffence']}",speed=0.03)
    weapon=weapons[int(SInput("\nIndex of the Weapon you want: "))-1]
    clear()
    return idol,weapon
def Intro(name):
    sleep(2)
    SPrint(pause_at=[',','.','\n'],chars="Welcome to the kingdom of Eldoria\n\nThe enchanting land of Eldoria, whare mythical creatures roam freely. Once a prosperous kingdom under King Alaric, Eldoria now faces darkness.\n\nThe king chose you to uncover ancient secrets and restore the kingdom's peace.",speed=0.06)
    SInput("\n\nPress any key to continue . . .",speed=0.03)
    clear()
    SPrint(f"King Alaric: {name}, we face grave threats. I'm chosing you to face the challenges ahead.\n\n{name}: Yes, Your Majesty. How should I proceed?\n\nKing Alaric: Throughout you journey you'll face many enemies, make sure to assess their weaknesses as you encounter them.\n\n{name}: I’ll be ready for whatever comes!\n\nKing Alaric: Good. I shall provide you with the Dark Amulet, it will help you to teleport to escape any enemy, but remember to use it wisely, as you can only use it 3 times after it's magic will be over. To restore the magic you must merge the Amulet with a Dark Crystal you can only find in Crystal Cave.\n\n{name}: Thank you, Your Majesty. I will not fail you.\n",pause_at=[':','\n','.','!'],speed=0.027)
    SInput("\nPress any key to continue . . .",speed=0.03)
    clear()
def RPG(player):
    while player.alive():
        usr=input("What you would like to do ::\n1. Explore\n2. Travel\n3. Go to Armoury\n4. Got to Weaponary\n5. Go to Shop\n\n-->")
        clear()
        if usr=='0':
            in_fight(player)
    return player.score
def endgame(name,score):
    print("Game Over !")
    with open("HighScore.txt",'w+') as hi:
        hs=int(hi.read())
        if hs<score:
            print(f"New High Score: {score} !!! ")
            hi.write(str(score))
        else:
            print(f"Score: {score}\nHigh Score: {hs}")
    input()
def PLAY():
    ascii_art()
    Data=DATA(input("Identity name : "))
    input(Data.data)
    clear()
    cont=False
    while True:
        user=Screen()
        print(user==0)
        if user==0:
            if Data.data!={}:
                restart=(input("Do you Want to restart your progress? (Y/n)\n-->").lower() == 'y')
                cont=bool(restart)
                if cont:
                    Data.clear()
                    continue
            start=Start()
            idol=start[0]
            Intro(idol['name'])
            score=RPG(Player(idol['name'],idol['hp'],idol['deffence'],idol['attack'],idol['classed'],idol['luck'],start[1]))
            endgame(Data.name,score)
##        if 
PLAY()
