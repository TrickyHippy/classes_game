import random
import time

trophys = []
counter = 0
god_mode = False
        
def print_slowly(text, delay=0.04):
    for char in str(text):
        print(char, end='', flush=True)
        time.sleep(delay)


def input_slowly(prompt):
    print_slowly(prompt)
    user_input = input()
    return user_input


class Monster:

    hero = input_slowly("Enter your name: ")
    hero_hp = 50
    generall_stat_increment = 0
    hero_power = 10
    hero_defense = 5

    def __init__(self, name, hp, power, defense, weapon = 0, bonus_heal = 0) -> None:
        self.name = name
        if self.name == "Gigantic Angel" or self.name == "Gigantic Demonlord" or self.name == "Gigantic Dragon":
            self.generall_stat_increment *= 2
        self.hp = hp + Monster.generall_stat_increment * 3
        self.power = power + Monster.generall_stat_increment * 2
        self.defense = defense + Monster.generall_stat_increment
        self.weapon = weapon
        self.bonus_heal = bonus_heal
        if "Rusty-Sword" in trophys:
            self.weapon = 3
        elif "Big-Wooden-Club" in trophys:
            self.weapon = 1
        if "Golden-Essence" in trophys and "Silver-Essence" in trophys:
            self.bonus_heal = 5
            if "Gold-Coin" in trophys and "Silver-Coin" in trophys:
                self.bonus_heal += 5
            elif "Gold-Coin" in trophys:
                self.bonus_heal += 3
            elif "Silver-Coin" in trophys:
                self.bonus_heal += 2
        elif "Golden-Essence" in trophys:
            self.bonus_heal = 3
            if "Gold-Coin" in trophys:
                self.bonus_heal += 3
        elif "Silver-Essence" in trophys:
            self.bonus_heal = 2
            if "Silver-Coin" in trophys:
                self.bonus_heal += 3


    def __str__(self) -> str:
        return f'{self.name}'
    
    def monster_name(self):
        return self.name
    
    def heal(self):
        Monster.hero_hp += 12 + self.bonus_heal
        return Monster.hero_hp
    
    def show_stats(self):
        return f"""{self.hero} stats are:
Hitpoints = {self.hero_hp}
Power = {self.hero_power}
Armor = {self.hero_defense}
"""
    
    def level_up(self):
        Monster.hero_power += 4 + self.weapon
        Monster.hero_defense += 2
        self.power += 5 
        self.defense += 1
        Monster.generall_stat_increment += 1

    def battle(self):
        if "Bandits-Bow" in trophys or "Frost-Rune" in trophys or "Fire-Rune" in trophys:
            god_damage = 0
            bow_list = [1, 2, 3, 59]
            if god_mode:
                god_damage = 55
                bow_list = [59, 59, 59, 250]
                
            target = random.choice(bow_list)
            if "Frost-Rune" in trophys:
                if "Fire-Rune" in trophys:
                    self.hp -= 20 + god_damage
                self.hp -= 5 + random.randint(1, 12)
                print_slowly("Freezee shooto!\n")
            elif "Fire-Rune" in trophys:
                self.hp -= 25 + god_damage
                print_slowly("Firreee Shooto!\n")
            elif "Bandits-Bow" in trophys:
                self.hp -= 1 + target
                print_slowly("Phiuww!\n")
                if target == 250:
                    print_slowly("Hearthpiercer shooto!\n")
                elif target == 59:
                    print_slowly("Headshot!\n")
            if "Frost-Rune" in trophys and "Bandits-Bow" in trophys:
                self.hp -= 1 + target
                print_slowly("Phiuww!\n")
                if target == 59:
                    print_slowly("Headshot!")

        if self.hp >= 0:
            time.sleep(1)
            print_slowly("Huagh!\n")
            time.sleep(1)
            print_slowly("Waarrrgh!\n")
            time.sleep(1)

        if self.power > Monster.hero_defense and self.hp > 0:
            Monster.hero_hp -= int(self.power - Monster.hero_defense)
            if Monster.hero_hp <= 0:
                return self.name, self.hp, True
        if Monster.hero_power > self.defense:
            self.hp -= int(Monster.hero_power - self.defense)
        Monster.level_up(self)

        if self.hp <= 0 and Monster.hero_hp > 0:
            print_slowly("Hurrraaay!\n")
        elif Monster.hero_hp <= 0:
            print_slowly("Aarrgghh!")
        else:
            print_slowly("Ruunn awaaay!\n")
        print_slowly(f"{self.show_stats()}")

        return self.name, self.hp, False


def generate_monster(name):
    names_numbers = {
        "Sprite": 1,
        "Fairy": 2,
        "Goblin": 4,
        "Wolf": 6,
        "Lizzard": 8,
        "Snapper": 10,
        "Bandit": 12,
        "Skeleton": 15,
        "Skeleton Mage": 18,
        "Ork": 21,
        "Ork Elite": 24,
        "Demon": 27,
        "Demon Lord": 30,
        "Dragon": 35,
        "Angel": 40
    }

    monster_modifyers = {
        "Tiny ": 0.5,
        "Small ": 0.75,
        "Normal ": 1,
        "Big ": 1.5,
        "Gigantic ": 2
    }
    if god_mode:
        monster_modifyers = {
            "Gigantic ": 2
        }

    monster_modifyers_list = list(monster_modifyers.keys())
    monster_modifyer = random.choice(monster_modifyers_list)
    name_number = names_numbers[name]
    hp = name_number * 5 + random.randint(1, 20)
    power = round(name_number * monster_modifyers[monster_modifyer], 0) + 5
    defense = round(name_number * 0.4 * monster_modifyers[monster_modifyer], 0)
    name = monster_modifyer + name

    monster = Monster(name, hp, power, defense)
    return monster

basic_monsters = ["Sprite", "Fairy", "Goblin", "Wolf", "Lizzard", "Snapper", "Bandit", "Skeleton", "Skeleton Mage", "Ork", "Ork Elite", "Demon", "Demon Lord", "Dragon", "Angel"]
monsters = ["Sprite", "Fairy", "Goblin", "Wolf", "Lizzard", "Snapper", "Bandit", "Skeleton", "Skeleton Mage", "Ork", "Ork Elite", "Demon", "Demon Lord", "Dragon", "Angel"]
monster_trophys = {
    "Sprite": "Golden-Essence",
    "Fairy": "Silver-Essence",
    "Goblin": "Big-Wooden-Club",
    "Wolf": "Wolf-Teeth",
    "Lizzard": "Lizzard-Skin",
    "Snapper": "Snapper-Claw",
    "Bandit": "Bandits-Bow",
    "Skeleton": "Rusty-Sword",
    "Skeleton Mage": "Frost-Rune",
    "Ork": "Silver-Coin",
    "Ork Elite": "Gold-Coin",
    "Demon": "Fire-Rune",
    "Demon Lord": "Excalibur",
    "Dragon": "Dragon-Teeth",
    "Angel": "Angel-Wings"
}
ability_trophys = ["Golden-Essence", "Silver-Essence", "Big-Wooden-Club", "Bandits-Bow", "Rusty-Sword", "Frost-Rune", "Fire-Rune", "Excalibur"]

battle_monster = ""
basic_monster = ""
hero_died = False

print_slowly("""Weak Monsters are:
Sprite, Fairy, Goblin.

Normal Monsters are: 
Wolf, Lizzard, Snapper.

Challanging Monsters are:
Bandit, Skeleton, Skeleton Mage.

Strong Monsters are:
Ork, Ork Elite, Demon.

Epic Monsters are:
Demon Lord, Dragon, Angel.

In order to win, you need to kill an epic monster.
""")


while True:
    battle_monsters = random.sample(monsters, 3)
    try:
        monster_index = eval(input_slowly(
f"""If you want to go straight ahead, towards {battle_monsters[0]} press 0
If you want to go left, towards {battle_monsters[1]} press 1
Or, if you want to go right, towards {battle_monsters[2]} press 2
"""))
    except:
        monster_index = random.randint(0,2)
    if battle_monsters[monster_index] not in basic_monsters:
        battle_monster = battle_monsters[monster_index]
    else:
        battle_monster = generate_monster(battle_monsters[monster_index])
        print_slowly(str(battle_monster) + "\n")
        if battle_monster.hp >= 0:
            monsters.append(battle_monster)
    battle_monster_name = str(battle_monster.name)
    while battle_monster.hp >= 0:
        counter += 1
        battle_monster_name, battle_monster_hp, hero_died = battle_monster.battle()

        if hero_died:
            break
        print_slowly("You take a rest.\n")
        hero_hp = battle_monster.heal()
        print_slowly(str(Monster.hero) + " HP = " + str(Monster.hero_hp) + "\n")

    monsters.remove(battle_monster)
    slice_str = str(battle_monster)
    basic_monster = slice_str[slice_str.find(" ")+1:]
    monsters.remove(basic_monster)
    if battle_monster_hp <= 0:
        trophys.append(monster_trophys[basic_monster])
        print_slowly(f"You gather {monster_trophys[basic_monster]}.\n")
        if monster_trophys[basic_monster] in ability_trophys:
            print_slowly("You gained a special ability.\n")
        if Monster.hero_power >= 150 and not god_mode:
            god_mode = True
            Monster.hero_hp += 100
            print_slowly("You enter Godmode..", 0.16)
            print_slowly("You gain 100 bonus HP and godlike accuracy.\n", 0.08)
            time.sleep(1)
            print_slowly("You look out for the strongest prey..\n", 0.08)

    if hero_died:
        break
    if ((battle_monster_name.count("Demon Lord") == 1 or battle_monster_name.count("Angel") == 1 or battle_monster_name.count("Dragon") == 1) and battle_monster_hp <= 0):
        break


if not hero_died:
    print_slowly(f"{Monster.hero} killed {battle_monster}\nYou won the game!!\n")
    if god_mode:
        print_slowly("You are a godlike hunter.\n")
    if counter <= 16:
        print_slowly(f"You are an absolute Legend.\nYou won in just {counter} turns.\n")
    else:
        print_slowly(f"You won in {counter} turns.\n")
else:
    print_slowly(f"You got killed by {battle_monster}\nYou lost the game!\n")
if trophys:
    print_slowly(f"Your inventory contains: \n{', \n'.join(trophys)}\n")


print_slowly("""\nSpeedrun-Info:
Max-Speed win is 8 turns.
Very Fast win is 12 Turns.
Quick win is 16 Turns or faster.
Normal Speedrun Win is 20 Turns or faster.
""")