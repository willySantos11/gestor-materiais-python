from datetime import datetime
materiais = []
total_geral = 0
continuar = "sim"
def exibir_relatorio(materiais, total_geral):
    print(f"Materiais escolhidos: {materiais}")
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%y, %H:%M:%S")
    print(f"Total final R${total_geral}")
    print(f"{data_formatada}")
    
    with open ("relatorio.txt", "a") as arquivo: 
        arquivo.write(f"Total:{total_geral}\n")
        arquivo.write(f"Materiais:{materiais}\n")
        

def verificar_orcamento(total):
    if total > 500:
        return "Orçamento estourado!"
    else:
        return "Orçamento aprovado!"
    
while continuar == "sim":
    item = input("Informe o produto que deseja: ")
    materiais.append(item)
    preco_material = float(input("Informe o valor do produto R$ "))
    total_geral += preco_material
    continuar = input("Deseja algo mais ? (sim/não)")
    
exibir_relatorio(materiais, total_geral)
status = verificar_orcamento(total_geral)
print(status)