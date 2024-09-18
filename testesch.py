import tkinter as tk
from tkinter import ttk

# Função para atualizar o rótulo com a seleção da combobox
def mostrar_selecao():
    selecionado = combobox_selecao.get()
    label_resultado.config(text=f"Você selecionou: {selecionado}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Exemplo com Opções Pré-definidas")

# Rótulo
label_novo = tk.Label(janela, text="Nível do problema")
label_novo.grid(row=0, column=0)

# Opções para a combobox
opcoes = ["Baixo", "Médio", "Alto"]

# Combobox
combobox_selecao = ttk.Combobox(janela, values=opcoes)
combobox_selecao.set("Escolha um nível")  # Valor inicial
combobox_selecao.grid(row=0, column=1)

# Botão para mostrar a seleção
botao_mostrar = tk.Button(janela, text="Mostrar Seleção", command=mostrar_selecao)
botao_mostrar.grid(row=1, columnspan=2)

# Rótulo para exibir a seleção
label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=2, columnspan=2)

# Iniciar o loop da interface gráfica
janela.mainloop()
