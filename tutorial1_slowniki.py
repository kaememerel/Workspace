czapki = {}
czapki["zimowa"] = "biala"
czapki["jesienna"] = "czerwona"
czapki["wiosenna"] = "niebieska"
print(czapki)
for pora, kolor in czapki.items():
    print("Moja %s czapka jest %s." % (pora, kolor))
#albo tak - to samo
for pora in czapki:
    print("Moja %s czapka jest %s." % (pora, czapki[pora]))
del czapki["wiosenna"]
print(czapki)
czapki.pop("jesienna")
print(czapki)
