#Algoritimo conversor de medidas

print("Esse algoritmo converte as medidas")
print("---------------------")
#Input usuario
Valor = int(input("Qual o valor? "))

#escolha do usuario
print("1- Metros para centímetros")
print("2- Centímetros para metros")
print("3- Quilômetros para metros")
print("4- Metros para quilômetros")
Escolha = int(input("Escolha a opção que deseja: "))

#Estrutura de decisão
if Escolha == 1:
    Resultado = Valor * 100
    print("O resultado é: ", Resultado, "cm")
elif Escolha == 2:
    Resultado = Valor / 100
    print("O resultado é: ", Resultado, "m")
elif Escolha == 3:
    Resultado = Valor * 1000
    print("O resultado é: ", Resultado, "m")
elif Escolha == 4:
    Resultado = Valor / 1000
    print("O resultado é: ", Resultado, "km")
else:
    print("Opção inválida!")


#Fim do algoritmo
print("---------------------")
print("Obrigado por usar o conversor de medidas!")
