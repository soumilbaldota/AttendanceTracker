import scrapy
from scrapy.crawler import CrawlerProcess
import argparse
class QuikspideySpider(scrapy.Spider):
    name = 'quikspidey'
    allowed_domains = ['quiklrn.com']
    start_urls = ['https://quiklrn.com/login.php']

    def __init__(self, email=None, password=None, *args, **kwargs):
        super(QuikspideySpider, self).__init__(*args, **kwargs)
        self.email = email
        self.password = password

    def parse(self, response):
        return scrapy.FormRequest.from_response(
        response,
        formdata={'email': self.email, 'password': self.password},
        callback=self.after_login,
        )

    def after_login(self, response):

        return scrapy.http.Request(
                url="https://quiklrn.com//user/report.php",
                callback = self.fetchreport
            )

    def fetchreport(self, response):
        s = (response.xpath('/html/body/div/div/div/div[3]').get())
        with open(f"data.html", "w") as out:
            out.write(s)
            out.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", help="my argument email")
    parser.add_argument("--password", help="my argument password")
    args = parser.parse_args()

    process = CrawlerProcess (settings={
    'USER_AGENT': 'Mozilla/5.0' ,
    })

    process.crawl (QuikspideySpider, email = args.email, password = args.password)
    process.start ()