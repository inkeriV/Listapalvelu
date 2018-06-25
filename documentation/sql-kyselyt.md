## SQL-Kyselyt

* Kaikki käyttäjät järjestettynä listamääränsä mukaan laskevaan järjestykseen
```sql
SELECT Account.id, Account.name, COUNT(*) 
FROM Account INNER JOIN Lists 
ON Account.id=Lists.account_id 
GROUP BY Account.id ORDER BY COUNT(Lists.id) DESC
```

* Käyttäjät, joilla on aloittamattomia töitä
```sql
SELECT DISTINCT Account.id, Account.name FROM Account, Lists, Jobs
WHERE Account.id = Lists.account_id AND Lists.id = Jobs.list_id AND Jobs.id 
NOT IN(SELECT Jobs.id FROM Jobs WHERE Jobs.status=2 OR Jobs.status=3)
```

* Käyttäjät, joilla ei ole yhtään listaa
```sql
SELECT DISTINCT Account.id, Account.name FROM Account 
WHERE NOT EXISTS(SELECT DISTINCT Lists.account_id 
FROM Lists WHERE" Account.id=Lists.account_id)
```