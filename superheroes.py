import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return(random.randint(0, self.max_damage))

# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return(random.randint(0, self.max_block))

class Hero:
    def __init__(self, name, current_health, starting_health=100):


        self.abilities = []
        self.armors = []
        self.current_health = current_health
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.max_damage
            # ability.attack()
        return total

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, dmg_amt = 0):
        for armor in self.armors:
            dmg_amt += armor.block()
        return dmg_amt

    def take_damage(self, damage):
        dmg = damage
        self.current_health = self.current_health - dmg

    def is_alive(self):
        if(self.current_health > 0):
            return True
        elif(self.current_health <= 0):
            return False

    def fight(self, opponent):
        if(self.abilities or opponent.abilities):
            while(self.is_alive() and opponent.is_alive()):
                self.take_damage(opponent.attack)
                opponent.take_damage(self.attack)
            if(self.is_alive() == True and opponent.is_alive() == False):
                print(f'{self.name} wins!')
            elif(self.is_alive() == False and opponent.is_alive() == True):
                print(f'{opponent.name} wins!')
            else:
                print("Draw!")


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman",1000)
    hero2 = Hero("Dumbledore",100)
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
