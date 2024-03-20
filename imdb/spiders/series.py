import scrapy
from imdb.items import SeriesItem

class SeriesSpider(scrapy.Spider):
    name = "series"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/"]

    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque produit
    #pour obtenir plus de détails.
    def parse(self, response):
        series = response.css('li.ipc-metadata-list-summary-item')
        for serie in series: #on parcours chaque serie
            titre = serie.css('h3.ipc-title__text::text').get()
            serie_url = serie.css('a::attr(href)').get() #on prend le href a chaque film
            # yield {
            #     'title': title,
            #     'url': film_url
            # }
            
            
            yield response.follow(serie_url, self.parse_product, meta = {'titre': titre})

        # #pagination
        # next_page = response.css('.page-numbers a.next::attr(href)').get()
        # if next_page:
        #     yield response.follow(url=next_page, callback=self.parse)


    #fonction est appelée pour parcourir chaque page de serie. 
    def parse_product(self, response):
        titre = response.meta.get('titre')
        
        serie_item = SeriesItem()

        serie_item['titre'] = titre
        serie_item['titre_original'] = response.css('h1 span.hero__primary-text::text').get()
        serie_item['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]//span/text()').get()
        serie_item['genre'] = response.css('span.ipc-chip__text::text').getall()
        serie_item['year'] = response.css('a[href*="releaseinfo"]::text').get()
        serie_item['duree'] = response.xpath('//li[@class="ipc-inline-list__item"]/following-sibling::li[1]/text()').get()
        serie_item['description'] = response.xpath('//span[@data-testid="plot-l"]/text()').get()
        serie_item['acteurs'] = response.xpath('//div[@data-testid="title-cast-item"]//a[@data-testid="title-cast-item__actor"]/text()').extract()
        serie_item['langue_origine'] = response.xpath('//a[contains(@class, "ipc-metadata-list-item__list-content-item") and contains(@href, "primary_language")]/text()').get()
        serie_item['pays'] = response.css('li[data-testid="title-details-origin"] .ipc-metadata-list-item__list-content-item--link::text').get()
        serie_item['public'] = response.css('a[href*="certificates"]::text').get()
    

        yield serie_item
