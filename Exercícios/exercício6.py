primeiro = int(input("Insira o primeiro número: "))
segundo = int(input("Insira o segundo número: "))
terceiro = int(input("Insira o terceiro número: "))

if primeiro > segundo and primeiro > terceiro:
    print("O valor maior é o", primeiro)
elif segundo > primeiro and segundo > terceiro:
    print("O valor maior é o", segundo)
elif terceiro > primeiro and terceiro > segundo:
    print("O valor maior é o",terceiro)