rodar = "S"
#while rodar =="S" or rodar == "s":
while rodar.upper() == "S" :
    operacao = input("digite 1-adição, 2-subtração, 3-multipliação, 4-disisão ")
    print("Seja bem vindo ao meu mundo de cálculos o que voçê deseja cálcular hoje?")
    if not operacao.isdigit():
        continue
    if int (operacao) > 4 or int(operacao)< 1:
        continue

    numero1 = float(input("digite um número: "))
    numero2 = float(input("digite outro número "))
    if operacao == "1":
        resultado = numero1 + numero2
    elif operacao == "2":
        resultado = numero1 - numero2
    elif operacao == "3":
        resultado = numero1 * numero2
    elif operacao =="4":
        resultado = numero1 / numero2
    print ("O resultado é :", resultado)
    rodar = input("deseja fazer outra conta? <S/N>: ")
    while rodar.upper() != "S" and rodar.upper() != "N":
        rodar = input("opção inválida. Digite S ou N-> ")
    