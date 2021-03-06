# Listapalvelu

Listapalvelussa kirjautunut käyttäjä voi luoda itselleen listoja. Listoja voi käyttää esimerkiksi rästissä olevien tehtävien työlistana tai tarvittavien tavaroiden ostoslistana. Käyttäjällä voi olla samanaikaisesti monta listaa, joihin voi lisätä ja poistaa asioita. 

Käyttäjä voi myös luoda yhteisen listan useamman käyttäjän käyttöön. Ryhmälistaa voi käyttää esim. opettaja oppilaiden tehtävien listaamiseen tai tapahtumanjärjestäjät puuttuvien ruokien/tarvikkeiden kirjalla pitoon. Ryhmän luoja voi päättää, onko muilla ryhmän jäsenillä oikeutta muokata listaa. 

Ryhmälistaan saadaan linkki sen luojalta, josta muut käyttäjät pystyvät tarkastelemaan listaa. 


[Sovellus Herokussa](https://lista-palvelu-iv.herokuapp.com)

## Tunnukset

#### Admin tunnukset
```
username: yllapitaja 
password: hbkypitaja10 
```
* admin näkee ja pystyy muokkaamaan/poistamaan kaikkien käyttäjien listoja
* vain admin näkee SQL-kyselyt

#### Tavallisen käyttäjän tunnukset
```
käyttäjätunnus: tester12
salasana: hbky12
```
tai
```
käyttäjätunnus2: tester13
salasana2: hbky13
```

## Toimintoja:

* Rekisteröityminen
* Kirjautuminen
* Listan luominen
* Listaan lisääminen / listasta poistaminen
* Listassa olevien töitten statuksen vaihtaminen
* Listan näkyvyyden vaihtaminen
* Listan poistaminen
* Omien listojen listaaminen

## Dokumentaatio

### Tietokantakaavio
![alt text](https://yuml.me/845eedc9.png "Tietokantakaavio")


[User stories](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/user-story.md)

[Asennusohje](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/asennusohje.md)

[Käyttöohje](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/kayttoohje.md)

[CREATE TABLE-lauseet](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/createtable-lauseet.md)

[SQL-kyselyt](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/sql-kyselyt.md)

[Sovelluksen puutteet](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/puutteet.md)

[Omat kokemukset](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/kokemukset.md)
