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