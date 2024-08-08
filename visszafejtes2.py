import copy
class uzenet:
    tartalom = ""
    fejtett = ""
    kod = []
    szavak = []

    def __init__(self, tartalom, kod):
        self.tartalom = tartalom
        self.kod = kod


class megoldas:
    tartalom = ""
    kod = []

    def __init__(self, tartalom, kod):
        self.tartalom = tartalom
        self.kod = kod


abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
words = []
with open("words.txt", "r") as bemenet:
    for i in bemenet:
        words.append(i.strip())


def egyezik(toredek, meglevo, szotar = words):
    egyezo = []
    toredek = toredek.strip()

    for i in szotar:
        if i[:len(toredek)] == toredek:
            egyezo.append(i)

    if len(egyezo) != 0:
        return egyezo

    return meglevo


def kodra(titkositando, karakter = abc):
    szamsor = []
    for i in titkositando:
        for j in karakter:
            if i == j:
                szamsor.append(karakter.index(j))
    return szamsor


uzenet1 = uzenet("ebtobehq nkongrxvjsmb wtmyu", kodra("ebtobehq nkongrxvjsmb wtmyu"))
uzenet2 = uzenet("cvtlsxoagjvuyzttqk ynyxq", kodra("cvtlsxoagjvuyzttqk ynyxq"))
lehetoseg = megoldas("", [])
db = 0
aktualis = uzenet1.kod
aktualisb = uzenet2.kod


if len(uzenet1.tartalom) > len(uzenet2.tartalom):
    hossz = len(uzenet1.tartalom)
else:
    hossz = len(uzenet2.tartalom)


def kulcs(szo, keszlet, proba):
    global aktualis, aktualisb, db
    szokod = kodra(szo)

    while len(lehetoseg.kod) < hossz:
        fejtett = ""

        for i in range(len(szo)):
            szam = aktualis[i] - szokod[i]
            if szam < 0:
                szam = (26 - szokod[i]) + aktualis[i] + 1
            lehetoseg.kod.append(szam)

        for i in range(len(lehetoseg.kod)):
            szam = aktualisb[i] - lehetoseg.kod[i]
            if szam < 0:
                szam = (26 - lehetoseg.kod[i]) + aktualisb[i] + 1
            fejtett += keszlet[szam]

        if uzenet1.szavak == egyezik(fejtett, copy.deepcopy(uzenet1.szavak)):
            kulcs(szo, keszlet, ++proba)

        aktualisb.szavak.append(egyezik(fejtett, aktualisb.szavak))
        szo = aktualisb.szavak[-1][proba][len(fejtett):] + " "
        szokod = kodra(szo)

        if db == 0:
            uzenet2.fejtett += uzenet2.szavak[0][proba] + " "
            aktualis = uzenet2.kod[(len(uzenet2.fejtett) - len(szo)):len(uzenet2.fejtett)]
            aktualisb = uzenet1.kod[len(uzenet1.fejtett):]
            db = 1
        else:
            uzenet1.fejtett += uzenet1.szavak[-1][proba] + " "
            aktualis = uzenet1.kod[(len(uzenet1.fejtett) - len(szo)):len(uzenet1.fejtett)]
            aktualisb = uzenet2.kod[len(uzenet2.fejtett):]
            db = 0

        for i in lehetoseg.kod:
            lehetoseg.tartalom += abc[i]
        lehetoseg.kod = []

    return lehetoseg.tartalom


kulcs("early ", abc, 0)
