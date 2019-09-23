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

    def defend(self, dmg_amt):
        sum = 0
        for armor in armors:
            block()
            sum += 1

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
