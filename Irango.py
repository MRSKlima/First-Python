#crie um setor de cadastro e execute um cálculo junto á ele


import tkinter as tk
from tkinter import messagebox



def calcular_e_exibir_total(): 
    try:
    # Obtendo os valores inseridos
        preco = float(entry_preco.get())
        quantidade = float(entryquantidade.get())
        
        # Calculando o total
        total = preco * quantidade
        
        # Exibindo a mensagem
        messagebox.showinfo("Resultado", f"O valor total é: R$ {total:.2f}")
    except ValueError:
        # Tratamento de erro para valores inválidos
        messagebox.showerror("Erro", "Por favor, insira valores válidos para preço e quantidade.")


janela = tk.Tk()
janela.title("Sistema IRango alpha 1.0")

    #titulo de boas vindas
labelnome = tk.Label(janela,text="faça seu pedido já!ಥ_ಥ", font=("Verdana", 18))
labelnome.pack(padx=50, pady=5)

    #Inserir nome do Lanche
labelnome = tk.Label(janela,text="Nome do lanche")
labelnome.pack(padx=50, pady=5)

entrynome = tk.Entry(janela, width=90)
entrynome.pack(padx=50, pady=5)

    #***Quantidade do(s)lanches

labelquantidade = tk.Label(janela,text="Quantidade")
labelquantidade.pack(padx=50, pady=5)
entryquantidade = tk.Entry(janela, width= 5)
entryquantidade.pack(padx=50, pady=5)

label_preco = tk.Label(janela, text="Preço do Lanche: R$")
label_preco.pack(pady=5)

entry_preco = tk.Entry(janela)
entry_preco.pack(pady=5)

button_calcular = tk.Button(janela, text="Calcular Total", command=calcular_e_exibir_total)
button_calcular.pack(pady=20)

janela.geometry("400x300")
janela.mainloop()
