class Character:
    def __init__(self,name,hp,atk,deff):
                 self.name = name
                 self.hp = hp
                 self.deff = deff 
                 self.atk = atk
    def Warrior(self):
        print("The Warrior Job \n")
        n = self.name 
        n = input("State your name Soldier : ")
        print("Hello " + n + " As a Warrior you should protect us \n","Here's your Status Warrior")
        self.atk = 100
        self.hp = 100
        self.deff = 50
        print("Your Health Point : ", self.hp, "\nYour Attack Point : ", self.atk, "\nYour Defence : ", self.deff)

    def Zombie(self):
        print("This is Zombie that eat  Brains ")
        self.name = "Zombie"
        self.atk = 100
        self.deff = 20
        self.hp = 125
        print("Name : ", self.name,"\n HP : ",self.hp,"\n Attack : ", self.atk, "\n Defence : ", self.deff)
    
    def battle(self):
        print("You met a zombie for the first TIME!!!")
        print("do you wanna Run/Fight? ")
        c = input("1.Run\n2.Fight \n ")
        while c not in ['1','2']:
            c = input("1.Run\n2.Fight \n ")
        if c == '1':
            print("You Run away and get hit buy Truck")
        elif c == '2':
            print("You pick a fight with Zombie ")
            

p = Character("",0,0,0)
p.Warrior()
p.Zombie()
p.battle()