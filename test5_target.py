def inverter_texto(texto):
    frases = texto[::-1]
    return frases


frase = input("Digite qualquer texto para inveter-lo: ")

print(inverter_texto(frase))
