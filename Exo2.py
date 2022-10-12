# Nombre Entier

user_input = int(input("Entrer un nombre entier : "))

number_list = [i for i in range(11)]

for i in number_list:
    print("{}x{} = {}".format(user_input, i, user_input*i))