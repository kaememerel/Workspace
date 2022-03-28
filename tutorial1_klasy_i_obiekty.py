class MojaKlasa:
    zmienna = "blah"
    def funkcja(self):
        print("To jest wiadomosc wewnatrz klasy.")
class MojaKlasa:
    zmienna = "blah"
mojobiekt = MojaKlasa()
mojobiekt.zmienna = "ple"
print(mojobiekt.zmienna)
#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu

# Ponizej umiesc swoj kod
Auto1 = Pojazd()
Auto1.nazwa = "Ferrari"
Auto1.rodzaj = "kabriolet"
Auto1.kolor = "czerwony"
Auto1.wartosc = 60000
Auto2 = Pojazd()
Auto2.nazwa = "Ikarus"
Auto2.rodzaj = "autobus"
Auto2.kolor = "niebieski"
Auto2.wartosc = 10000
# sprawdzenie kodu
print (Auto1.opis())
print (Auto2.opis())
class Kubek:
    rozmiar = "duzy"
    kolor = "zolty"
    skad = "od cioci"
    do = "kawy"
    def jaki(self):
        jaki_kubek = "Ten %s %s kubek jest %s i uzywam go do %s" % (self.rozmiar, self.kolor, self.skad, self.do)
        return jaki_kubek
Kubek1 = Kubek()
Kubek1.rozmiar = "sredni"
Kubek1.kolor = "niebieski"
Kubek1.skad = "od taty"
Kubek1.do = "herbaty"

Kubek2 = Kubek()
Kubek2.rozmiar = "maly"
Kubek2.kolor = "zielony"
Kubek2.skad = "znad morza"
Kubek2.do = "espresso"

print(Kubek1.jaki())
print(Kubek2.jaki())
