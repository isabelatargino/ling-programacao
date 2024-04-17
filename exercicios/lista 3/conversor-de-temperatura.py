def converteTemp(tempC):
    tempF = tempC * (9/5) + 32
    return tempF

tempC = float(input("Digite a temperatura em Celsius:\n"))
tempF = converteTemp(tempC)
print(f"{tempC}C° é equivalente a {tempF}F°")