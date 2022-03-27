x = 2
print(x == 2)
print(x != 2)
print(x == 3)
print(x < 3)
print("==== operatory logiczne =====")
imie = "Jan"
wiek = 23
if imie == "Jan" and wiek == 23:
    print("Nazywasz sie " + imie + " i masz " + str(wiek) + " lata.")
if imie == "Jan" or imie == "Robert":
    print("Nazywasz sie Jan lub Robert.")
print("=== operator 'in' ===")
imie = "Czarek"
if imie in ["Jan", "Robert"]:
    print("Nazywasz sie Jan lub Robert.")
else:
    print("Nie nazywasz sie ani Jan, ani Robert.")
if x == 2:
    print("x wynosi dwa!")
else:
    print("x jest rozne od dwoch.")
print("==== operator 'is' ====")
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)
tablica = [1, 2, 3]
tablica2 = ['a', 'b', tablica]
print(tablica == tablica2[2])
print(tablica is tablica2[2])
tablica.append(4)
print(tablica2[2])
tablica2[2] = tablica + [4]
print(tablica is tablica2[2])
print("tablica2 = ", tablica2[2])
print("tablica = ", tablica)
print("=== operator 'not' ===")
print(not False)
print((not False) == (False))
print("=== cwiczenie ===")
# Zmien ponizszy kod
liczba = 16
druga_liczba = 0
pierwsza_tablica = [1,4,5]
druga_tablica = [1,2]

if liczba > 15:
    print ("1")

if pierwsza_tablica:
    print ("2")

if len(druga_tablica) == 2:
    print ("3")

if len(pierwsza_tablica) + len(druga_tablica) == 5:
    print ("4")

if pierwsza_tablica and pierwsza_tablica[0] == 1:
    print ("5")

if not druga_liczba:
    print ("6")
