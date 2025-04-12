class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    import math
    total_attack_to_win_for_1 = math.ceil(fighter1.health / fighter2.damage_per_attack)
    total_attack_to_win_for_2 = math.ceil(fighter2.health / fighter1.damage_per_attack)
    if first_attacker == fighter1.name:
        if total_attack_to_win_for_1 >= total_attack_to_win_for_2:
            return fighter1.name
        else:
            return fighter2.name
    elif first_attacker == fighter2.name:
        if total_attack_to_win_for_2 >= total_attack_to_win_for_1:
            return fighter2.name
        else:
            return fighter1.name

print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"))

# refactored code

def declare_winner(fighter1, fighter2, first_attacker):
    hits_to_defeat_1 = math.ceil(fighter1.health / fighter2.damage_per_attack)
    hits_to_defeat_2 = math.ceil(fighter2.health / fighter1.damage_per_attack)

    if hits_to_defeat_1 == hits_to_defeat_2:
        return first_attacker
    return fighter1.name if hits_to_defeat_1 > hits_to_defeat_2 else fighter2.name