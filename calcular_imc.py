# Calculadora de IMC

# Fórmula: IMC = peso / altura^2

peso = float(input("Insira o seu peso:"))
altura = float(input("Insira o sua altura:"))

imc = peso / (altura**2)

if imc < 18.5:
    print("Você está Abaixo do peso")
elif imc >= 18.5 <= 24.9:
    print("Você está com Peso normal")
elif imc >= 25.0 <= 29.9:
    print("Você está com Sobrepeso")
elif imc >= 30.0 <= 34.9:
    print("Você está com Obesidade Grau I")
elif imc >= 35.0 <= 39.9:
    print("Você está com Obesidade Grau II (severa)")
elif imc >= 40.0:
    print("Você está com Obesidade Grau III (morbida)")