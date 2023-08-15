
import random



doors = [0]*3                                           # empty door list
goatdoor = [0]*2                                        # empty goatdoor list
swap = 0                                                # swap wins
dont_swap = 0                                           # without swap wins
j = 0
while(j<10):                                                # wwhile loop to keep a track of win types 
    x = random.randint(0,2)                                 # random 1 door among 3 doors (0, 1, 2)
    doors[x] = "BMW"                                        # that 1 door has BMW
    # rest doors to have goats
    for i in range(0,3):                                    # for i in range o - 3 (0, 1, 2)
        if(i == x):
            continue
        else:
            doors[i] = "GOAT"
            goatdoor.append(i)                              # to keep the track fo door having goats
                                                            # at end of for loop there must be goatdoors        
        
    choice = int(input("plz, enter the choice : "))
    door_open = random.choice(goatdoor)                     # opening random door among the goatdoor    
    while(door_open == choice):                             # for door_open shouldn't be equal to choice of participant
        door_open = random.choice(goatdoor)                 # again choose random door among goatdoor
    
    
    ch = input("hey!! Do you want to swap (y/n) - ")
    if(ch == 'y'):
        if(doors[choice] == 'GOAT'):                        # if initial choice of doors was goat, then swapping here makes him win.
            print("Congratulations! you won")
            swap = swap + 1
        else:
            print("opss!!! sorry you lost")
    else:
        if(doors[choice] == 'GOAT'):
            print("opss!!! sorry you lost")
        else:
            print("Congratulations! you won")
            dont_swap = dont_swap + 1 
    j = j + 1 
        
print("total swap wins : ", swap)
print("total without swap wins : ", dont_swap)
    
