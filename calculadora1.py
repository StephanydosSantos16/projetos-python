def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    choice = input("Digite o número da operação (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print("Resultado: ", add(num1, num2))
        elif choice == '2':
            print("Resultado: ", subtract(num1, num2))
        elif choice == '3':
            print("Resultado: ", multiply(num1, num2))
        elif choice == '4':
            print("Resultado: ", divide(num1, num2))
    else:
        print("Escolha inválida")

if __name__ == "__main__":
    calculator()
