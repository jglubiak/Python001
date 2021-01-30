def dziennik(klasa,**kwargs):
    print("Klasa " + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
        print(kwargs.get(nazwisko))

dziennik("3c", Kowalski=1, Nowak=2, Wisniewski=3)