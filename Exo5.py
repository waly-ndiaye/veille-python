# affichage des dix nombres suivants

numb = int (input("Entrer un nombre : "))

for i in range(1, 11):
    print(i+numb, end=" ")