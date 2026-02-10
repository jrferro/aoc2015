# https://adventofcode.com/2015/day/21

BOSS_HP = 109
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

PLAYER_HP = 100

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
# 
# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
# 
# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

WEAPON_ATK_COST = [999, 999, 999, 999, 8, 10, 25, 40, 74]
RING_ATK_COST = [0, 25, 50, 75, 125, 150]
ARMOR_DEF_COST = [0, 13, 31, 53, 75, 102]
RING_DEF_COST = [0, 20, 40, 60, 100, 120]

def ttk(dmg, arm, hp):
    dpt = max(dmg-arm, 1)
    if hp % dpt == 0:
        return hp // dpt
    else:
        return (hp // dpt) + 1

def cost_of_atk(a, rank):
    costs = []
    for i, v in enumerate(RING_ATK_COST):
        if a-i >= 4 and a-i <= 8:
            costs.append(v + WEAPON_ATK_COST[a - i])
    return rank(costs)

def cost_of_def(d, rank):
    costs = []
    for i, v in enumerate(RING_DEF_COST):
        if d-i <= 5:
            costs.append(v + ARMOR_DEF_COST[d - i])
    return rank(costs)

def main():
    player_atk = 7
    player_def = 4
    print("TTK", ttk(player_atk, BOSS_ARMOR, BOSS_HP), "turns for", cost_of_atk(player_atk, min), "gold")
    print("TTD", ttk(BOSS_DAMAGE, player_def, PLAYER_HP), "turns for", cost_of_def(player_def, min), "gold")
    player_atk = 7
    player_def = 3
    print("TTK", ttk(player_atk, BOSS_ARMOR, BOSS_HP), "turns for", cost_of_atk(player_atk, max), "gold")
    print("TTD", ttk(BOSS_DAMAGE, player_def, PLAYER_HP), "turns for", cost_of_def(player_def, max), "gold")

if __name__ == "__main__":
    main()
