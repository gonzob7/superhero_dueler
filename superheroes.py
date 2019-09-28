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
        max_damage = random.randint(0, self.max_damage)
        return max_damage


# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total = total + ability.attack()
            # ability.attack()
        return total

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def defend(self):
        total_defense = 0
        if not len(self.armors) == 0:
            for armor in self.armors:
                total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        health_change = self.defend() - damage
        self.current_health += health_change

    def is_alive(self):
        return self.current_health >= 0

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            if self.is_alive() and not opponent.is_alive():
                print(f'{self.name} won!')
                self.add_kill(1)
                opponent.add_deaths(1)
            elif not self.is_alive() and opponent.is_alive():
                print(f'{opponent.name} won!')
                opponent.add_kill(1)
                self.add_deaths(1)

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        max_damage = random.randint(self.max_damage//2, self.max_damage)
        return max_damage

class Team:
    def __init__(self, name):
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)


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
