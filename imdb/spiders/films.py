import scrapy
from imdb.items import ImdbItem

class FilmsSpider(scrapy.Spider):
    name = "films"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    
    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque produit
    #pour obtenir plus de détails.
    def parse(self, response):
        films = response.css('li.ipc-metadata-list-summary-item')
        for film in films: #on parcours chaque pokemon un pokemon = li.product
            titre = film.css('h3.ipc-title__text::text').get()
            film_url = film.css('a::attr(href)').get() #on prend le href a chaque film
            # yield {
            #     'title': title,
            #     'url': film_url
            # }
            
            
            yield response.follow(film_url, self.parse_product, meta = {'titre': titre})

        # #pagination
        # next_page = response.css('.page-numbers a.next::attr(href)').get()
        # if next_page:
        #     yield response.follow(url=next_page, callback=self.parse)


    #fonction est appelée pour chaque page de produit. 
    #elle extrait et enregistre les détails tels que le nom, le prix, la description, et l'URL.
    def parse_product(self, response):
        titre = response.meta.get('titre')
        
        film_item = ImdbItem()

        film_item['titre'] = titre
        film_item['titre_original'] = response.css('h1 span.hero__primary-text::text').get()
        # film_item['score'] = response.css
        # film_item['genre'] = response.
        # film_item['year'] = response.
        # film_item['duree'] = response.css
        # film_item['description'] = response.css
        # film_item['acteurs'] = response.css
        # film_item['public'] = response.css
        # film_item['pays'] = 
        # film_item['langue_origine'] = 
    

        yield film_item
        
        
        
        
        
        
        
        # yield {
        #         'titre': titre,
        #         'titre_original': titre_original,
        #         # 'score':
        #         # 'genre':
        #         # 'year':
        #         # 'duree':
        #         # 'description':
        #         # 'acteurs':
        #         # 'public':
        #         # 'pays':
        #         # 'langue_origine':
        #     }
        
        
        
        
        
        
        # longueur = largeur = hauteur = None
        # if dimension: 
        #     #regex pour prendre les differentes dimensions sur le string 6x6x6
        #     pattern = r"(\d) x (\d) x (\d)"
        #     match = re.search(pattern, dimension)
        #     if match:
        #         longueur = match.group(1)
        #         largeur = match.group(2)
        #         hauteur = match.group(3)
        #     else:
        #         print('rien trouvé')
        # else:
        #     print('rien trouvé')

        
        # poke_item = PokeItem()

        
        # poke_item['name'] = name
        # poke_item['prix'] = response.css('p.price span.woocommerce-Price-amount::text').get()
        # poke_item['description'] = response.css('div.woocommerce-product-details__short-description p::text').get()
        # poke_item['url'] = response.url
        # poke_item['stock'] = response.css('p.stock::text').get()
        # poke_item['categories'] = response.css('span.posted_in a::text').get()
        # poke_item['tags'] = response.css('span.tagged_as a::text').get()
        # poke_item['sku'] = response.css('span.sku::text').get()
        # poke_item['poids'] = response.css('td.product_weight::text').get()
        # poke_item['longueur'] = longueur
        # poke_item['largeur'] = largeur
        # poke_item['hauteur'] = hauteur
    

        # yield poke_item
