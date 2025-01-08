def quick_sort(lista):
    if len(lista) < 2:
        return lista
    
    pivo = lista[0]

    menores = [x for x in lista[1:] if x < lista[0]]
    maiores = [x for x in lista[1:] if x > lista[0]]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

print(quick_sort([4,2,3,6,5,8,7,1]))