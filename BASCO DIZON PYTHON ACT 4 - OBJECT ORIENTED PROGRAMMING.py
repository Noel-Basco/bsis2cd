#Object Oriented Programming Activity 4
#Character Customization

#Members:
#BASCO, NOEL FRANCIS MARIE F.
#DIZON, THEA JAZMINE G.


from asyncio.windows_events import NULL


class customize:
    def __init__ (self, character: str, weapon: str, ability1: str, ability2: str):
        self.character = character
        self.weapon = weapon
        self.ability1 = ability1
        self.ability2 = ability2

    def setClass(self):
        
        choice = int(input("\nChoose a class:\n1. Wizard\n2. Knight\n3. Archer\n4. Assassin\n\n"))

        if choice == 1:
            self.character = "Wizard"

        elif choice == 2:
            self.character = "Knight"
            
        elif choice == 3:
            self.character = "Archer"

        elif choice == 4:
            self.character = "Assassin"

    def setWeapon(self):
        
        choice = int(input("\nChoose a Weapon:\n1. Wizard Staff\n2. Sword\n3. Bow & Arrow\n4. Katar\n\n"))

        if choice == 1:
            self.weapon = "Wizard Staff"

        elif choice == 2:
            self.weapon = "Sword"
            
        elif choice == 3:
            self.weapon = "Bow & Arrow"

        elif choice == 4:
            self.weapon = "Katar"

    def setAbility(self,choice):

        Ability_List = ["Energy Ball","Dragon's Breath","Crown of Flame","Hail Storm",]
        Ability_List2 = ["Fire Slash","Power Slash","Gigantic Storm","Chaotic Disaster"]
        Ability_List3 = ["Take Aim","Quick Shot","Blazing Arrow","Frost Arrow"]
        Ability_List4 = ["Cloaking","Enchant Poison","Sonic Acceleration","Meteor Assault"]

        if self.character == "Wizard":
            checker = False
            while checker == False:
                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List[0],Ability_List[1],Ability_List[2],Ability_List[3]))
                choice = int(input("Choose your first ability: "))

                if choice == 1:
                    self.ability1 = Ability_List[0]     
                elif choice == 2:
                    self.ability1 = Ability_List[1]     
                elif choice == 3:
                    self.ability1 = Ability_List[2]     
                elif choice == 4:
                    self.ability1 = Ability_List[3]     
                else: 
                    print("not in list! Try again.") 
                    continue

                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List[0],Ability_List[1],Ability_List[2],Ability_List[3]))
                choice = int(input("Choose your second ability: "))

                if choice == 1:
                    self.ability2 = Ability_List[0]
                elif choice == 2:
                    self.ability2 = Ability_List[1]
                elif choice == 3:
                    self.ability2 = Ability_List[2]
                elif choice == 4:
                    self.ability2 = Ability_List[3]
                else: 
                    print("not in list! Try again.") 
                    continue
                checker = True
        
        if self.character == "Knight":
            checker = False
            while checker == False:
                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List2[0],Ability_List2[1],Ability_List2[2],Ability_List2[3]))
                choice = int(input("Choose your first ability: "))

                if choice == 1:
                    self.ability1 = Ability_List2[0]
                elif choice == 2:
                    self.ability1 = Ability_List2[1]
                elif choice == 3:
                    self.ability1 = Ability_List2[2]
                elif choice == 4:
                    self.ability1 = Ability_List2[3]
                else: 
                    print("not in list! Try again.") 
                    continue
                
                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List2[0],Ability_List2[1],Ability_List2[2],Ability_List2[3]))
                choice = int(input("Choose your second ability: "))

                if choice == 1:
                    self.ability2 = Ability_List2[0]
                elif choice == 2:
                    self.ability2 = Ability_List2[1]
                elif choice == 3:
                    self.ability2 = Ability_List2[2]
                elif choice == 4:
                    self.ability2 = Ability_List2[3]
                else: 
                    print("not in list! Try again.") 
                    continue
                checker = True

        if self.character == "Archer":
            checker = False
            while checker == False:
                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List3[0],Ability_List3[1],Ability_List3[2],Ability_List3[3]))
                choice = int(input("Choose your first ability: "))

                if choice == 1:
                    self.ability1 = Ability_List3[0]
                elif choice == 2:
                    self.ability1 = Ability_List3[1]
                elif choice == 3:
                    self.ability1 = Ability_List3[2]
                elif choice == 4:
                    self.ability1 = Ability_List3[3]
                else: 
                    print("not in list! Try again.") 
                    continue

                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List3[0],Ability_List3[1],Ability_List3[2],Ability_List3[3]))
                choice = int(input("Choose your second ability: "))

                if choice == 1:
                    self.ability2 = Ability_List3[0]
                elif choice == 2:
                    self.ability2 = Ability_List3[1]
                elif choice == 3:
                    self.ability2 = Ability_List3[2]
                elif choice == 4:
                    self.ability2 
                else: 
                    print("not in list! Try again.") 
                    continue
                checker = True
            

        if self.character == "Assassin":
            checker = False
            while checker == False:
                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List4[0],Ability_List4[1],Ability_List4[2],Ability_List4[3]))
                choice = int(input("Choose your first ability: "))

                if choice == 1:
                    self.ability1 = Ability_List4[0]
                elif choice == 2:
                    self.ability1 = Ability_List4[1]
                elif choice == 3:
                    self.ability1 = Ability_List4[2]
                elif choice == 4:
                    self.ability1 = Ability_List4[3]
                else: 
                    print("not in list! Try again.") 
                    continue

                print("\nAbilities list:\n1. %s\n2. %s\n3. %s\n4. %s\n"%(Ability_List4[0],Ability_List4[1],Ability_List4[2],Ability_List4[3]))
                choice = int(input("Choose your second ability: "))

                if choice == 1:
                    self.ability2 = Ability_List4[0]
                elif choice == 2:
                    self.ability2 = Ability_List4[1]
                elif choice == 3:
                    self.ability2 = Ability_List4[2]
                elif choice == 4:
                    self.ability2 = Ability_List4[3]
                else: 
                    print("not in list! Try again.") 
                    continue
                checker = True

char1 = customize("Null","Null","Null","Null")
char2 = customize("Null","Null","Null","Null")
choice = 5

print("Character 1:")

char1.setClass()
char1.setWeapon()
char1.setAbility(choice)

print("Character 2:")

char2.setClass()
char2.setWeapon()
char2.setAbility(choice)

print("\n---Character List:---\n")
print("\nCharacter 1:\n")
print("Class: ", char1.character)
print("Weapon: ", char1.weapon)
print("Abilities: ",char1.ability1,"and",char1.ability2,"\n")

print("\nCharacter 2:\n")
print("Class: ", char2.character)
print("Weapon: ", char2.weapon)
print("Abilities: ",char2.ability1,"and",char2.ability2, "\n")
print("---End of List---")