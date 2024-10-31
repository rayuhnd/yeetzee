import random      

def re_roll(keep, roll):    
    user_re_roll=keep    
    split_re_roll=user_re_roll.split() 
    lst_keep=[]
    #appendar lst_keep med inedx i roll
    for index in split_re_roll:     
        if int(index) - 1 < len(roll): 
            lst_keep.append(roll[int(index) - 1]) 
    #print(lst_keep)  

    #rullar om index som inte är i keep 
    roll = []
    for i in lst_keep: 
        roll.append(i) 

    for i in range(5-len(roll)):
        rand = random.randint(1,6) 
        roll.append(rand)
    return roll  
