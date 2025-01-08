# Soma Recursiva

def soma(lista: list[int]) -> int:
    if lista == []:
        return 0

    return lista[0] + soma(lista[1:])
    

print(soma([1,2,3,4,5,6]))