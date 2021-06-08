from os import link
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from essay_spider.items import Volume

def parse_link(response):
    ...

def parse_essay(response):
    print("Found essay")

class AiSpiderSpider(Spider):
    name = 'ai_spider'
    allowed_domains = [
        "dblp.uni-trier.de",
        "www.sciencedirect.com"
        "doi.org"
    ]
    journals = ["ai", "pami", "ijcv", "jmlr"]
    conferences = ["aaai", "nips", "acl", "cvpr", "iccv", "icml", "ijcai"]
    url_dicts = {
        "journals": journals,
        "conf": conferences
    }
    start_urls = ["https://dblp.uni-trier.de/db/journals/ai/index.html"]
    essay_list = []
    keywords = []
    # _rules = (
        # Rule(LinkExtractor(allow_domains=allowed_domains, allow=(r"db"), deny=(r"pid", r"rec", r"search")), callback=parse_link, follow=True),
    # )

    def __init__(self):
        pass
        # for k, v in self.url_dicts.items():
            # for name in v:
                # self.start_urls.append(f"https://{self.allowed_domains[0]}/db/{k}/{name}/index.html")
        # print(self.start_urls)

    def parse(self, response):
        requests = []
        # index page, acquire volume info
        if response.xpath("//*[@id=\"info-section\"]"):
            yearly_list = response.xpath("//*[@id=\"main\"]/ul/li")
            # print(yearly_list)
            for year_volumes in yearly_list:
                year = year_volumes.xpath("text()").extract_first()[0:4]
                # print(year)
                volume = Volume()
                volume_selectors = year_volumes.xpath("a")
                # print(volume_selectors)
                for selector in volume_selectors:
                    volume["id"] = selector.xpath("text()").extract_first()
                    volume["year"] = int(year)
                    link = selector.xpath("@href").extract_first()
                    volume["link"] = link
                    requests.append(Request(link))
                    self.essay_list.append(volume)
        elif response.xpath("/html/body/div/ul/li[@class=\"entry article\"]"):
            article_selectors = response.xpath("/html/body/div/ul/li[@class=\"entry article\"]")
            print(article_selectors)
            for article_selector in article_selectors:
                article_link = article_selector.xpath("nav/ul/li/div/a/@href").extract_first()
                print(article_link)
                requests.append(Request(article_link))
                    # print(link)
        # link_extractor = LinkExtractor()
        # links = link_extractor.extract_links(response)
        # print(links)
        return requests



                
