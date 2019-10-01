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
        return randint(0, int(self.max_damage))

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage = total_damage + ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_ability(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def defend(self):
        damage_amt = 0
        for armor in self.armors:
            damage_amt = damage_amt + armor.block()
        return damage_amt

    def take_damage(self, damage):
        attack = self.defend()
        attack_val = 0
        if damage - attack > 0:
            attack_val = damage - attack
        else:
            attack_val = 0
        self.current_health = int(self.current_health) - int(attack_val)

    def is_alive(self):
        if int(self.current_health) <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.is_alive() and not opponent.is_alive():
            self.add_kill(1)
            opponent.add_deaths(1)
            print(self.name, 'won!')
        elif opponent.is_alive() and not self.is_alive():
            opponent.add_kill(1)
            self.add_deaths(1)
            print(opponent.name, 'won!')
        else:
            print('Draw!')

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint((self.max_damage // 2), self.max_damage)


class Team:
    def __init__(self, name):
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
        kdr = 0
        total_kills = 0
        total_deaths = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        if total_deaths == 0:
            kdr = total_kills
        else:
            kdr = total_kills/total_deaths
        return kdr

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self, name, damage):
        return Ability(name, damage)

    def create_weapon(self, name, damage):
        return Ability(name, damage)

    def create_armor(self, name, points):
        return Armor(name, points)

    def create_hero(self):
        hero_name_input = input("Enter hero name: ")
        hero_health_input = int(input("Enter hero health: "))
        current_hero = Hero(hero_name_input, int(hero_health_input))

        if input("Do you want armor? (Y/N): ").upper() == "Y":
            armor_name = input("Enter armor name: ").lower()
            armor_points = int(input("Enter armor max block: "))
            current_hero.add_armor(self.create_armor(armor_name, armor_points))

        hero_weapon_option_input = input("Do you want a weapon? (Y/N): ").upper()
        if hero_weapon_option_input == "Y":
            weapon_name = input("Enter weapon name: ").lower()
            weapon_damage = int(input("Enter weapon max damage: "))
            current_hero.add_weapon(self.create_weapon(weapon_name, weapon_damage))

        hero_ability_option_input = input("Do you want an ability? (Y/N): ").upper()
        if hero_ability_option_input == "Y":
            ability_name = input("Enter ability name: ").lower()
            ability_damage = int(input("Enter ability max damage: "))
            current_hero.add_ability(self.create_ability(ability_name, ability_damage))

        return current_hero

    def build_team_one(self):
        team_name = input("\nEnter first team name: ")
        self.team_one = Team(team_name)

        hero_amount_input = int(input("How many heroes?: "))
        for index in range(hero_amount_input):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        team_name = input("\nEnter second team name: ")
        self.team_two = Team(team_name)

        hero_amount_input = int(input("How many heroes?: "))
        for index in range(hero_amount_input):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        stat_header = """
        ===========
        || STATS ||
        ===========
        """
        print(stat_header)
        print(f'Team One KDR: {self.team_one.stats()}')
        print(f'Team Two KDR: {self.team_two.stats()} \n')

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
