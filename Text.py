with open( "poen.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)

print("Чи бажаєте добавити автора?Так або ні")
Choose = input()
if( Choose == "Так"):
    Autor=input()
else:
    exit()

with open( "poen.txt", "a", encoding="utf-8") as file:
    file.write("\n"+Autor)
with open( "poen.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)

print("Чи бажаєте добавити цитату?Так або ні")
Autor=input()

with open( "poen.txt", "a", encoding="utf-8") as file:
    file.write("\n"+Autor)
with open( "poen.txt", "r", encoding="utf-8") as file:
    data = file.read()
print(data)

