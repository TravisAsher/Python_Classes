# -*- coding: utf-8 -*-
"""
Player classes
"""


import random as rn
import textwrap
    # We import 'textwrap' to eliminate extra indents/spacing in multi-line strings



enemy_type = ["goblin","orc","troll","wizard"]
enemy_reward = [(5,10,2),(20,13,4),(50,25,7),(100,35,10)]
enemy_coll = {}
for x in range(0,len(enemy_type)):
    enemy_coll.update({enemy_type[x]: enemy_reward[x]})
    

class Player:
    def __init__(self,name="Player",hp=100,xp=0,gp=0,alive=True):
        self.name = name
        self.hp= hp
        self.xp = xp
        self.gp = gp
        self.alive = alive
        
    def spend(self,amt):
        if amt <= self.gp:
            self.gp -= amt
            print(f"You spent {amt} gp. You now have {self.gp} gp.")
            return True
        else:
            print("You do not have the required funds.")
            return False

    def end_battle(self,enemy):
        if self.hp <= 0:
            self.alive = False
            print("You have died. Game over!")
            return False
        else:
            if enemy not in enemy_type:
                invalid_message = f"""
                '{enemy}' is not a valid enemy type. Valid enemies are as follows:
                '{', '.join(enemy_type)}'
                """
                print(textwrap.dedent(invalid_message).strip())
                return False
            else:
                (reward_xp, reward_gp, variance) = (enemy_coll[enemy][0], enemy_coll[enemy][1],
                enemy_coll[enemy][2])
                gained_xp = rn.randint(reward_xp-variance,reward_xp+variance)
                gained_gp = rn.randint(reward_gp-(2*variance),reward_gp+(2*variance))
                self.xp += gained_xp
                self.gp += gained_gp
                print(f"Battle won! Earned {gained_xp} xp and found {gained_gp} gp!")
                return True