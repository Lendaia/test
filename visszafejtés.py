abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
words = []
with open("words.txt", "r") as bemenet:
    for i in bemenet:
        words.append(i.strip())


def kod(titkositando, karakter):
    szamsor = []
    for i in titkositando:
        for j in karakter:
            if i == j:
                szamsor.append(karakter.index(j))
    return szamsor

def egyezik(toredek, melyik, meglevo, szotar = words):
    egyezo = []
    toredek = toredek.strip()

    for i in szotar:
        if i[:len(toredek)] == toredek:
            egyezo.append(i)

    if len(egyezo) != 0:
        meglevo[melyik % 2].append(egyezo)

    return meglevo


def kulcs(uzenet1, uzenet2, szo, keszlet):
    lehetoseg = ""
    fejtett1 = szo
    fejtett2 = ""
    lehetosegkod = []
    uzenet1kod = kod(uzenet1, keszlet)
    uzenet2kod = kod(uzenet2, keszlet)
    szokod = kod(szo, keszlet)
    db = 0
    proba = 0
    valtozo = -1
    szavak = [[], []]
    if len(uzenet1) > len(uzenet2):
        hossz = len(uzenet1)
    else:
        hossz = len(uzenet2)
    aktualis = uzenet1kod
    aktualisb = uzenet2kod

    while len(lehetosegkod) < hossz:
        fejtett = ""

        for i in range(len(szo)):
            szam = aktualis[i] - szokod[i]
            if szam < 0:
                szam = (26 - szokod[i]) + aktualis[i] + 1
            lehetosegkod.append(szam)

        for i in range(len(lehetosegkod)):
            szam = aktualisb[i] - lehetosegkod[i]
            if szam < 0:
                szam = (26 - lehetosegkod[i]) + aktualisb[i] + 1
            fejtett += keszlet[szam]

        if szavak == egyezik(fejtett, db, szavak):
            proba += 1
        else:
            szavak = egyezik(fejtett, db, szavak)
            proba = 0

        szo = szavak[db][valtozo][proba][len(fejtett):] + " "
        szokod = kod(szo, keszlet)

        if db == 0:
            fejtett2 += szavak[db][valtozo][proba] + " "
            aktualis = uzenet2kod[(len(fejtett2) - len(szo)):len(fejtett2)]
            aktualisb = uzenet1kod[len(fejtett1):]
            db = 1

        else:
            fejtett1 += szavak[db][valtozo][proba] + " "
            aktualis = uzenet1kod[(len(fejtett1) - len(szo)):len(fejtett1)]
            aktualisb = uzenet2kod[len(fejtett2):]
            db = 0

        for i in lehetosegkod:
            lehetoseg += abc[i]
        lehetosegkod = []

    return lehetoseg


print(kulcs("ebtobehq nkongrxvjsmb wtmyu", "cvtlsxoagjvuyzttqk ynyxq", "early ", abc))
