# Combinaisons de 3 chiffres

for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            if i < j < k:
                print(f"{i}{j}{k}",end=",")