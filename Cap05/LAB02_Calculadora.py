#Calculadora Soma/Multiplicação/Divisão 

#Calculadora

#Qual cálculo será realizado ? 

# Soma (
 #   digite o primeiro número;
 #  operação de soma; 
 # digite o segundo número; 
#      )

# Subtração (
 #   digite o primeiro número;
 #  operação de subtração; 
 # digite o segundo número; 
#      )

# Multiplicação (
 #   digite o primeiro número;
 #  operação de Multiplicação; 
 # digite o segundo número; 
#      )

# Divisão (
 #   digite o primeiro número;
 #  operação de Divisão; 
 # digite o segundo número; 
#      )

print ("\n ******* CALCULADORA *******\n")

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Divisão por zero."

while True:
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Saindo...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", soma(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado:", divisao(num1, num2))
    else:
        print("Opção inválida. Tente novamente.")