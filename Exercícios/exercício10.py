print ("especifique o seu turno: M-Matutino V-Verspertino N-Noturno")
turno = input("Digite o turno: ")

if turno == "M" or turno == "m":
    print ("Bom dia!")
elif turno == "V" or turno == "v":
    print ("Boa tarde!")
elif turno == "N" or turno == "n":
    print ("Boa noite!")
else:
    print ("Valor invalido!")