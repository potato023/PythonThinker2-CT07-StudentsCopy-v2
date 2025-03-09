

import random
hp = 100
turns = 0





for i in (100):
    if hp > 0:
        (hp) = (hp) - random.randint(1,15)
        (turns) = (turns) + 1
        print (hp)
    elif hp < 1:
        print (turns)




print (turns) 
print (hp)

