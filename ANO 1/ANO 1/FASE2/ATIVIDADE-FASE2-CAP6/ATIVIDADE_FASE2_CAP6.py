import json

TIPOS_VALIDOS = ("manual", "mecanica")

colheitas = []

def cadastrar_colheita():
    nome = input("Nome da fazenda: ").strip()

    tipo = input("Tipo de colheita (manual/mecanica): ").lower()
    while tipo not in TIPOS_VALIDOS:
        tipo = input("Digite 'manual' ou 'mecanica': ").lower()

    try:
        producao_esperada = float(input("Produção esperada (ton): "))
        producao_real = float(input("Produção real (ton): "))

        if producao_esperada < 0 or producao_real < 0:
            print("Erro: valores não podem ser negativos!")
            return

    except:
        print("Erro: digite números válidos!")
        return

    perda = calcular_perda(producao_esperada, producao_real)


    if perda > 10:
        print("Atenção: perda acima de 10%!")

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
    # Evita divisão por zero
    if esperado == 0:
        return 0

    perda = ((esperado - real) / esperado) * 100
    return round(perda, 2)


def mostrar_dados():
    if not colheitas:
        print("\nNenhuma colheita cadastrada.\n")
        return

    print("\n=== DADOS DAS COLHEITAS ===")

    for i, c in enumerate(colheitas, 1):
        print(f"\nColheita {i}")
        print(f"Fazenda: {c['nome']}")
        print(f"Tipo: {c['tipo']}")
        print(f"Produção esperada: {c['esperado']} ton")
        print(f"Produção real: {c['real']} ton")
        print(f"Perda: {c['perda_percentual']}%")


def salvar_json():
    try:
        with open("colheitas.json", "w") as f:
            json.dump(colheitas, f, indent=4)
        print("Dados salvos em JSON!")
    except:
        print("Erro ao salvar arquivo.")


def carregar_json():
    global colheitas
    try:
        with open("colheitas.json", "r") as f:
            colheitas = json.load(f)
    except:
        colheitas = []
    print("Dados carregados!")



def menu():
    carregar_json()

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