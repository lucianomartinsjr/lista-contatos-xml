import xml.etree.ElementTree as ET
import os

def salvar_contatos_arquivo(contatos, nome_arquivo):
    root = ET.Element("lista-contatos")

    for contato in contatos:
        elemento_contato = ET.Element("contato")
        ET.SubElement(elemento_contato, "nome").text = contato.nome
        ET.SubElement(elemento_contato, "telefone").text = contato.telefone
        ET.SubElement(elemento_contato, "email").text = contato.email
        root.append(elemento_contato)

    tree = ET.ElementTree(root)
    tree.write(nome_arquivo)

def ler_contatos_arquivo(nome_arquivo):
    contatos = []

    if os.path.exists(nome_arquivo):
        tree = ET.ElementTree(file=nome_arquivo)
        root = tree.getroot()

        for elemento_contato in root.findall("contato"):
            nome = elemento_contato.find("nome").text
            telefone = elemento_contato.find("telefone").text
            email = elemento_contato.find("email").text
            contatos.append(Contato(nome, telefone, email))

    return contatos

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

def adicionar_contato(contatos,nome_arquivo):
    nome = input("\nNome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    novo_contato = Contato(nome, telefone, email)
    contatos.append(novo_contato)
    
    salvar_contatos_arquivo(contatos, nome_arquivo)
    print("\nContato adicionado com sucesso!")
    

def listar_contatos(contatos):
    if not contatos:
        print("\n-=-=-=-=- Lista de Contatos -=-=-=-=-")
        print("Nenhum contato cadastrado.")
        print("-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=-=-") 
    else:
        print("\n-=-=-=-=- Lista de Contatos -=-=-=-=-")
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. Nome: {contato.nome}, Telefone: {contato.telefone}, E-mail: {contato.email}")
        print("-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=-=-")    
        

def remover_contato(contatos,nome_arquivo):
    listar_contatos(contatos)
    if not contatos:
        return
    try:
        indice = int(input("\nDigite o número do contato que deseja remover: ")) - 1
        if 0 <= indice < len(contatos):
            contato_removido = contatos.pop(indice)
            print(f"\n- Contato {contato_removido.nome} removido com sucesso! - ")
            
            salvar_contatos_arquivo(contatos, nome_arquivo)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite o número do contato que deseja remover.")


def main():
    nome_arquivo = "contatos.xml"
    contatos = ler_contatos_arquivo(nome_arquivo)

    while True:
        print("\nOpções:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contato")
        print("4. Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            adicionar_contato(contatos,nome_arquivo)
        elif escolha == '2':
            listar_contatos(contatos)
        elif escolha == '3':
            remover_contato(contatos,nome_arquivo)
        elif escolha == '4':
            salvar_contatos_arquivo(contatos, nome_arquivo)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()