temperatura = input("").split()
valor = float(temperatura[0])
escala = temperatura[1].upper()

if escala == "C":
    celsius = valor
    fahrenheit = ((celsius * 9/5) + 32)
    kelvin = celsius + 273.15
    print(f"Temperatura em Celsius: {celsius:.2f} °C Temperatura em Fahrenheit: {fahrenheit:.2f} °F Temperatura em Kelvin: {kelvin:.2f} K")
elif escala == "F":
    fahrenheit = valor
    celsius = ((fahrenheit - 32) * 5/9)
    kelvin = (((fahrenheit - 32) * 5/9) + 273.15)
    print(f"Temperatura em Celsius: {celsius:.2f} °C Temperatura em Fahrenheit: {fahrenheit:.2f} °F Temperatura em Kelvin: {kelvin:.2f} K")
elif escala == "K":
    kelvin = valor
    celsius = kelvin - 273.15
    fahrenheit = ( ((kelvin - 273.15) * 9/5) + 32 )
    print(f"Temperatura em Celsius: {celsius:.2f} °C Temperatura em Fahrenheit: {fahrenheit:.2f} °F Temperatura em Kelvin: {kelvin:.2f} K")
else:
    print("Erro!")