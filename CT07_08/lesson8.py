

import random
hp = 100
turns = 0





while hp > 0:
    (hp) = (hp) - random.randint(1,15)
    (turns) = (turns) + 1
    if hp < 1:
        print ((turns))
    else:
        print (hp)





print (turns) 
print (hp)

