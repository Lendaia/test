import copy
class uzenet:
    tartalom = ""
    fejtett = ""
    kod = []
    szavak = []
    betu = []
    szint = 0

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


def egyezik(toredek, szotar=words):
    egyezo = []
    toredek = toredek.strip()

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


uzenet1 = uzenet("ebtobehq nkongrxvjsmb wtmyu", kodra("ebtobehq nkongrxvjsmb wtmyu"))
uzenet1.fejtett += "early "
uzenet2 = uzenet("cvtlsxoagjvuyzttqk ynyxq", kodra("cvtlsxoagjvuyzttqk ynyxq"))
lehetoseg = megoldas("", [])

if len(uzenet1.tartalom) > len(uzenet2.tartalom):
    hossz = len(uzenet1.tartalom)
else:
    hossz = len(uzenet2.tartalom)

def kulcs(szo, keszlet, proba):
    db = 0
    aktualis = uzenet1.kod
    aktualisb = uzenet2.kod
    flag = True
    fejtett = ""
    kulcs_priv(szo, keszlet, proba, aktualis, aktualisb, db, flag, fejtett)

def kulcs_priv(szo, keszlet, proba, aktualis, aktualisb, db, flag, fejtett):
    szokod = kodra(szo)

    while len(lehetoseg.kod) < hossz:
        if flag:
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
                flag = True
                if db == 0:
                    szo = uzenet2.szavak[-1][proba][len(fejtett):] + " "
                    szokod = kodra(szo)
                    aktualis = uzenet1.kod[(len(uzenet1.fejtett) - len(szo)):len(uzenet1.fejtett)]
                    aktualisb = uzenet2.kod[len(uzenet2.fejtett):]
                    uzenet2.szint -= 1

                else:
                    szo = uzenet1.szavak[-1][proba][len(fejtett):] + " "
                    szokod = kodra(szo)
                    aktualis = uzenet2.kod[(len(uzenet2.fejtett) - len(szo)):len(uzenet2.fejtett)]
                    aktualisb = uzenet1.kod[len(uzenet1.fejtett):]
                    uzenet1.szint -= 1

            kulcs_priv(szo, keszlet, proba, aktualis, aktualisb, db, flag, fejtett)
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
                        if counter == len(uzenet2.betu):
                            uzenet2.fejtett = uzenet2.fejtett[:i+1]
                            break

            if len(uzenet1.fejtett) > len(uzenet2.fejtett):
                lehetoseg.tartalom = lehetoseg.tartalom[:len(uzenet1.fejtett)]
            else:
                lehetoseg.tartalom = lehetoseg.tartalom[:len(uzenet2.fejtett)]

        else:
            return

    return lehetoseg.tartalom


print(kulcs("early ", abc, 0))
