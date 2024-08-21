1 Változók
══════════

  • `uzenet.fejtett': az üzenet megfejtett formátuma
  • `uzenet.tartalom': üzenet kódolt formátuma
  • `uzenet.kod': tömb, melyben a kódolt üzenet szerepel betű szerinti
    indexekre bontva. Pl 'abc' -> [0, 1, 2]
  • `uzenet.betu': adott üzenetben fixen szereplő szótöredékek
  • `uzenet.szavak': az adott üzenetben összes lehetségesen szereplő
    szó. Pl ha a fejtett szótöredék 'k', akkor ez ['keep', 'kill',
    'killed', …]
  • `uzenet.szint': rekurzió szerint az üzenet melyik rétegben (stack
    frame-ben) tart
  • `megoldas.tartalom': visszafejtett kulcs
  • `megoldas.kod': a kulcs indexekre bontott változata
  • `abc': angol abc
  • `words': angol szólista


2 Metódusok:
════════════

2.1 Egyezik():
──────────────

  • `egyezo': töredékkel egyező szavak listája
  • `toredek': a visszafejtett szótöredék


2.2 Kodra():
────────────

  • `titkositando': szöveges érték, melyet át akarunk váltani index
    formátumba
  • `szamsor': index formátum
  • `uzenet1': első üzenet objektum
  • `uzenet2': második üzenet objektum
  • `lehetoseg': kulcs
  • `hossz': hosszabbik üzenet hossza


2.3 Kulcs():
────────────

  • `db': segédérték, mely számontartja hogy melyik üzenetet fejtjük
    éppen
  • `aktualis': az aktuálisan használt üzenet index értékei
  • `aktualisb': az aktuálisan fejtett üzenet index értékei
  • `flag': vizsgálja, hogy az adott frame-re sikeres lefutás miatt,
    vagy idejekorai `return'-ből léptünk-e át
  • `fejtett': aktuálisan fejtett szótöredék

  A függvény két részből áll. A meghívás a publikus `kulcs()'-on
  keresztül történik, ahol az egyes változók deklarálása történik,
  illetve a `kulcs_priv()' függvényt innen hívjuk meg.  Erre azért van
  szükség, hogy a rekurzió során a call stack-ben minden frame
  megtarthassa a változóinak az értékét, így azok értékének
  visszaállítása egy bizonyos futásidejű pontra egyszerű legyen.


2.4 Kulcs_priv():
─────────────────

  • `szo': kitalált szó
  • `szokod': szó indexekre bontott értéke
  • `keszlet': angol abc
  • `proba': kitalált szavak közül az aktuálisan próbált index szerinti
    értéke
  • `szam': cikluson belül aktuálisan megfejtett betű index formátumban
  • `counter': space-eket számolja, ezzel segítve a tévesen
    visszafejtett szavak törlését


3 Deklaráció, segéd függvenyek
══════════════════════════════

  Az osztályok létrehozása után a szótár fájlt beolvassuk, tartalmát
  eltároljuk. Az `egyezik()' függvény a szótár összes elemével
  összehasonlítja a szótöredék, figyelmen kívül hagyva minden betűt, ami
  a töredék hosszán túlnyúlik. Az így megkapott szavakat az `egyezo'
  tömbbe menti el. Amennyiben nem talált új szót (mert a szótöredékünk
  értelmetlen szöveg), a függvény semmit sem ad vissza.

  A `kodra()' függvény a titkosítandó szöveget betűről-betűre
  átvizsgálja, és egy tömbben visszaadja a betűk abc szerinti indexét.


3.1 `kulcs()' függvény
──────────────────────

  A privát részben (`kulcs_priv()') a vizsgált szó, vagy szótöredék
  indexekre való bontása után egy `while' ciklusban meghatározzuk, hogy
  a függvény addig menjen, amíg el nem éri minimum a kívánt hosszt
  (`hossz').  A flag változó - amennyiben meghívás útján kerültünk a
  függvénybe - engedi lefutni a kettő `for' ciklust. Az első a kódolt
  üzenetből és az ismert szóból számolja ki a lehetséges kulcs soron
  következő karakteteit. A második ciklus az így meghatározott
  kulcsrészletből kiszámítja a másik üzenet soron következő szakaszának
  betűjeit.  Végül, a kulcs kódos formátuma nullázódik, helyette
  karakteres formátumba tároljuk.  A kiszámolt szótöredékből
  megpróbáljuk kikövetkeztetni, hogy milyen angol szóra egészíthető
  ki. Amennyiben az `egyezik' függvény talál ilyen szót, az első ilyen
  találattal elindul. A `szo' változó a kitalát szó azon karakterei
  lesznek, amelyek túllógnak a biztosan kitalált részleten.  Ha meghívás
  útján léptünk a függvénybe, a `db' változó segítségével hozzáadjuk a
  megfelelő `uzenet' objektumhoz a megfejtett szót egy szóközzel a
  végén, a `betu', a `szavak' és a `fejtett' értékekhez a megfelelő
  módon. Így az előző kettő változó mátrixot alkotnak.  A két üzenet
  kódját levágjuk ott, ahol már megfejtettük, illetve megcseréljük az
  értékeiket. A `szint'-et és a `db'-ot nyomonkövetjük.  Ezen a ponton a
  függvény meghívja önmagát, így a következő frame-ben a soron következő
  szóval folytatja a megfejtést. Amennyiben a 96. sor `if'-je `None'
  értéket ad vissza, akkor `return'-be futunk. Ekkor a `flag' `False'
  lesz, és - szintén a `db' változó alapján eldöntve - a megfelelő
  üzenetből a szóközök számát összeveti a kitalált szavakéval, és
  kitörli a feleslegesen belekerült változatokat, és ezek alapján a
  kulcs felesleges karakteteit is.  Ezúttal a `while' eleje kimarad,
  helyette a `proba' változóhoz adunk egyet. Így az `egyezik' függvény
  az előző szó következő elemével fog lefutni. Amennyiben ezúttal volt
  eredmény, a flag ismét `True' lesz, és a két üzenet helyesen
  megcserélődik, valamint a kitalált szó is megújul.


4 Runtime error
═══════════════

  A probléma 99, 100 illetve a 110 és 111 sorban van. Ha az
  `uzenet1.betu', vagy az `uzenet1.szavak' értéke változik, akkor az
  `uzenet2.betu' vagy `uzenet2.szavak' is megkapja a változtatásokat,
  annak ellenére, hogy más memóriacímre mutat a két objektum. Ez igaz
  fordítva is. Így az `uzenet.fejtett' nem lesz jól visszabontva, emiatt
  a kitalált kulcs se, ami a következő szó visszafejtésénel problémát
  eredményez. Így nem tudja kitalalni a helyes szót, és egy idő után az
  `uzenet.szavak' mátrix utolsó eleméhez érünk. Ez eredményezi a
  `ListIndexOutOfRange' hibát.


5 Update:
═════════

  A referenciahibát megoldottam, de sajnos a visszalépés továbbra sem
  működik.  Viszont az `"big cabin"' és `"above cloud"' bemenetekkel a
  helyes `"abcdefjkilmn"' kulcsot kapjuk eredményül.
