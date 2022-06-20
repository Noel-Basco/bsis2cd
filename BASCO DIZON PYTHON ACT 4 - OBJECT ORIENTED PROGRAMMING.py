#Object Oriented Programming Activity 4
#Character Customization

#Members:
#BASCO, NOEL FRANCIS MARIE F.
#DIZON, THEA JAZMINE G.


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

char1 = customize("Null","Null","Null","Null")
char2 = customize("Null","Null","Null","Null")

char1.setClass()
char1.setWeapon()
# char1.setAbility()

char2.setClass()
char2.setWeapon()
# char2.setAbility()

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
