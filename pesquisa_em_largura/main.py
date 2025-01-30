from collections import deque

def comeca_com_m(pessoa):
    if pessoa[0] == 'N':
        return True
    return False

pessoas = {}

pessoas["Matheus"] = ["Julia","Carcos","Francisco"]
pessoas["Julia"] = ["Carlos","Matheus"]
pessoas["Marcos"] = ["Matheus"]
pessoas["Francisco"] = ["Carlos","Matheus"]
pessoas["Carlos"] = ["Julia","Francisco","Nada"]
pessoas["Carcos"] = ["Julia","Francisco"]



def pesquisa(nome,p):
    fila = deque()
    fila += p[nome]
    verificadas = []

    while fila:
        p1 = fila.popleft()

        if not p1 in verificadas:
            if comeca_com_m(p1):
                print(f"{p1}")
                return True
            
            verificadas.append(p1)
            fila += p[p1]

    print("Nenhum usuario encontrado")
    return False

pesquisa("Matheus",pessoas)
