def adicao(numA, numB):
    return numA+ numB
def subtracao (numA,numB):
    return numA-numB



print ("Escola uma opção: ")
print ("1 - adição")
print ("2 - subtração")
print ("3 - multiplicação")
print ("4 - divisão")

opcao = input ("Digite a opção desejada: ")

if opcao == "1":
    numeroA = float(input("Digite o primeiro número: "))
    numeroB =float(input("digite o segundo número: "))
    resultado = adicao(numeroA,numeroB)
    #print ("o resultado é", resultado)
elif opcao == "2":
    numeroA = float(input("digite o primeiro numero: "))
    numeroB = float(input("digite o segundo número: "))
    resultado = subtracao (numeroA,numeroB)
    #print ("o resultado é", resultado)

    print (f"O resultado é {resultado:.2f}")