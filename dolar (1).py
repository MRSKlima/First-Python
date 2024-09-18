

#Exercicio 2
#'''
#Mostrar um programa em Python para calcular os juros de uma conta atrasada:

#Pedir:
#1-) Valor da conta
#2-) dias de atraso
#3-) Juros por dia

#Fórmula:
#Valor Corrigido = valorDaConta + (ValorDaConta * diasAtraso * jurosPorDia)
#'''
while True:
    valorDaConta = float(input ("Digite o valor da conta: R$ "))
    diasAtraso = int(input("Digite a quantidade de dias atrasado: "))
    jurosPordia = float(input("Informe o Juros por Dia: % "))

    valorCorrigido = valorDaConta + (valorDaConta * diasAtraso * (jurosPordia/100))
    print(f"O novo valor corrigido com o Juros é: R$ {valorCorrigido:.2f} reais ")
    sair = input("Deseja realizar outro calculo? <S/N>")
    if sair.upper() == "N":
        break



