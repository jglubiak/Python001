imie = "Bartek"
nazwisko = "Kowalski 'Nowak'"
adres = '''Kwiatowa 28c/1
            Warszawa 09-121'''

print(nazwisko)
print('Czytam ksiazke "Wladca pierscieni"')
print('Czytam \t ksiazke \n \"Wladca pierscieni"')

print("male".upper())
print("DUZE".lower())
print(imie.islower())
print(nazwisko.isupper())

for char in imie:
    print(char)

print(imie[0])
print(imie[0:4])
print(imie.index("a"))
print("Ala" not in "Ala ma kota")

print(" ".join(["Ala", "ma", "kota"]))
print("Ala,ma kota,i,psa".split(","))

