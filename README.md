# Tehtävä 1 -> MaterialTrackingTestBench.py

Tarkoituksena on saada seuraavanlainen toiminta.

1. Kysytään rfid lukijalta näkeekö se mitään rfid tagia
2. Mikäli tagi löytyy varmistetaan käyttäjältä onko tägi oikealla numerolla
3. Jos tägi löytyy kysytään käyttäjältä onnistuiko testi
4. Lähetetään testin tulos ja tägi tietokantaan.

Tehtävää varten yksinkertaistetaan asiaa hieman. Tehtävän specsi on seuraava:

- Määrittele funktio joka testaa löytääkö rfid lukija tägiä

  - Funktiota kutsutaan pääohjelmassa koko ajan kunnes tagi löytyy
  - lukijalta kysytään löytyykö tägi käyttämällä funktiota getTag()
  - Kysyminen suoritetaan painamalla enter näppäintä
  - Kun tägi löytyy pitää siitä ilmoittaa käyttäjälle
  - Löydetty tägi tallennetaan myös pääohjelman muuttujaan

- Määrittele funktio joka kysyy onko testi onnistunut

  - Funktio kysyy käyttäjältä onnistuiko testi
  - Käyttäjä kirjoittaa y tai n mikäli testi onnistui tai ei
  - Vain y tai n hyväksytään vastaukseksi
  - Ohjelma vielä varmistaa käyttäjältä että onko tämä varmasti vastauksesi
    - Mikäli käyttäjä vastaa tähän n niin ohjelma kysyy taas onnistuiko testi vai ei
  - Kun kysely on tehty kerrotaan käyttäjälle vastaus ja tallennetaan vastaus pääohjelman muuttujaan

- Määrittele funktio joka tallentaa tiedot tietokantaan

  - tagin id ja vastaus testiin tulee tallettaa dictionary muuttujaan
  - funktio ottaa tämän dictionary muuttujan inputtina
  - kun funktiota kutsutaan se tulostaa käyttäjälle inputin tiedot esim.
    TagId: 45267
    TestSucceeded: True
  - lopuksi kutsutaan vielä saveToDatabase() nimistä funktiota johon laitetaan inputtina vielä tämän funktion input
  - Funktio palauttaa saveToDatabase() funktion tuloksen

- Pääohjelma toimii seuraavalla tavalla
  - Mikäli tag idtä ei vielä ole löydetty kutsutaan rfid lukija funktiota
  - Jos tag id on löydetty kutsutaan testikysely funktiota
  - Mikäli Vastaus on saatu kutsutaan tietokantatallennus funktiota

Muista keskittyä myös käyttäjälle kerrottaviin asioihin ja tapahtumiin. Mieti missä ja miten olisi hyvä tarkistaa kaatuuko ohjelma vai ei.
