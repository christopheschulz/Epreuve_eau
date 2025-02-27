# Combinaisons de 2 nombres

for one in range (0,99):
    for two in range (one+1,100):
        if one != two:
            
            print(f" {str(one).zfill(2)} {str(two).zfill(2)}",end=",")