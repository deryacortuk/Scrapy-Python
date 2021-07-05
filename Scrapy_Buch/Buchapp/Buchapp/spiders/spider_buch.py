
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bookdata" 
    page =0
    book_count=1

    file =open("books.txt","a",encoding="utf-8")           

    start_urls = [
        'https://www.ebay.de/b/Gebrauchte-Bucher/267/bn_7109686138'
    ]

    def parse(self, response):
        bookname=  response.css(" a.s-item__link  h3.s-item__title::text").extract()     
        bookprice = response.css("div.s-item__detail.s-item__detail--primary  span.s-item__price::text").extract() 
        i = 0 
        
        while(i<len(bookname)):            
            
            self.file.write("****************\n")
            self.file.write(str(self.book_count)+".\n")
            self.file.write("Book name: "+bookname[i]+"\n")
            self.file.write("Book price:" + bookprice[i]+"\n")
            
            self.file.write("****************")
            self.book_count +=1
            i +=1
            
        next_url = response.css('a.ebayui-pagination__control::attr(href)')[1].extract() 

        self.page +=1

        if next_url is not None and self.page !=8:
            yield scrapy.Request(url=next_url,callback=self.parse)
        else:
            self.file.close()

        
      