#!/usr/bin/env python
# coding: utf-8

# In[26]:


import random

def Game(comp,player):
    if comp == player:
        return None
    elif comp == "s":
        if player == "g":
            return True
        else:
            player == "w"
            return False
    elif comp == "w":
        if player== "s":
            return True
        else:
            player == "g"
            return False
    elif comp == "g":
        if player == "w":
            return True
        else:
            player == "s"
            return False
print("Computer Turn: Snake(s) , Water(w), Gun(g)")
rand = random.randint(1,3)
if rand == 1:
    comp = "s"
elif rand == 2:
     comp = "w"
else:
    rand == 3
    comp = "g"
    
player = input("player turn: Snake(s) , Water(w), Gun(g)\nEnter your option(s/w/g): ")
c = Game(comp,player)
print(f"player: {player}")
print(f"computer: {comp}")
if c == None:
    print("##### Game Tie #####")
elif c == True:
    print("##### player Won #####")
else:
    c == False
    print("##### computer Won #####")


# In[ ]:




