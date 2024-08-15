import random
numero= random.randint(1,20)
print ("Bem-vindo ao jogode advinhação!")
print ("Tente advinhar o número que estou pensando entre 1 e 20.")
while True:
    palpite= int(input("qual o seu palpite?"))
    if palpite == numero:
        print("#$@## você acertou")
    elif palpite > numero:
        print("voçê chutou alto")
    else:
        print("voçê chutou baixo")