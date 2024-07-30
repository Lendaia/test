abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uzenet = "helloworld"
kulcs = "abcdefgijkl"


def kod(titkositando, karakter):
    szamsor = []
    for i in titkositando:
        for j in karakter:
            if i == j:
                szamsor.append(karakter.index(j))
    return szamsor


uzenetkod = kod(uzenet, abc)
kulcskod = kod(kulcs, abc)
titkositott = ""
for i in range(len(uzenet)):
    szam = uzenetkod[i] + kulcskod[i]
    if szam > 26:
        szam = szam % 27
    titkositott += abc[szam]

print(titkositott)
