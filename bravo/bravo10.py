lista = [100, 200, 300, 400, 500, 600, 700]
despues500 = lista.index(500)
lista.insert(despues500 + 1, "bravo")
lista.insert(despues500 + 2, "qux")
lista.insert(despues500 + 3, "thud")
print(lista)