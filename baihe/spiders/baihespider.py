import scrapy
from scrapy import Request
from scrapy.selector import HtmlXPathSelector

from baihe.items import BaiheItem


class BaiHeSpider(scrapy.Spider):
    name = "baihe"
    start_urls = (
        'http://search.baihe.com/solrAdvanceSearch.action',
    )

    def parse(self, response):
        response_selector = HtmlXPathSelector(response)
        idsvalue = response_selector.select(u'//input[@id="userIds"]/@value').extract()
        idvalue = idsvalue[0]
        ids = idvalue.split(',')
        for item in ids:
            lists = item.split(':')[0]
            url = 'http://profile1.baihe.com/?oppId=' + lists + '&showType=2012'
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        baihe_item = BaiheItem()
        response_selector = HtmlXPathSelector(response)
        baihe_item['baiheid'] = response_selector.select(u'//div[@class="womanData"]/div[@class="data"]/dl/dt[1]').extract()
        baihe_item['img'] = response_selector.select(u'//div[@class="big_pic"]/ul/li').extract()
        baihe_item['name'] = response_selector.select(
            u'//div[@class="womanData"]/div[@class="inter"]/div[@class="name"]/span[1]').extract()
        baihe_item['lovetype'] = response_selector.select(u'//div[@class="womanData"]/div[@class="data"]/dl/dt[3]').extract()
        yield baihe_item
