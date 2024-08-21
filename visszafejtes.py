import copy
class uzenet:
    tartalom = ""
    fejtett = ""
    kod = []
    szavak = []
    betu = []
    szint = 0

    def __init__(self, tartalom, kod, szavak, betu):
        self.tartalom = tartalom
        self.kod = kod
        self.szavak = szavak
        self.betu = betu

class megoldas:
    tartalom = ""
    kod = []
    siker = True

    def __init__(self, tartalom, kod):
        self.tartalom = tartalom
        self.kod = kod


abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
words = []
with open("words.txt", "r") as bemenet:
    for i in bemenet:
        words.append(i.strip())


def egyezik(toredek, szotar=words):
    egyezo = []

    for i in szotar:
        if i[:len(toredek)] == toredek:
            egyezo.append(i)

    if len(egyezo) != 0:
        return egyezo

    return None


def kodra(titkositando, karakter=abc):
    szamsor = []
    for i in titkositando:
        for j in karakter:
            if i == j:
                szamsor.append(karakter.index(j))
    return szamsor


uzenet1 = uzenet("bjicgfksvk", kodra("bjicgfksvk"), [["big "]], ["big "])
uzenet1.fejtett += "big "
uzenet2 = uzenet("acqyielvwepm", kodra("acqyielvwepm"), [], [])
lehetoseg = megoldas("", [])


if len(uzenet1.tartalom) > len(uzenet2.tartalom):
    hossz = uzenet1.tartalom
    rovidebb = uzenet2.tartalom
else:
    hossz = uzenet2.tartalom
    rovidebb = uzenet1.tartalom

def kulcs(szo, keszlet):
    db = 0
    aktualis = uzenet1.kod
    aktualisb = uzenet2.kod
    flag = True
    fejtett = ""
    proba = 0
    return kulcs_priv(szo, keszlet, proba, aktualis, aktualisb, db, flag, fejtett)

def kulcs_priv(szo, keszlet, proba, aktualis, aktualisb, db, flag, fejtett):
    szokod = kodra(szo)

    while lehetoseg.siker:
        if flag:
            fejtett = ""
            if len(lehetoseg.tartalom) != len(rovidebb):

                for i in range(len(szo)):
                    szam = aktualis[i] - szokod[i]
                    if szam < 0:
                        szam = (26 - szokod[i]) + aktualis[i] + 1
                    lehetoseg.kod.append(szam)
                    if i == len(aktualis)-1:
                        break

            for i in range(len(lehetoseg.kod)):
                szam = aktualisb[i] - lehetoseg.kod[i]
                if szam < 0:
                    szam = (26 - lehetoseg.kod[i]) + aktualisb[i] + 1
                fejtett += keszlet[szam]

            for i in lehetoseg.kod:
                lehetoseg.tartalom += abc[i]
            lehetoseg.kod = []
        else:
            proba += 1

        if egyezik(fejtett):
            if flag:
                if db == 0:
                    uzenet2.betu.append(fejtett)
                    uzenet2.szavak.append(egyezik(fejtett))
                    szo = uzenet2.szavak[-1][proba][len(fejtett):] + " "
                    szokod = kodra(szo)

                    uzenet2.fejtett += uzenet2.szavak[-1][proba] + " "
                    aktualis = uzenet2.kod[(len(uzenet2.fejtett) - len(szo)):len(uzenet2.fejtett)]
                    aktualisb = uzenet1.kod[len(uzenet1.fejtett):]
                    uzenet2.szint += 1
                    db = 1

                else:
                    uzenet1.betu.append(fejtett)
                    uzenet1.szavak.append(egyezik(fejtett))
                    szo = uzenet1.szavak[-1][proba][len(fejtett):] + " "
                    szokod = kodra(szo)

                    uzenet1.fejtett += uzenet1.szavak[-1][proba] + " "
                    aktualis = uzenet1.kod[(len(uzenet1.fejtett) - len(szo)):len(uzenet1.fejtett)]
                    aktualisb = uzenet2.kod[len(uzenet2.fejtett):]
                    uzenet1.szint += 1
                    db = 0

            else:
                if db == 0:
                    uzenet2.fejtett += uzenet2.szavak[-1][proba] + " "
                    aktualis = uzenet2.kod[(len(uzenet2.fejtett) - len(szo)):len(uzenet2.fejtett)]
                    aktualisb = uzenet1.kod[len(uzenet1.fejtett):]
                    uzenet2.szint += 1
                    db = 1

                else:
                    uzenet1.fejtett += uzenet1.szavak[-1][proba] + " "
                    aktualis = uzenet1.kod[(len(uzenet1.fejtett) - len(szo)):len(uzenet1.fejtett)]
                    aktualisb = uzenet2.kod[len(uzenet2.fejtett):]
                    uzenet1.szint += 1
                    db = 0
            if len(hossz) == len(uzenet1.fejtett) or len(hossz) == len(uzenet2.fejtett):
                for i in range(len(szo)):
                    szam = aktualis[i] - szokod[i]
                    if szam < 0:
                        szam = (26 - szokod[i]) + aktualis[i] + 1
                    lehetoseg.kod.append(szam)
                    if i == len(aktualis)-1:
                        break

                for i in lehetoseg.kod:
                    lehetoseg.tartalom += abc[i]
                lehetoseg.kod = []
                lehetoseg.siker = False
                return lehetoseg.tartalom

            kulcs_priv(szo, keszlet, 0, aktualis, aktualisb, db, True, fejtett)
            if not lehetoseg.siker:
                return lehetoseg.tartalom

            flag = False
            if db == 0:
                counter = 0
                for i in range(len(uzenet1.fejtett[:-1])):
                    if uzenet1.fejtett[i] == " ":
                        counter += 1
                        if counter == len(uzenet1.betu):
                            uzenet1.fejtett = uzenet1.fejtett[:i]
                            break
            else:
                counter = 0
                for i in range(len(uzenet2.fejtett[:-1])):
                    if uzenet2.fejtett[i] == " ":
                        counter += 1
                        if counter == len(uzenet2.betu)-1:
                            uzenet2.fejtett = uzenet2.fejtett[:i+1]
                            break

            if len(uzenet1.fejtett) > len(uzenet2.fejtett):
                lehetoseg.tartalom = lehetoseg.tartalom[:len(uzenet1.fejtett)]
            else:
                lehetoseg.tartalom = lehetoseg.tartalom[:len(uzenet2.fejtett)]

        else:
            return

    return lehetoseg.tartalom


print(kulcs("big ", abc))
