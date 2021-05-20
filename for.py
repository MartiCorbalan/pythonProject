a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "hola hoy estoy aprendiendo python"

vocales = ["a", "e", "i", "o", "u"]

vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        #print("he ecnotrado una {}".format(letra))
        vocales_encontradas += 1

print(frase)
print("Vocales encontradas: {}".format(vocales_encontradas))
