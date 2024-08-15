#nome= input("qual o seu nome amigo? " )
#idade= input("qual a sua idade tambem? ")
#print ("Caraca",nome,"você ja tem tem", idade,"anos!!! Já está bem velho hein kkkkkk")
#idade = int (input("ohhh brother qual a sua idade ai? "))
#print ("vamos contar a sua idade...")
#for contador in range (idade+1):
#  print ("e",contador)

sair = "N"

while sair != "S":
    nome = input ("digite seu nome ai parceiro: ")
    for letra in nome:
        print (letra)
    print ("**********************")
    sair = input("Sair do programa? (S/N): ")