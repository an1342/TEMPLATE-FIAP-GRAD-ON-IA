import json

colheitas = []

def cadastrar_colheita():
    nome = input("Nome da fazenda: ")

    tipo = input("Tipo de colheita (manual/mecanica): ").lower()
    while tipo not in ["manual", "mecanica"]:
        tipo = input("Digite 'manual' ou 'mecanica': ")

    try:
        producao_esperada = float(input("Produção esperada (ton): "))
        producao_real = float(input("Produção real (ton): "))
    except:
        print("Erro: digite números válidos!")
        return

    perda = calcular_perda(producao_esperada, producao_real)

    colheita = {
        "nome": nome,
        "tipo": tipo,
        "esperado": producao_esperada,
        "real": producao_real,
        "perda_percentual": perda
    }

    colheitas.append(colheita)
    print("Colheita cadastrada com sucesso!\n")



def calcular_perda(esperado, real):
    perda = ((esperado - real) / esperado) * 100
    return round(perda, 2)



def mostrar_dados():
    if not colheitas:
        print("Nenhuma colheita cadastrada.")
        return

    for c in colheitas:
        print("\n--- COLHEITA ---")
        print(f"Fazenda: {c['nome']}")
        print(f"Tipo: {c['tipo']}")
        print(f"Perda: {c['perda_percentual']}%")



def salvar_json():
    with open("colheitas.json", "w") as f:
        json.dump(colheitas, f, indent=4)
    print("Dados salvos em JSON!")


def carregar_json():
    global colheitas
    try:
        with open("colheitas.json", "r") as f:
            colheitas = json.load(f)
        print("Dados carregados!")
    except:
        print("Arquivo não encontrado.")


def menu():
    while True:
        print("\n=== SISTEMA AGRO ===")
        print("1 - Cadastrar colheita")
        print("2 - Mostrar dados")
        print("3 - Salvar em JSON")
        print("4 - Carregar JSON")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_colheita()
        elif op == "2":
            mostrar_dados()
        elif op == "3":
            salvar_json()
        elif op == "4":
            carregar_json()
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")
menu()
