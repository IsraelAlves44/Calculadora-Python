

def loop():
    print("\n")
    print("***Calculadora*** \n")
    print("Escolha uma opção")
    print(" 1-Adição \n"
          " 2-Subtração \n"
          " 3-Divisão \n"
          " 4-Multiplicação")

    entry = float(input("Digite o número de escolha: "))
    match entry:
        case 1:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            addition = num1 + num2;
            print("A soma de %f + %f é igual a %i " % (num1, num2, addition))
        case 2:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            subtraction = num1 - num2;
            print("A subtração de %f - %f é igual a %i " % (num1, num2, subtraction))

        case 3:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            if (num2 == 0):
                print("A divisão não pode ser executada, nenhum número pode ser dividido por 0.")
                loop();
            else:
                division = num1 / num2;
                print("A divisão de %f e %f é igual a %f " % (num1, num2, division))
        case 4:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            multiplication = num1 * num2;
            print("A soma de %f + %f é igual a %f " % (num1, num2, multiplication))


def finalizar():
    entry2 = int(input("1-Fechar \n"
                       "2-Novamente \n"
                       ": "))
    match entry2:
        case 1:
            print("Finalizado")
        case 2:
            loop();
            finalizar()


loop()
finalizar()