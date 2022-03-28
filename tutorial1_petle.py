#W Pythonie używane są dwa rodzaje pętli: while i for.
print("=== Petla 'for' ===")
pierwsze = [7, 3, 5, 2]
for pomidor in pierwsze:
    print(pomidor)
for x in range(5):
    print(x)
print(pomidor)

for gruszka in range(3,6):
    print(gruszka)
print("=== Petla 'while' ===")
# LOL - uwazaj na while - jesli nie da mu sie warunku,
# wypisuje cyferki w nieskonczonosc - uzyj ^C zeby przerwac
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1
print('=== Instrukcje "break" i "continue" ===')
licznik = 0
while True:
    print (licznik),
    licznik += 1
    if licznik >= 5:
        break
for ble in range(10):
    if ble % 2 == 0:
        continue
    print(ble)
liczby = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for x in liczby:
    if x == 237:
        break
    if x % 2 == 1:
        continue
    print(x)
    
