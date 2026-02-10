# https://adventofcode.com/2015/day/21

from scipy.optimize import linprog
import numpy as np

BOSS_HP = 109
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

PLAYER_HP = 100

# Cost, Atk, Def, IsWeap, IsArm, IsRing
EQUIPMENT = [[8, 4, 0, 1, 0, 0],
             [10, 5, 0, 1, 0, 0],
             [25, 6, 0, 1, 0, 0],
             [40, 7, 0, 1, 0, 0],
             [74, 8, 0, 1, 0, 0],
             [13, 0, 1, 0, 1, 0],
             [31, 0, 2, 0, 1, 0],
             [53, 0, 3, 0, 1, 0],
             [75, 0, 4, 0, 1, 0],
             [102, 0, 5, 0, 1, 0],
             [25, 1, 0, 0, 0, 1],
             [50, 2, 0, 0, 0, 1],
             [100, 3, 0, 0, 0, 1],
             [20, 0, 1, 0, 0, 1],
             [40, 0, 2, 0, 0, 1],
             [80, 0, 3, 0, 0, 1]]

def ttk(dmg, arm, hp):
    dpt = max(dmg-arm, 1)
    return int(hp / dpt)
    
def eqpt_row(n):
    return [v[n] for v in EQUIPMENT]

def cost_to_win(turns):
    costs = eqpt_row(0)
    A_ub = []
    b_ub = []
    A_eq = []
    b_eq = []
    # At most one armor
    A_ub += [eqpt_row(4)]
    b_ub += [1]
    # At most two rings
    A_ub += [eqpt_row(5)]
    b_ub += [2]
    # Exactly one weapon
    A_eq += [eqpt_row(3)]
    b_eq += [1]
    # Must be alive after n-1 boss strikes
    A_ub += [[-(turns-1) * d for d in eqpt_row(2)]]
    b_ub += [-(turns-1) * BOSS_DAMAGE + PLAYER_HP - 1]
    # Must kill boss in n player strikes
    A_ub += [[-turns * a for a in eqpt_row(1)]]
    b_ub += [-turns * BOSS_ARMOR - BOSS_HP]
    # Only one available of any item
    bounds = [(0,1)] * len(EQUIPMENT)
    result = linprog(np.array(costs),
                     A_ub=np.array(A_ub),
                     b_ub=np.array(b_ub),
                     A_eq=np.array(A_eq),
                     b_eq=np.array(b_eq),
                     bounds=bounds,
                     integrality=1)
    return result.fun

def cost_to_lose(turns):
    costs = [-i for i in eqpt_row(0)]
    A_ub = []
    b_ub = []
    A_eq = []
    b_eq = []
    # At most one armor
    A_ub += [eqpt_row(4)]
    b_ub += [1]
    # At most two rings
    A_ub += [eqpt_row(5)]
    b_ub += [2]
    # Exactly one weapon
    A_eq += [eqpt_row(3)]
    b_eq += [1]
    # Must be dead after n boss strikes
    A_ub += [[turns * d for d in eqpt_row(2)]]
    b_ub += [turns * BOSS_DAMAGE - PLAYER_HP]
    # Must not kill boss in n player strikes
    A_ub += [[turns * a for a in eqpt_row(1)]]
    b_ub += [turns * BOSS_ARMOR + BOSS_HP]
    # Only one available of any item
    bounds = [(0,1)] * len(EQUIPMENT)
    result = linprog(np.array(costs),
                     A_ub=np.array(A_ub),
                     b_ub=np.array(b_ub),
                     A_eq=np.array(A_eq),
                     b_eq=np.array(b_eq),
                     bounds=bounds,
                     integrality=1)
    return result.fun

def main():
    for i in range(10, 30):
        print(f"It costs at least {cost_to_win(i)} to win in {i} turns")
    for i in range(10, 30):
        print(f"It costs at most {cost_to_lose(i)} to lose in {i} turns")

if __name__ == "__main__":
    main()
