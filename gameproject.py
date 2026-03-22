# RPG битва - мой первый проект
import random
import sys
sys.stdout.reconfigure(encoding='utf-8') # для поддержки русских символов в консоли

character1 = { # персонаж 1
    "Здоровье": 100,
    "Имя": "Hero",
    "Уровень": random.randint(10, 20),
    "Урон": "10-15",
    "Инвентарь": ["кинжал", "щит", "зелье"]
}

print(character1["Имя"])
print(f"Здоровье: {character1['Здоровье']}") 
print(f"Урон: {character1['Урон']}")
print(f"Уровень: {character1['Уровень']}")
print(f"Инвентарь: {character1['Инвентарь'][1]}")

character2 = { # персонаж 2
    "Здоровье": 80,
    "Имя": "Enemy",
    "Уровень": random.randint(10, 20),
    "Урон": "15-20",
    "Инвентарь": ["меч", "щит", "зелье"]
}

print(character2["Имя"])
print(f"Здоровье: {character2['Здоровье']}") 
print(f"Урон: {character2['Урон']}")
print(f"Уровень: {character2['Уровень']}")
print(f"Инвентарь: {character2['Инвентарь'][1]}")

def подсчитать_урон(мин, макс):
    return(random.randint(мин, макс))
def использовать_зелье(персонаж):
    if персонаж["Здоровье"] < 30 and "зелье" in персонаж["Инвентарь"]:
        персонаж["Здоровье"] += 20
        персонаж["Инвентарь"].remove("зелье")
        print(f"{персонаж['Имя']} использует зелье! Здоровье восстановлено до: {персонаж['Здоровье']}")

while character1["Здоровье"] > 0 and character2["Здоровье"] > 0:

    character1["Урон"] = подсчитать_урон(10, 15)
    character2["Урон"] = подсчитать_урон(15, 20)

    character2["Здоровье"] -= character1["Урон"]
    print(f"{character1['Имя']} атакует! {character2['Имя']} Здоровье: {character2['Здоровье']}")

    if character2["Здоровье"] <= 0:
        print(f"{character2['Имя']} побежден!")
        break


    character1["Здоровье"] -= character2["Урон"]
    print(f"{character2['Имя']} атакует! {character1['Имя']} Здоровье: {character1['Здоровье']}")

    if character1["Здоровье"] <= 0:
        print(f"{character1['Имя']} побежден!")
        break
    использовать_зелье(character1)
    использовать_зелье(character2)

print(f"Здоровье {character1['Имя']}: {character1['Здоровье']}")
print(f"Здоровье {character2['Имя']}: {character2['Здоровье']}")
