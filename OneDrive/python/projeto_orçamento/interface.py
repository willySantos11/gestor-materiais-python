import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema de orçamentos do Willy")
janela.geometry("400x300")
janela.configure(bg = "#2c3e50")

texto_total = tk.Label(janela,
bg = "#2c3e50",
fg = "white",
font = ("Arial", 14, "bold"))
texto_total.pack()   
            
def mostrar_janela_erro(mensagem):
    janela_erro = tk.Toplevel()
    janela_erro.geometry("300x150")
    
    texto_erro = tk.Label(janela_erro,
    text = mensagem,
    font = ("arial", 14))
    texto_erro.pack()
    
    botao_OK = tk.Button(janela_erro,
    text = "OK",
    command = janela_erro.destroy,
    font = ("arial", 10))
    botao_OK.pack()
    
def atualizar_total():
    soma = 0
    with open("relatorio.txt", "r") as arquivo:
        for linha in arquivo:
            if "R$" in linha:
                partes = linha.split("R$")
                valor = partes[1].strip()
                soma = soma + float(valor)
    texto_total.config(text = f"Total: R$ {soma:.2f}")

def limpar_tela():
    resposta = messagebox.askyesno("Atenção", "Tem certeza que deseja deletar?")
    if resposta == True:
        with open("relatorio.txt", "w") as arquivo:
            pass
        atualizar_total()    
        
def enviar_dados():
    conteudo = entrada.get()
    valor_material = entrada_preco.get()
    if not conteudo :
        mostrar_janela_erro("Digite o material que deseja!") 
    elif not valor_material:
        mostrar_janela_erro("informe o valor do material!")
    else:
        with open("relatorio.txt", "a") as arquivo:
            arquivo.write(f"{conteudo} - R${valor_material}\n")
            entrada.delete(0, tk.END)
            entrada_preco.delete(0,tk.END)
        atualizar_total() 

texto = tk.Label(janela,
text ="Bem-vindo ao sistema de obra!",
font = ("Arial", 14),
bg = "#2c3e50",
fg = "white")
texto.pack(pady = 20)

texto2 = tk.Label(janela,
text = "Digite o material que deseja",
font = ("Arial", 12),
bg = "#2c3e50",
fg = "white")
texto2.pack(pady = 20)

entrada = tk.Entry(janela)
entrada.pack(pady = (0, 15))

valor = tk.Label(janela,
text ="Digite o valor R$",
font = ("Arial", 12),
bg = "#2c3e50",
fg = "white")
valor.pack(pady = 10)

entrada_preco = tk.Entry(janela)
entrada_preco.pack()

botao = tk.Button(janela,
text = "Salvar Materiais",
padx = 20,
pady = 5,
command = enviar_dados,
font = ("Arial", 10),
bg = "#27ae60",
fg = "white")
botao.pack(pady = 10)

botao_deletar = tk.Button(janela,
text = "Deletar",
padx = 20,
pady = 5,
command = limpar_tela,
font = ("Arial", 10),
bg = "red",
fg = "white")
botao_deletar.pack(pady = 10)

atualizar_total()

janela.mainloop()