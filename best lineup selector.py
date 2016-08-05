import random

def remove_key(role):
    del d_top[role]
    del d_jungle[role]
    del d_mid[role]
    del d_adc[role]
    del d_support[role]

def Random_role(role): #DOESNT WORK
    role = random.choice(list(d_role.keys())) #select random for role from dict
    score += d_role[role] #add score of person to total
    remove_key(role) #remove person from other dicts

best_score = 0

loop =  0
while loop < 100000:
    loop += 1

    d_top = {'sono':5,'coup':30,'eden':143,'crazy':85,'innoxious':5,}
    d_jungle = {'sono':8,'coup':112,'eden':63,'crazy':14,'innoxious':2,}
    d_mid = {'sono':4,'coup':32,'eden':424,'crazy':204,'innoxious':16,}
    d_adc = {'sono':8,'coup':16,'eden':55,'crazy':32,'innoxious':150,}
    d_support = {'sono':77,'coup':15,'eden':304,'crazy':65,'innoxious':20,}

    score = 0

    top = random.choice(list(d_top.keys())) 
    score += d_top[top]
    remove_key(top)

    jungle = random.choice(list(d_jungle.keys()))
    score += d_jungle[jungle]
    remove_key(jungle)

    mid = random.choice(list(d_mid.keys()))
    score += d_mid[mid]
    remove_key(mid)

    adc = random.choice(list(d_adc.keys()))
    score += d_adc[adc]
    remove_key(adc)

    support = random.choice(list(d_support.keys()))
    score += d_support[support]
    remove_key(support)

    #print('top: '+top)
    #print('jungle: '+jungle)
    #print('mid: '+mid)
    #print('adc: '+adc)
    #print('support: '+support)
    #print ('')
    #print('score: '+str(score))

    if score > best_score:
        best_top = top
        best_jungle = jungle
        best_mid = mid
        best_adc = adc
        best_support = support
        best_score = score

print('')
print('----------------------------------------')
print('')
print('best score: '+str(best_score))
print('with lineup:')
print('top: '+best_top)
print('jungle: '+best_jungle)
print('mid: '+best_mid)
print('adc: '+best_adc)
print('support: '+best_support)

    
