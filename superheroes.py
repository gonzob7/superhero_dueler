from random import randint, choice

class Ability:
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return randint(0, self.max_damage)


# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def defend(self, damage_amt=0):
        total_block = 0
        for armor in self.armors:
            armor.block()
            new_block = armor.block()
            total_block += new_block
        return total_block

    def take_damage(self, damage):
        current_health = self.current_health
        damage_defense = self.defend(damage)

    def is_alive(self):
        return self.current_health <= 0

    def fight(self, opponent):
        if self.is_alive() == True and opponent.is_alive() == True:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                #print(self.current_health)
                #print(opponent.current_health)
                if self.is_alive() == False and opponent.is_alive() == True:
                    print('{} Wins!'.format(opponent.name))
                    opponent.add_kill(1)
                    self.add_death(1)
                elif self.is_alive() == True and opponent.is_alive() == False:
                    print('{} Wins!'.format(self.name))
                    self.add_kill(1)
                    opponent.add_death(1)
                elif self.is_alive() == False and opponent.is_alive() == False:
                    print("They both died...")
                    self.add_kill(1)
                    opponent.add_death(1)
                    opponent.add_kill(1)
                    self.add_death(1)

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        return randint((self.max_damage // 2), self.max_damage)


class Team:
    def __init__(self, name):
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        index = 0
        length = len(self.heroes)
        for hero in self.heroes:
            if hero.name == name:
                del self.heroes[index]
            else:
                index += 1
        if len(self.heroes) == length:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def team_members_alive(self):
        heroes_alive = []
        for hero in self.heroes:
            if hero.is_alive() == True:
                heroes_alive.append(hero)
        return heroes_alive

    def number_of_team_members_alive(self):
        number_heroes_alive = 0
        for hero in self.heroes:
            if hero.is_alive() == True:
                number_heroes_alive += 1
        return number_heroes_alive

    def attack(self, other_team):
        while self.number_of_team_members_alive() > 0 and other_team.number_of_team_members_alive() > 0:
            hero1 = choice(self.team_members_alive())
            hero2 = choice(other_team.team_members_alive())
            hero1.fight(hero2)

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = 100

    def stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.hero_list:
            team_kills += hero.kills
            team_deaths += hero.deaths

            kd = round(hero.kills / hero.deaths,
                       2) if hero.deaths > 0 else hero.kills
            print(f'{hero.name} has {hero.kills} kills and {hero.deaths} deaths')
            print(f'{hero.name} has a KD of: {kd}')

        return round(team_kills / team_deaths, 2) if team_deaths > 0 else team_kills

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

    def create_ability(self, name):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        ability_name = input("Input ability name ").lower()
        ability_damage = int(input("Input ability damage "))
        return Ability(ability_name, ability_damage)

    def create_weapon(self, name):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        weapon_name = input("Input weapon name ").lower()
        weapon_damage = int(input("Input weapon damage "))
        return Ability(weapon_name, weapon_damage)

    def create_armor(self, name):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        armor_name = input("Input armor name ").lower()
        armor_points = int(input("Input armor value "))
        return Armor(armor_name, armor_points)

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
        hero_name_input = input("Enter hero name: ")
        hero_health_input = int(input("Enter hero health: "))
        u_hero = Hero(hero_name_input, int(hero_health_input))

        hero_armor_option_input = input("Do you want armor? (Y/N): ").upper()
        if hero_armor_option_input == "Y":
            u_hero.add_armor(self.create_armor)
        else:
            pass

        hero_weapon_option_input = input("Do you want a weapon? (Y/N): ")
        if hero_weapon_option_input == "Y":
            u_hero.add_weapon(self.create_weapon)

        else:
            pass

        hero_weapon_option_ability = input("Do you want an ability? (Y/N): ")
        if hero_weapon_option_input == "Y":
            u_hero.add_ability(self.create_ability)
        else:
            pass

        return u_hero

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
        for index in range(hero_amount_input):
            self.team_one.add_hero(self.create_hero())



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
        for index in range(hero_amount_input):
            self.team_two.add_hero(self.create_hero())



    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)


    def show_stats(self):
        print('=' * 24)
        print('TEAM ONE STATISTICS: \n')
        print(f'\nTeam one\'s stats: {self.team_one.stats()}\n')

        print('=' * 24)

        print('TEAM TWO STATISTICS: \n')
        print(f'\nTeam two\'s stats: {self.team_two.stats()}\n')
        print('=' * 24)

        print('FIGHT OUTCOME: \n')
        if self.team_one.team_alive():
            hero_list = [hero.name for hero in self.team_one.hero_list]
            print(
                f'Team 1 is victorious!\nChampions: {", ".join(hero_list)}')
        else:
            hero_list = [hero.name for hero in self.team_two.hero_list]
            print(
                f'Team 2 is victorious!\nChampions: {", ".join(hero_list)}')
        print('=' * 24)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
