import copy

EU = []
EU2 = []
dic = {}
with open("EU.txt", "r", encoding="utf-8") as file:
    for sor in file:
        dic["Ország név"] = sor.strip().split(" ")[0]
        dic["Belépési év"] = int(sor.strip().split(" ")[1])
        EU2.append(copy.deepcopy(dic))
        EU.append(sor.strip().split(" "))

print(EU)
print(EU2)
print(dic)
