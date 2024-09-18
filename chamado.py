import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

# Função para calcular o total do pedido

# Função para salvar o problema em um arquivo JSON
def salvar_pedido():
    nome_do_cliente= entry_nome.get()
    #tipo_de_problema = entry_quantidade.get()
    preco_unitario = entry_preco.get()

    #if not nome_do_cliente or not tipo_de_problema or not preco_unitario:


    # Estrutura do chamado
    pedido = {
        "nome_lanche": nome_do_cliente,
        #"quantidade": tipo_de_problema,
        "preco_unitario": preco_unitario,
    }

    # Verifica se o arquivo JSON já existe
    if os.path.exists("pedidos.json"):
        with open("pedidos.json", "r") as arquivo:
            pedidos = json.load(arquivo)
    else:
        pedidos = []

    # Adiciona o novo pedido
    pedidos.append(pedido)

    # Salva no arquivo JSON
    with open("pedidos.json", "w") as arquivo:
        json.dump(pedidos, arquivo, indent=4)

    messagebox.showinfo("Sucesso", "Pedido salvo com sucesso!")

    # Limpa os campos após salvar
    limpar_campos()

# Função para exibir um pedido específico
def recuperar_pedido():
    if os.path.exists("pedidos.json"):
        nome_lanche = simpledialog.askstring("Recuperar Pedido", "Digite o nome do lanche:")
        if not nome_lanche:
            return

        with open("pedidos.json", "r") as arquivo:
            pedidos = json.load(arquivo)

        # Procura o pedido pelo nome do lanche
        for pedido in pedidos:
            if pedido["nome_lanche"].lower() == nome_lanche.lower():
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, pedido["nome_lanche"])
                #entry_quantidade.delete(0, tk.END)
                #entry_quantidade.insert(0, pedido["quantidade"])
                entry_preco.delete(0, tk.END)
                entry_preco.insert(0, pedido["preco_unitario"])
                return

        messagebox.showinfo("Pedido não encontrado", f"Pedido com nome '{nome_lanche}' não encontrado.")
    else:
        messagebox.showinfo("Sem Pedidos", "Nenhum pedido cadastrado até o momento.")


def mostrar_selecao():
    selecionado = combobox_selecao.get()


# Função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    #entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_nome.focus()

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Pedidos de Lanches")
janela.geometry("370x140")

# Labels e Entries para os campos
label_nome = tk.Label(janela, text="Cliente")
label_nome.grid(row=0, column=0)

entry_nome = tk.Entry(janela, width=23)
entry_nome.grid(row=0, column=1)

label_quantidade = tk.Label(janela, text="Tipo de problema")
label_quantidade.grid(row=1, column=0)

opcoes = ["Falha do software", "Problema de Rede", "Erro de Hardware"]

# Combobox

combobox_quantidade = ttk.Combobox(janela, values=opcoes)
combobox_quantidade.grid(row=1, column=1)
#entry_quantidade = tk.Entry(janela)
#entry_quantidade.grid(row=1, column=1)

label_preco = tk.Label(janela, text="Descrição do problema")
label_preco.grid(row=2, column=0)

entry_preco = tk.Entry(janela, width=23)
janela.rowconfigure(2, minsize=30)
entry_preco.grid(row=2, column=1)

label_novo = tk.Label(janela, text="Nível do problema")
label_novo.grid(row=3, column=0)

# Opções para a combobox
opcoes = ["Baixo", "Médio", "Alto"]

# Combobox
combobox_selecao = ttk.Combobox(janela, values=opcoes)
combobox_selecao.set("Escolha um nível")  # Valor inicial
combobox_selecao.grid(row=3, column=1)

#botões para definit pedido

botao_novo_pedido = tk.Button(janela, text="Novo chamado", width=17, command=limpar_campos)
botao_novo_pedido.grid(row=5, column=0)

botao_salvar = tk.Button(janela, text="Salvar chamado", width=17, command=salvar_pedido)
botao_salvar.grid(row=5, column=1)

botao_recuperar = tk.Button(janela, text="Localizar Chamado", width=17, command=recuperar_pedido)
botao_recuperar.grid(row=6, column=0)

janela.mainloop()
