from calculadora.calculadora import (
    somar, subtrair, multiplicar, dividir, potencia, porcentagem
)

def main():
    while True:
        print("\n=== CALCULADORA PYTHON DEVOPS ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potência")
        print("6 - Porcentagem")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Calculadora encerrada.")
            break

        if opcao in {"1", "2", "3", "4", "5", "6"}:
            try:
                a = float(input("Digite o primeiro valor: "))
                b = float(input("Digite o segundo valor: "))

                if opcao == "1":
                    resultado = somar(a, b)
                elif opcao == "2":
                    resultado = subtrair(a, b)
                elif opcao == "3":
                    resultado = multiplicar(a, b)
                elif opcao == "4":
                    resultado = dividir(a, b)
                elif opcao == "5":
                    resultado = potencia(a, b)
                else:
                    resultado = porcentagem(a, b)

                print(f"Resultado: {resultado}")
            except ValueError as erro:
                print(f"Erro: {erro}")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
