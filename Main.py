import os
import random

NUM_LOTOFACIL = 15
MIN_NUM_LOTOFACIL = 1
MAX_NUM_LOTOFACIL = 25

NUM_MEGA_SENA = 6
MIN_NUM_MEGA_SENA = 1
MAX_NUM_MEGA_SENA = 60

NUM_QUINA = 5
MIN_NUM_QUINA = 1
MAX_NUM_QUINA = 80

def limpar_tela():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def fazer_sorteio_loto_facil():
    numeros_sorteados = random.sample(range(MIN_NUM_LOTOFACIL, MAX_NUM_LOTOFACIL + 1), NUM_LOTOFACIL)
    numeros_sorteados.sort()
    return numeros_sorteados

def escolher_numeros_loto_facil():
    print(f"Escolha {NUM_LOTOFACIL} números entre {MIN_NUM_LOTOFACIL} e {MAX_NUM_LOTOFACIL}:")
    print("----------------------------------------------------\n")
    numeros_escolhidos = []
    for i in range(1, NUM_LOTOFACIL + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                if MIN_NUM_LOTOFACIL <= numero <= MAX_NUM_LOTOFACIL and numero not in numeros_escolhidos:
                    numeros_escolhidos.append(numero)
                    break
                else:
                    print("Número inválido ou repetido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    numeros_escolhidos.sort()
    return numeros_escolhidos

def salvar_numeros_sorteados_loto_facil(numeros_sorteados):
    with open("numeros_sorteadosLt.txt", "a") as arquivo:
        arquivo.write(" ".join(map(str, numeros_sorteados)) + "\n")

def calcular_estatisticas_loto_facil():
    while True:
        limpar_tela()
        print("Estatísticas da Lotofácil:")
        print("----------------------------------------------------")
        frequencia_numeros = {i: 0 for i in range(MIN_NUM_LOTOFACIL, MAX_NUM_LOTOFACIL + 1)}
        with open("numeros_sorteadosLt.txt", "r") as arquivo:
            for linha in arquivo:
                numeros_sorteados = list(map(int, linha.strip().split()))
                for numero in numeros_sorteados:
                    frequencia_numeros[numero] += 1

        numeros_ordenados = sorted(frequencia_numeros.items(), key=lambda x: x[1], reverse=True)

        for numero, frequencia in numeros_ordenados:
            print(f"Número {numero}: {frequencia} vezes")

        print("----------------------------------------------------")
        retorno = input("\nPressione 0 e Enter para retornar ao Menu Lotofácil...")
        if retorno == "0":
            return

def fazer_sorteio_mega_sena():
    numeros_sorteados = random.sample(range(MIN_NUM_MEGA_SENA, MAX_NUM_MEGA_SENA + 1), NUM_MEGA_SENA)
    numeros_sorteados.sort()
    return numeros_sorteados

def escolher_numeros_mega_sena():
    print(f"Escolha {NUM_MEGA_SENA} números entre {MIN_NUM_MEGA_SENA} e {MAX_NUM_MEGA_SENA}:")
    print("----------------------------------------------------\n")
    numeros_escolhidos = []
    for i in range(1, NUM_MEGA_SENA + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                if MIN_NUM_MEGA_SENA <= numero <= MAX_NUM_MEGA_SENA and numero not in numeros_escolhidos:
                    numeros_escolhidos.append(numero)
                    break
                else:
                    print("Número inválido ou repetido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    numeros_escolhidos.sort()
    return numeros_escolhidos

def salvar_numeros_sorteados_mega_sena(numeros_sorteados):
    with open("numeros_sorteadosMg.txt", "a") as arquivo:
        arquivo.write(" ".join(map(str, numeros_sorteados)) + "\n")

def calcular_estatisticas_mega_sena():
    while True:
        limpar_tela()
        print("Estatísticas da Mega Sena:")
        print("----------------------------------------------------")
        frequencia_numeros = {i: 0 for i in range(MIN_NUM_MEGA_SENA, MAX_NUM_MEGA_SENA + 1)}
        with open("numeros_sorteadosMg.txt", "r") as arquivo:
            for linha in arquivo:
                numeros_sorteados = list(map(int, linha.strip().split()))
                for numero in numeros_sorteados:
                    frequencia_numeros[numero] += 1

        numeros_ordenados = sorted(frequencia_numeros.items(), key=lambda x: x[1], reverse=True)

        for numero, frequencia in numeros_ordenados:
            print(f"Número {numero}: {frequencia} vezes")

        print("----------------------------------------------------")
        retorno = input("\nPressione 0 e Enter para retornar ao Menu Mega Sena...")
        if retorno == "0":
            return

def fazer_sorteio_quina():
    numeros_sorteados = random.sample(range(MIN_NUM_QUINA, MAX_NUM_QUINA + 1), NUM_QUINA)
    numeros_sorteados.sort()
    return numeros_sorteados

def escolher_numeros_quina():
    print(f"Escolha {NUM_QUINA} números entre {MIN_NUM_QUINA} e {MAX_NUM_QUINA}:")
    print("----------------------------------------------------\n")
    numeros_escolhidos = []
    for i in range(1, NUM_QUINA + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                if MIN_NUM_QUINA <= numero <= MAX_NUM_QUINA and numero not in numeros_escolhidos:
                    numeros_escolhidos.append(numero)
                    break
                else:
                    print("Número inválido ou repetido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    numeros_escolhidos.sort()
    return numeros_escolhidos

def salvar_numeros_sorteados_quina(numeros_sorteados):
    with open("numeros_sorteadosQuina.txt", "a") as arquivo:
        arquivo.write(" ".join(map(str, numeros_sorteados)) + "\n")

def calcular_estatisticas_quina():
    while True:
        limpar_tela()
        print("Estatísticas da Quina:")
        print("----------------------------------------------------")
        frequencia_numeros = {i: 0 for i in range(MIN_NUM_QUINA, MAX_NUM_QUINA + 1)}
        with open("numeros_sorteadosQuina.txt", "r") as arquivo:
            for linha in arquivo:
                numeros_sorteados = list(map(int, linha.strip().split()))
                for numero in numeros_sorteados:
                    frequencia_numeros[numero] += 1

        numeros_ordenados = sorted(frequencia_numeros.items(), key=lambda x: x[1], reverse=True)

        for numero, frequencia in numeros_ordenados:
            print(f"Número {numero}: {frequencia} vezes")

        print("----------------------------------------------------")
        retorno = input("\nPressione 0 e Enter para retornar ao Menu Quina...")
        if retorno == "0":
            return

def verificar_acertos_mega_sena(numeros_sorteados, numeros_escolhidos):
    acertos = set(numeros_sorteados).intersection(set(numeros_escolhidos))
    return acertos

def verificar_acertos_quina(numeros_sorteados, numeros_escolhidos):
    acertos = set(numeros_sorteados).intersection(set(numeros_escolhidos))
    return acertos

def menu_loto_facil():
    while True:
        limpar_tela()
        print("Menu Lotofácil:")
        print("-------------------------------------------------------------------------------")
        print("1 - Realizar Sorteio")
        print("2 - Verificar Números Mais Sorteados")
        print("3 - Voltar ao Menu Principal")
        print("-------------------------------------------------------------------------------")
        escolha_menu_loto_facil = input("Escolha uma opção: ")

        if escolha_menu_loto_facil == "1":
            limpar_tela()
            numeros_escolhidos = escolher_numeros_loto_facil()

            input("\nPressione Enter para realizar o sorteio...")
            limpar_tela()

            print("-------------------------------------------------------------------------------")
            print("Seus números escolhidos:", numeros_escolhidos)

            numeros_sorteados = fazer_sorteio_loto_facil()
            print("Números sorteados:", numeros_sorteados)
            print("-------------------------------------------------------------------------------")

            salvar_numeros_sorteados_loto_facil(numeros_sorteados)

            acertos = verificar_acertos_mega_sena(numeros_sorteados, numeros_escolhidos)

            print("\n\n-------------------------------------------------------------------------------")
            print("Você acertou", len(acertos), "números.")
            print("Números acertados:", acertos)

            numeros_faltando = list(set(numeros_sorteados) - set(acertos))
            print("Números que faltaram para ganhar: ", len(numeros_faltando), numeros_faltando)
            print("-------------------------------------------------------------------------------")

            while True:
                repetir = input("\nDeseja fazer outro sorteio? (S/N): ").strip().lower()
                if repetir == "s":
                    break
                elif repetir == "n":
                    print("Retornando ao Menu Lotofácil...")
                    return
                else:
                    print("Resposta inválida. Digite 'S' para repetir ou 'N' para retornar.")

        elif escolha_menu_loto_facil == "2":
            limpar_tela()
            calcular_estatisticas_loto_facil()
            print("----------------------------------------------------")
            
        elif escolha_menu_loto_facil == "3":
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")

def menu_mega_sena():
    while True:
        limpar_tela()
        print("Menu Mega Sena:")
        print("-------------------------------------------------------------------------------")
        print("1 - Realizar Sorteio")
        print("2 - Verificar Números Mais Sorteados")
        print("3 - Voltar ao Menu Principal")
        print("-------------------------------------------------------------------------------")
        escolha_menu_mega_sena = input("Escolha uma opção: ")

        if escolha_menu_mega_sena == "1":
            limpar_tela()
            numeros_escolhidos = escolher_numeros_mega_sena()

            input("\nPressione Enter para realizar o sorteio...")
            limpar_tela()

            print("-------------------------------------------------------------------------------")
            print("Seus números escolhidos:", numeros_escolhidos)

            numeros_sorteados = fazer_sorteio_mega_sena()
            print("Números sorteados:", numeros_sorteados)
            print("-------------------------------------------------------------------------------")

            salvar_numeros_sorteados_mega_sena(numeros_sorteados)

            acertos = verificar_acertos_mega_sena(numeros_sorteados, numeros_escolhidos)

            print("\n\n-------------------------------------------------------------------------------")
            print("Você acertou", len(acertos), "números.")
            print("Números acertados:", acertos)

            numeros_faltando = list(set(numeros_sorteados) - set(acertos))
            print("Números que faltaram para ganhar: ", len(numeros_faltando), numeros_faltando)
            print("-------------------------------------------------------------------------------")

            while True:
                repetir = input("\nDeseja fazer outro sorteio? (S/N): ").strip().lower()
                if repetir == "s":
                    break
                elif repetir == "n":
                    print("Retornando ao Menu Mega Sena...")
                    return
                else:
                    print("Resposta inválida. Digite 'S' para repetir ou 'N' para retornar.")

        elif escolha_menu_mega_sena == "2":
            limpar_tela()
            calcular_estatisticas_mega_sena()
            print("----------------------------------------------------")
            
        elif escolha_menu_mega_sena == "3":
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")

def menu_quina():
    while True:
        limpar_tela()
        print("Menu Quina:")
        print("-------------------------------------------------------------------------------")
        print("1 - Realizar Sorteio")
        print("2 - Verificar Números Mais Sorteados")
        print("3 - Voltar ao Menu Principal")
        print("-------------------------------------------------------------------------------")
        escolha_menu_quina = input("Escolha uma opção: ")

        if escolha_menu_quina == "1":
            limpar_tela()
            numeros_escolhidos = escolher_numeros_quina()

            input("\nPressione Enter para realizar o sorteio...")
            limpar_tela()

            print("-------------------------------------------------------------------------------")
            print("Seus números escolhidos:", numeros_escolhidos)

            numeros_sorteados = fazer_sorteio_quina()
            print("Números sorteados:", numeros_sorteados)
            print("-------------------------------------------------------------------------------")

            salvar_numeros_sorteados_quina(numeros_sorteados)

            acertos = verificar_acertos_quina(numeros_sorteados, numeros_escolhidos)

            print("\n\n-------------------------------------------------------------------------------")
            print("Você acertou", len(acertos), "números.")
            print("Números acertados:", acertos)

            numeros_faltando = list(set(numeros_sorteados) - set(acertos))
            print("Números que faltaram para ganhar: ", len(numeros_faltando), numeros_faltando)
            print("-------------------------------------------------------------------------------")

            while True:
                repetir = input("\nDeseja fazer outro sorteio? (S/N): ").strip().lower()
                if repetir == "s":
                    break
                elif repetir == "n":
                    print("Retornando ao Menu Quina...")
                    return
                else:
                    print("Resposta inválida. Digite 'S' para repetir ou 'N' para retornar.")

        elif escolha_menu_quina == "2":
            limpar_tela()
            calcular_estatisticas_quina()
            print("----------------------------------------------------")
            
        elif escolha_menu_quina == "3":
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")

def main():
    while True:
        limpar_tela()
        print("Bem-vindo à simulação da Lotofácil, Mega Sena e Quina!")
        print("----------------------------------------------------")
        print("1 - Sorteio da Lotofácil")
        print("2 - Sorteio da Mega Sena")
        print("3 - Sorteio da Quina")
        print("4 - Encerrar o programa")
        print("----------------------------------------------------")
        escolha_menu_principal = input("Escolha uma opção: ")

        if escolha_menu_principal == "1":
            menu_loto_facil()
        elif escolha_menu_principal == "2":
            menu_mega_sena()
        elif escolha_menu_principal == "3":
            menu_quina()
        elif escolha_menu_principal == "4":
            print("Encerrando o programa...")
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")

if __name__ == "__main__":
    main()
