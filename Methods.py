def pogoda():
    print("Jest slonecznie")
    print("Temperatura 20 stopni")
    print("Nie pada deszcz")

pogoda()

def przedstaw_sie(imie, wiek):
    print("Czesc mam na imię " + imie)
    print("Mam " + wiek)


przedstaw_sie("Jedrzej", "11 lat")
przedstaw_sie("Tomek", "33 lata")
przedstaw_sie(str(3333), "tak")


def dodawanie(pierwsza, druga):
    wynik = pierwsza + druga
    return wynik


print(dodawanie(2,2))

print(dodawanie(dodawanie(1, 2), dodawanie(3, 4)))

def odejmowanie(a,b):
    print(a-b)


roznica = odejmowanie(3, 4)
print(roznica)