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

# Hei koodikatselmoija!
* sovellusta ei oikein pääse katsomaan, koska tunnukset eivät toimi. Jos saat jotain ideaa siitä, mistä se voi johtua, olisin hyvin kiitollinen. Ohjelma pyörii siis lokaalisti moitteetta, mutta en saa sovellusta käyttämään herokun tietokantaa.
* Aloitussivulla redirectit kirjautumislomakkeelle toimii, mutta heti kun sovelluksen pitäisi lukea tietokantaa, se kaatuu. Procfile on tällä hetkellä web: gunicorn application:app --preload, tuota ennen se oli niin kuin esimerkissäkin aluksi web: gunicorn --preload --workers 1 application:app.
* Koetin vaihtaa application -kansion __init__.py tiedoston if ehtoon "if os.environ.get("HEROKU"):" lanausmerkkien sisään HEROKUn tilalle jotain muuta, jolloin sovellus ei kaadu Show all lists eikä Login komentoon. Login ilmoittaa vain ettei kyseisiä tunnuksia ole, koska ympäristömuuttuja oli vain jotain tekstiä eikä viitannut herokun tietokantaan.
* Koneeltani näen heroku pg:psql komennolla että tietokannassani on 2 taulua ja olen syöttänyt account-tauluun kyseiset tunnukset.
![alt text](/home/vbinkeri/Pictures/muutettu.jpg "tietokanta")

## Tunnukset
* käyttäjätunnus: tester12
* salasana: hbky12
* HUOM! tunnukset ei toimi. En saa sovellusta käyttämään herokun postgresql:lää. Sovellus toimii lokaalisti, mutta heti kun sovelluksen pitäisi lukea herokun tietokantaa, johon tunnukset on tallennettu, se kaatuu. 

