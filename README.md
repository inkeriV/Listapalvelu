# Listapalvelu

Listapalvelussa kirjautunut käyttäjä voi luoda itselleen mitä tahansa listoja. Listoja voi käyttää esimerkiksi rästissä olevien tehtävien työlistana tai tarvittavien tavaroiden ostoslistana. Käyttäjällä voi olla samanaikaisesti monta listaa, joihin voi lisätä ja poistaa asioita. 

Käyttäjä voi myös luoda yhteisen listan useamman käyttäjän käyttöön. Ryhmälistaa voi käyttää esim. opettaja oppilaiden tehtävien listaamiseen tai tapahtumanjärjestäjät puuttuvien ruokien/tarvikkeiden kirjalla pitoon. Ryhmän luoja voi päättää, onko muilla ryhmän jäsenillä oikeutta muokata listaa. 

Ryhmälistaan saadaan linkki sen luojalta, josta käyttäjä voi liittää ryhmälistan omiin listoihinsa. 

# Toimintoja:

* Kirjautuminen
* Listan luominen
* Listaan lisääminen / listasta poistaminen
* Listan poistaminen
* Omien listojen listaaminen
* Ryhmälistan luonti & tyypin määrittely (mitä oikeuksia ryhmän jäsenillä on)
* Ryhmälistan poisto 
* Ryhmälistaan lisääminen / ryhmälistasta poistaminen
* Ryhmälistaan liittyminen
* Ryhmälistasta poistuminen


## Tietokantakaavio
![alt text](https://yuml.me/436b44e8.png "Tietokantakaavio")

[User stories](https://github.com/inkeriV/Listapalvelu/blob/master/documentation/user-story.md)

[Sovellus Herokussa](https://lista-palvelu-iv.herokuapp.com)

## Tunnukset

#### admin tunnukset: username: yllapitaja, password: hbkypitaja10 (admin näkee ja pystyy muokkaamaan/poistamaan kaikkien käyttäjien listoja)

#### tavallisen käyttäjän tunnukset
* käyttäjätunnus: tester12
* salasana: hbky12
* tai
* käyttäjätunnus2: tester13
* salasana2: hbky13


## Asennusohje Herokuun (alustava)

* Luo tunnukset Herokun nettisivuilla
* Lataa sovellus omalle koneellesi
* Käytetään Gunicorn palvelunta
* requirements.txt tiedostossa on Herokulle valmiina tiedot siitä, mitä riippuvuuksia sen pitää asentaa

* Kirjaudu Herokuun komentoriviltä komennolla "heroku login" tai "~/path/heroku login"
* Luo Herokuun paikka sovellukselle komennolla "heroku create sovelluksen-nimi"

## Käyttöohje

### Rekisteröityminen
* Luo itsellesi tunnukset painamalla Register-linkkiä etusivun oikeasta yläreunasta. 
* Syötä tekstikenttiin haluamasi nimi, käyttäjätunnus ja salasana, ja paina Register-nappia.
* Tämän jälkeen voit kirjautua sisään luomilla tunnuksillasi painamalla Login-linkkiä.
* Mikäli et siirry rekisteröitymis sivulta pois, syöttämäsi nimi, käyttäjätunnus tai salasana ovat liian lyhyitä/pitkiä tai salasanan varmistus ei onnistunut.

### Kirjautuminen
* Jos sinulla on jo tunnukset palveluun, pääset kirjautumaan painamalla oikeasta yläkulmasta Login-linkkiä.
* Kirjaudu sisään käyttäjätunnuksellasi ja salasanallasi.

### Listojen luonti
* Yläpalkin Create new list-linkistä pääset tekemään itsellesi listoja. Anna listalle nimi ja paina Create a new list-nappia.
* Tämän jälkeen siirryt Show all lists-sivulle, missä näät kaikki luomasi listat, voit lisätä listaan tehtäviä, tai poistaa listan.
* Lisää listaan tehtävä antamalla sille nimi, ja painamalla Add a job-nappia.
* Uuden listan voit luoda palaamalla Create a new list-sivuille. 

### Listojen käyttö
* Voit tarkastella yksittäistä listaa tarkemmin painamalla listan nimen vieressä olevaa muokkaa-linkkiä.
* Aukeavalla sivulla voit lisätä listaan töitä ja vaihtaa tehtävän statuksen.
* Työt statukset ovat: waiting - kun työtä ei ole aloitettu, in process - kun työ on kesken ja done - kun työ on saatu valmiiksi.
* Done-statuksen vaihtaminen muuttaa statuksen takaisin waiting-statukseski.

### Uloskirjautuminen
* Kun haluat lopettaa Listapalvelun käytön, paina oikeasta yläkulmasta linkkiä Logout. 
