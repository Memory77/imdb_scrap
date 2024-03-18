--> 1.Quel est le film le plus long ?
SELECT titre, duree
from films f 
order by duree DESC 
limit 1



--> 2. Quels sont les 5 films les mieux notés ?
SELECT titre, score
from films f 
order by score DESC 
limit 5


--> 3. Dans combien de films a joué Morgan Freeman ? 
SELECT acteurs, count(titre)
from films f 
where acteurs LIKE '%Morgan Freeman%'

-- Tom Cruise ?
SELECT acteurs, count(titre)
from films f 
WHERE acteurs LIKE '%Tom Cruise%'



--> 4. Quels sont les 3 meilleurs films d'horreur ?
SELECT titre, genre, score
from films f 
where genre LIKE '%horror%'
ORDER by score DESC 
limit 3

-- dramatique ?
SELECT titre, genre, score
from films f 
WHERE genre LIKE '%drama%'
ORDER by score DESC 
limit 3

-- comique ?
SELECT  titre, genre, score
from films f 
where genre LIKE '%comedy%'
ORDER by score DESC 
limit 3



--> 5. Parmi les 100 films les mieux notés, quel pourcentage sont américains ? 
WITH tableau AS (
SELECT titre, score, pays, langue_origine 
from films f 
order by score DESC 
limit 100 
)
--SELECT count(titre)   output : 100 films 
--from tableau

SELECT count(titre) as total_film, pays
from tableau
group by pays

-- 57 films de United Stated donc comme il y a 100 films, il y a 57% de films américains. 
-- français ? 4% de films français.


--> 6. Quel est la durée moyenne d'un film en fonction du genre ?
SELECT AVG(duree) as duree_moy_film, genre
from films f 
group by genre



-------- Bonus 
--> 7. En fonction du genre, afficher la liste des films les plus longs
SELECT titre, genre, max(duree)
from films f 
group by genre

--> 8. En fonction du genre, quel est le cout de tournage d'une minute de film ? 
-- je passe

--> 9. Quelles sont les séries les mieux notées ? 
SELECT titre, score
from series s 
order by score DESC 


