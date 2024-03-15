# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import sqlite3

class ImdbPipeline:
    def open_spider(self, spider):
        # creation de la bdd sqlite
        self.connection = sqlite3.connect('imdb.db') 
        self.c = self.connection.cursor()
        # creation la table si elle n'existe pas déjà
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS imdb (
                titre TEXT,
                score REAL,
                genre TEXT,
                year INTEGER,
                duree INTEGER
            )
        ''')
        self.connection.commit()
        
    def process_item(self, item, spider):
        
        
        adapter = ItemAdapter(item)
        #print('objet :', adapter)
        
        #field titre
        #supprimer 123. 
        adapter['titre'] = re.sub(r'^\d+\.\s*', '', adapter['titre'])
        
        #field score
        #convertir en float
        score = adapter.get('score')
        adapter['score'] = float(score)
        
        #field genre
        #retirer la valeur back to top en fin de liste
        genre = adapter.get('genre')
        #je recupere la dernière valeur de la liste
        last_value = genre[-1]
        if last_value == "Back to top":
            #pop parametre c'est l'index donc je lui dis retire moi le dernier
            genre.pop(-1)
        #print(genre)
        
        #field year
        #prend que les quatres premier chiffres
        cleaned_year = re.search(r'\d{4}', adapter['year']).group()
        adapter['year'] = int(cleaned_year)
        
        #field duree
        duree = adapter.get('duree')
        nombre_heure = 0
        minutes = 0

        if 'h' in duree:
            # separation heures et les minutes
            duree_split = duree.split('h')
            nombre_heure = int(duree_split[0])
            # verification s'il y a des minutes après 'h'
            if 'm' in duree_split[1]:
                minutes = int(duree_split[1].strip('m'))
        elif 'm' in duree:  # si la chaîne ne contient que des minutes
            minutes = int(duree.strip('m'))

        # conversion en minutes
        nouvelle_valeur_duree = (nombre_heure * 60) + minutes
        print(f"La durée totale est de {nouvelle_valeur_duree} minutes.")
        adapter['duree'] = nouvelle_valeur_duree
        
        
        #insertion en bdd
        self.c.execute('''
            INSERT INTO imdb (titre, score, genre, year, duree) VALUES (?, ?, ?, ?, ?)
        ''', (
            adapter.get('titre'),
            adapter.get('score'),
            ','.join(adapter.get('genre')),  # conversion de la liste en chaîne de caractères puisque SQLite ne prend pas en charge le stockage direct de listes ou d'arrays.
            adapter.get('year'),
            adapter.get('duree')
        ))
        self.connection.commit()
        
        return item 

    def close_spider(self, spider):
        self.connection.close()  # fermer la connexion à la base de données