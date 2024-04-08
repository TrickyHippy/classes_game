import random
        

class Monster:

    hero = input("Enter your name.")
    hero_hp = 50
    hero_power = 10
    hero_defense = 5

    def __init__(self, name, hp, power, defense) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense

    def __str__(self) -> str:
        return f'A {self.name}. It has {self.hp} HP, {self.power} power and {self.defense} armor.'
    
    def monster_name(self):
        return self.name
    
    def heal(self):
        Monster.hero_hp += 12
        return Monster.hero_hp
    
    def show_stats(self):
        return f"""{self.hero} stats are:
Hitpoints = {self.hero_hp}
Power = {self.hero_power}
Armor = {self.hero_defense}
"""
    
    def level_up(self):
        Monster.hero_power += 2
        Monster.hero_defense += 1
        self.power += 3
        self.defense += 3

    def battle(self):
        if Monster.hero_defense <= self.power:
            Monster.hero_hp -= self.power + Monster.hero_defense
            if Monster.hero_hp <= 0:
                return self.name, self.hp, True
        if self.defense <= Monster.hero_power:
            self.hp -= Monster.hero_power + self.defense
        print(f"{self.hero} HP = {Monster.hero_hp}\n{self.name} HP = {self.hp}")
        Monster.level_up(self)
        return self.name, self.hp, False


def generate_monster(name):
    names_numbers = {
        "Fairy": 1,
        "Goblin": 2,
        "Wolf": 3,
        "Lizzard": 5,
        "Snapper": 7,
        "Bandit": 9,
        "Skeleton": 12,
        "Skeleton Mage": 15,
        "Ork": 18,
        "Ork Elite": 22,
        "Demon": 26,
        "Demon Lord": 30
    }

    monster_modifyers = {
        "Tiny ": 0.5,
        "Small ": 0.75,
        "Normal ": 1,
        "Big ": 1.5,
        "Gigantic ": 2
    }

    monster_modifyers_list = list(monster_modifyers.keys())
    monster_modifyer = random.choice(monster_modifyers_list)
    name_number = names_numbers[name]
    hp = name_number * 5 + random.randint(1, 20)
    power = name_number * monster_modifyers[monster_modifyer]
    defense = name_number * 0.4 * monster_modifyers[monster_modifyer]
    name = monster_modifyer + name

    monster = Monster(name, hp, power, defense)
    return monster


monsters = ["Fairy", "Goblin", "Wolf", "Lizzard", "Snapper", "Bandit", "Skeleton", "Skeleton Mage", "Ork", "Ork Elite", "Demon", "Demon Lord"]
battle_monster = ""
hero_alive = True
monster_list_in_battle = []


while True:

    if len(monster_list_in_battle) > 5:
        battle_monsters = random.sample(list(monster_list_in_battle), 3)
    else:
        battle_monsters = random.sample(monsters, 3)
    try:
        monster_index = eval(input(
f"""
If you want to go straight ahead, towards {battle_monsters[0]} press 0
If you want to go left, towards {battle_monsters[1]} press 1
Or, if you want to go right, towards {battle_monsters[2]} press 2
"""))
    except:
        monster_index = random.randint(0,2)
    if battle_monsters[monster_index] in monster_list_in_battle:
        battle_monster = battle_monsters[monster_index]
    else:
        battle_monster = generate_monster(battle_monsters[monster_index])
        print(battle_monster)
        monster_list_in_battle.append(battle_monster)

    battle_monster_name, battle_monster_hp, hero_died = battle_monster.battle()
    battle_monster_name = str(battle_monster_name)
    if hero_died:
        break
    elif battle_monster_name.count("Demon Lord") == 1 and battle_monster_hp <= 0:
        break
    if battle_monster_hp <= 0:
        monster_list_in_battle.remove(battle_monster)
        
    print("You take a rest.")
    hero_hp = battle_monster.heal()
    stats = battle_monster.show_stats()
    print(stats)


if not hero_died:
    print(f"You killed {battle_monster}\nYou won the game!!")
else:
    print(f"You got killed by {battle_monster}\nYou lost the game!")