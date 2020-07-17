import scrapy


class BooksSpider(scrapy.Spider):
    name = "books_spider"

    def start_requests(self):
        urls = ['http://books.toscrape.com/catalogue/page-1.html', ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''  page_id = response.url.split('/')[-1][-6]
        #filename = "books-%s.html" % page_id '''

        for q in response.css('article.product_pod'):
            img = q.css('div.image_container a img').attrib['src']
            title = q.css('h3 a::attr(title)').get()
            price = q.css('div.product_price p.price_color::text').get()

            yield {
                'image_url': img,
                'book_title': title,
                'product_price': price,
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
