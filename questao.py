#criar um comando que tenha que colocar o o estado a cidade e um pedaço da rua
#para que assim informe o CEP


import tkinter as tk
from tkinter import messagebox
import requests


def buscar_endereco():
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    rua = entry_rua.get().strip()
    
    url = f"https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        dados = dados[0]
        
        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            endereco = (
                f"CEP:{dados['cep']}\n"
            )
            label_resultado.config(text=endereco)
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")

# Configurando a janela principal
root = tk.Tk()
root.title("Busca de Endereço pelo CEP")
root.geometry("300x250")

#campo para a entrada da cidade
label_cidade = tk.Label(root, text="Digite o nome da cidade:")
label_cidade.pack(pady=5)
entry_cidade = tk.Entry(root)
entry_cidade.pack(pady=5)

# Campo de entrada para o rua
label_rua = tk.Label(root, text="Digite o nome da rua:")
label_rua.pack(pady=5)
entry_rua = tk.Entry(root)
entry_rua.pack(pady=5)

#campode entrada para Estado
label_estado = tk.Label(root, text="Digite o nome do Estado:")
label_estado.pack(pady=5)
entry_estado = tk.Entry(root)
entry_estado.pack(pady=5)

# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Buscar Endereço", command=buscar_endereco)
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()


#COMANDO EXECUTADO COM SUCESSO E FUNCIONANDO