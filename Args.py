def rzeczy(pierwsza_rzecz, *args):
    for arg in args:
        print(arg)
    print(pierwsza_rzecz)


rzeczy("Cos", "tak", "nie", True, False, 22)
