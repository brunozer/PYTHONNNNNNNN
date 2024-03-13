# inp =  int(input("digite um numero: "))

# if inp > 10:
#     print("o", inp, "é maior que 10")

# if inp <10:
#     print("o ", inp, "é menor que 10")

# if inp == 10:
#     print("o numero é 10") 



# horasTrabalhadas =  int(input("digite a quantidade de horas trabalhadas: "))


# valorPagoPorHora =  int(input("digite o valor por hora: "))

# valorBruto = valorPagoPorHora * horasTrabalhadas

# salarioLiquido= 0

# if valorBruto <1000:
#     salarioLiquido= valorBruto - (valorBruto * 0.05)
#     print("o salario liquido é:",salarioLiquido)
    
# elif valorBruto >=1000 and valorBruto <=2000:
#       salarioLiquido= valorBruto - (valorBruto * 0.10)
#       print("o salario liquido: ",salarioLiquido)
# else:
#       salarioLiquido= valorBruto - (valorBruto * 0.15)
#       print("salario liquido",salarioLiquido)


nome= input("qual é o seu nome: ")
peso = float(input("digite seu peso: "))
altura = float(input("digite seu altura: "))



imc = peso / altura **2

print(nome,",", "seu imc é", imc)

if imc <=18.5:
    print("abaixo do peso")
    

elif imc >=18.5 and imc<=24.9:
    print("peso normal")
    
elif imc >=25 and imc<=29.9:
    print("levemente acima do peso")


elif imc >=30 and imc<=34.9:
    print("obesidade I")

elif imc >=35 and imc<=39.9:
    print("Obesidade II -> (severa)")
    
else:
    print("Obesidade III (mórbida)")




