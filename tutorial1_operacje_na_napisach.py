# Zeby wydrukowac cudzyslow w cudzyslowie trzeba poprzedzic go backslashami
print ("Nigdy nie czytalem \"Potopu\".")
print ('Nigdy nie czytalem \'Potopu\'.')
print("====cwiczenia====")
napis = "AAA BBB ..."
print (len(napis))
napis = "abcdeabcde"
print(napis.index("a"))
print(napis.index("d"))
napis = "abrakadabra"
print(napis.count("a"))
print(napis.count("ab"))
print(napis[2])
print(napis[3:7])
print(napis[0:4])
print(napis[:4])
print(napis[::])
print(napis[4:len(napis)])
print(napis[4:])
print(napis[-1])
print(napis[-5:-3])
print(napis[-4:])
print(napis[:-2])
napis = "Witaj Kasiu"
print(napis.upper())
print(napis.lower())
print(napis.startswith("Witaj"))
print(napis.startswith("Czesc"))
print(napis.endswith("Kasiu"))
print(napis.endswith("swiecie"))
napis = "Ala ma kota."
tablica_slow = napis.split(" ")
print(tablica_slow)
