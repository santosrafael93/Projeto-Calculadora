#! /bin/bash
print ("Bem vindo a Calculadora do Rafael!")

while True:
    print ('Você deseja realizar qual operação?')
    print ('1 - Soma')
    print ('2 - Subtração')
    print ('3 - Multiplicação')
    print ('4 - Divisão')
    print ('5 - Potenciação')
    print ('6 - Sair')

    operacao = int(input('Digite o número da operação desejada: '))

    if operacao == 6:
      print("Ok, até a próxima. Tchau!")
      break
    elif operacao < 1 or operacao > 6:
        print ('Digite um número entre 1 e 6')
        continue

    num1 = float(input('Digite o primeiro número: '))
    if operacao != 5:
      num2 = float(input('Digite o segundo número: '))

    if operacao == 1:
        result = num1 + num2
        print (num1, "+" , num2, "é: ", result)

        continua = input("Deseja continuar? (sim/não) ")
        if continua == "sim":
            continue
        else:
            print("Ok, até a próxima. Tchau!")
            break
    elif operacao == 2:
        result = num1 - num2
        print (num1, "-", num2, "é: ", result)

        continua = input("Deseja continuar? (sim/não) ")
        if continua == "sim":
            continue
        else:
            print("Ok, até a próxima. Tchau!")
            break
    elif operacao == 3:
        result = num1 * num2
        print (num1, "*", num2, "é: ", result)

        continua = input("Deseja continuar? (sim/não) ")
        if continua == "sim":
            continue
        else:
            print("Ok, até a próxima. Tchau!")
            break
    elif operacao == 4:
        if num2 == 0:
            print("Erro: Divisão por zero!")
        else:
            result = num1 / num2
            print (num1, "/", num2, "é: ", result)

            continua = input("Deseja continuar? (sim/não) ")
            if continua == "sim":
                continue
            else:
                print("Ok, até a próxima. Tchau!")
                break
    elif operacao == 5:
      num2 = float(input('Digite a potência: '))
      result = num1 ** num2
      print (num1, "elevado a", num2, "é: ", result)

      continua = input("Deseja continuar? (sim/não) ")
      if continua == "sim":
          continue
      else:
          print("Ok, até a próxima. Tchau!")
          break
