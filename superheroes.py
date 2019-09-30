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
        self.starting_health = starting_health
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
        return self.current_health > 0

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

        def add_weapon(self, weapon):
            self.abilities.append(weapon)
        pass

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
            if hero.name == name:
                self.heroes.remove(hero)
        return 0


    def is_team_alive(self):
        for hero in self.heroes:
            if hero.is_alive():
                return True
        else:
            return False


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def get_r_fighter(self):
        if self.is_team_alive() == False:
            return 0
        else:
            fighter = random.choice(self.heroes)
            if fighter.is_alive() == False:
                fighter = self.get_r_fighter()
            return fighter


    def attack(self, other_team):

        state = "alive"

        while state == "alive":
            self_fighter = self.get_r_fighter()
            other_team_fighter = other_team.get_r_fighter()
            self_fighter.fight(other_team_fighter)
            if self.is_team_alive() or self_fighter == "alive":
                state = "fighter team died"
            elif other_team.is_team_alive() or other_team_fighter == "alive":
                state = "opponent team dead"

    def revive_heroes(self, health=100):

        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = 100

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(f"{hero.name}; Kills - {hero.kills}, Deaths - {hero.deaths}")

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        ability_input = input("Enter ability name: ")
        max_strength_input = input("Enter maximum strength for ability: ")
        return Ability(ability_input, max_strength_input)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        weapon_input = input("Enter weapon name: ")
        weapon_attack = int(input("Enter weapon max attack (Ints only): "))
        return Weapon(weapon_input, weapon_attack)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        armor_input = input("Enter armor name: ")
        armor_max_block_input = input("Enter armor max block: ")
        return Armor(armor_input, armor_max_block_input)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        hero_name_input = input("Input hero name: ")
        hero_armor_option_input = input("Do you want armor? (Y/N): ")
        if hero_armor_option_input == "Y":
            create_armor()
        else:
            pass

        hero_weapon_option_input = input("Do you want a weapon? (Y/N): ")
        if hero_weapon_option_input == "Y":
            create_weapon()
        else:
            pass

        hero_weapon_option_ability = input("Do you want an ability? (Y/N): ")
        if hero_weapon_option_input == "Y":
            create_ability()
        else:
            pass

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        team_name = input("Enter first team name: ")
        self.team_one = Team(team_name)

        hero_amount_input = int(input("How many heroes?: "))
        for hero_index in hero_amount_input:
            hero = self.create_hero()
            team_one.add_hero(hero)
        self.team_one = team_one


    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        team_name = input("Enter second team name: ")
        self.team_two = Team(team_name)

        hero_amount_input = int(input("How many heroes?: "))
        for hero_index in hero_amount_input:
            hero = self.create_hero()
            team_two.add_hero(hero)
        self.team_two = team_two

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
