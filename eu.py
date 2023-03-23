EU = []
with open("EU.txt", "r", encoding="utf-8") as file:
    for sor in file:
        EU.append(sor.strip().split(" "))

for i in range(len(EU)):
    EU[i][1] = int(EU[i][1])

min = EU[0][1]
for i in EU:
    if i[1] < min:
        min = i[1]

dbe = 0
dbb = 0
db6 = 0
legrovh = len(EU[0][0])
legrovn = EU[0][0]
for i in EU:
    if i[0][0] == "B":
        dbb = dbb+1
    if len(i[0]) > 6:
        db6 = db6+1
    if len(i[0]) < legrovh:
        legrovh = len(i[0])
        legrovn = i[0]
    if i[1] == min:
        dbe = dbe+1

print("Első csatlakozók száma:", dbe)
print(dbb)
print(db6)
print(legrovh)
print(legrovn)
