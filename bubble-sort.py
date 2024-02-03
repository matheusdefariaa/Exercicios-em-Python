"""
Bumbble Sort

Os valores menores "sobem" gradualmente para o topo do array,
enquanto os valores maiores "descem" para a parte de baixo do array.
"""

numeros = [9,8,7,6,5,4,3,2,1]

print(numeros) # Lista não ordenada

for x in numeros:
    for y in range(len(numeros) - 1): # Loop dentro da lista
        
        if numeros[y] > numeros[(y + 1)]: # Loop de verificação dos números
            var = numeros[y] # Variável auxiliar
            numeros[y] = numeros[y + 1]
            numeros[y + 1] = var


print(numeros) #Lista ordenada