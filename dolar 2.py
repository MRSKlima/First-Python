print("Agradeço pela visita. Volte Sempre que precisar")
print("Sistema de Conversão do  Dólar")
print("Desenvolvido por: Krebzin ")
print("Copywrite 2024")
print("Versão 0.1")

while True:
    valorEmDolar = float(input("Valor do produto em Dólar: US$ "))
    cotacaoDolarHoje = float(input("Digite a cotação de dólar: R$ "))
    
    valorConvertido = (valorEmDolar * cotacaoDolarHoje)

    print(f"O Valor convertido é: R$ {valorConvertido:.2f} reais") # O "f" no começo do print é pra mencionar uma ou + variaveis no conjunto em CHAVES, e o .2f dentro da chaves significa para aperecer 2 casas decimais.
    sair = input("Deseja converter outro valor? <S/N>")
    if sair.upper() == "N":
        ...