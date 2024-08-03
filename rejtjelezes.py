import random

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
uzenet = "curiosity killed the cat"

# uzenet = input("üzenet: ")

kulcs = "abcdefgijkl"

# Amennyiben random generált kulcsot szeretnénk generálni, ez az egyszerű algoritmus használható
def randomkulcs(hossz, keszlet):
    ujkulcs = ""
    for i in range(len(hossz) + random.randint(0, 50)):
        ujkulcs += random.choice(keszlet)

    return ujkulcs


# kulcs = randomkulcs(uzenet, abc)


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
