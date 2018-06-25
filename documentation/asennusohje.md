## Asennusohje (Herokuun)

#### Käytössä:
* Python flask, PostgreSQL

#### Tarvitset:
* [Github](https://github.com/)- ja [Heroku](https://www.heroku.com/)-tilin


#### Alustus:
* Lataa koodi koneellesi esim. komentoriviltä komennolla:
```
git clone https://github.com/inkeriV/Listapalvelu.git
``` 
* Siirry virtuaaliympäristöön sovelluksen juurikansiossa komennolla:
```
source ENV/bin/activate
```
* Luo sovellukselle git-repositorio omalle Github-tilillesi, jotta ylläpito olisi helppoa.
* Komenna
```
git remote add origin https://github.com/käyttäjätunnus/sovelluksen-nimi.git
```
, jotta voit päivittää koodia gittiin.


#### Sovellus Herokuun:
* Luo viimeistään nyt tili [Herokuun](https://www.heroku.com/)
* Asenna [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
* Kirjaudu Herokuun komentoriviltä komennolla:
```
heroku login
```
* Luo sovellukselle paikka Herokuun komennolla:
```
heroku create haluamasi-nimi-sovellukselle
```
* Sovellukselle tulostuu osoite (muotoa sovelluksen-nimi.herokuapp.com/)
* Lisää Gittiin tieto Herokusta komennolla:
```
git remote add heroku sovelluksen-osoite-herokussa
```
* Projektin lähettäminen Herokuun onnistuu committaamalla Gittiin
```
git add .
git commit -m "commit teksti"
git push heroku master
```
* Suositeltavaa on käyttää [Herokun github-integraatiota](https://devcenter.heroku.com/articles/github-integration), jolloin Heroku päivittää sovellusta automaattisesti, kun Git-repo päivittyy.
* Sovellus on nyt asennettu Herokuun!

#### PostgreSQL-tietokanta
* Luo Herokuun postgresql-tietokanta komennolla:
```
heroku addons:add heroku-postgresql:hobby-dev
```
* Tietokantaa pääsee katsomaan komennolla:
```
heroku pg:psql
```
* Taulut näkyviin
```
\dt
```
* Poistu komennolla
```
\q
```

#### Sovellus lokaalisti
* Käynnistyy sovelluksen kotikansiossa komennolla:
```
python3 run.py
```
* Lokaali sovellus käyttää SQLite-tietokantaa
* Tietokantaa pääsee katsomaan komennolla:
```
sqlite3 application/lists.db
```
* Taulut näkyviin
```
.schema
``` 
* Ja poistu komennolla
```
.exit
```

#### Huomioitavaa
* Admin-käyttäjä on luotava komentoriviltä (admin syntyy, kun boolean admin on '1').
* Sovellukseen rekisteröityvistä käyttäjistä tulee automaattisesti vain käyttäjiä.
