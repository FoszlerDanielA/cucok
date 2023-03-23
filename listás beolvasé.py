lista = []
def csokkeno(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[i]:
                lista[j], lista[i] = lista[i], lista[j]


with open("lista.txt", "r", encoding="utf-8") as file:
    for sor in file:
        felsorolas = sor.split(";")
for i in range(len(felsorolas)):
    print(felsorolas[i])
    felsorolas[i] = int(felsorolas[i])

csokkeno(felsorolas)
print(felsorolas)
print(felsorolas[0])
print(felsorolas[len(felsorolas) - 1])
for i in felsorolas:
    st = st+str(i)+" "
with open("kiiras.txt", "w", encoding="utf-8") as file:
    file.write()