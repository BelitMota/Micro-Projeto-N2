# Calculadora de IMC

# Fórmula: IMC = peso / altura^2

peso = float(input("Insira o seu peso: "))
altura = float(input("Insira o sua altura: "))

imc = round (peso / (altura**2))

if imc < 18.5:
    print(f"Você está Abaixo do peso. IMC: {imc} ")
elif imc >= 18.5 <= 24.9:
    print(f"Você está com Peso normal. IMC: {imc}")
elif imc >= 25.0 <= 29.9:
    print(f"Você está com Sobrepeso. IMC: {imc}")
elif imc >= 30.0 <= 34.9:
    print(f"Você está com Obesidade Grau I. IMC: {imc}")
elif imc >= 35.0 <= 39.9:
    print(f"Você está com Obesidade Grau II (severa). IMC: {imc}")
elif imc >= 40.0:
    print(f"Você está com Obesidade Grau III (morbida). IMC: {imc}")