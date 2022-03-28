napis = "Odwazny rudy lis przeskoczyl nad spiacym wilczurem"
slowa = napis.split()
dlugosc_slow = []
for slowo in slowa:
    if slowo != "nad":
        dlugosc_slow.append(len(slowo))
print (dlugosc_slow)
#to teraz lista skladana:
napis = "Odwazny rudy lis przeskoczyl nad spiacym wilczurem"
slowa = napis.split()
dlugosc_slow = [len(slowo) for slowo in slowa if slowo != "nad"]
print(dlugosc_slow)

liczby = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

nowa = [int(calkowita) for calkowita in liczby if calkowita > 0]

print (nowa)
