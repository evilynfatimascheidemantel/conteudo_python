primeiro = int(input("Insira o valor do primeiro produto: "))
segundo = int(input("Insira o valor do segundo produto: "))
terceiro = int(input("Insira o valor do terceiro produto: "))

if primeiro < segundo and primeiro < terceiro:
    print("O item com o menor valor é o primeiro:",primeiro)
elif segundo < primeiro and segundo < terceiro:
    print("O item com o menor valor é o segundo:",segundo)
elif terceiro <primeiro and terceiro < segundo:
    print("o item o menor valor é o terceiro:",terceiro)