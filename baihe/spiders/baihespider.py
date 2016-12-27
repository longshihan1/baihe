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
        baiheid=response_selector.select(u'//div[contains(@class, "data")]/dl/dt[1]').extract()
        baihe_item['baiheid'] =baiheid.split('：')[1]
        baihe_item['img'] = response_selector.select(u'//div[contains(@class, "big_pic")]/ul/li[1]/a/img/@src').extract()
        baihe_item['name'] = response_selector.select(u'//div[contains(@class, "name")]').extract()
        lovetype=response_selector.select(u'//div[contains(@class, "data")]/dl/dt[2]').extract()
        baihe_item['lovetype'] = lovetype.split(':')[1]

        baihe_item['description'] = response_selector.select(u'//div[contains(@class,"intr")]').extract()
        ahwe=response_selector.select(u'//div[contains(@class, "inter")]/p').extract()
        baihe_item['age'] = ahwe.split('//')[0]
        baihe_item['height'] = ahwe.split('//')[1]
        baihe_item['weight'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[1]/dd[1]').extract()
        baihe_item['education'] = ahwe.split('//')[2]
        baihe_item['address'] = ahwe.split('//')[3]
        baihe_item['income'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[1]/dd[0]').extract()
        baihe_item['marriage'] = ahwe.split('//')[4]
        baihe_item['self_evaluation'] = response_selector.select(u'//div[contains(@class, "inter label")]').extract()
        baihe_item['account'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[2]/dd[1]').extract()
        baihe_item['occupation'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[2]/dd[2]').extract()
        baihe_item['profession'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[2]/dd[3]').extract()
        baihe_item['familysituation'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[3]/dd[1]').extract()
        baihe_item['parentalstatus'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[3]/dd[2]').extract()
        baihe_item['motherwork'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[3]/dd[3]').extract()
        baihe_item['fatherwork'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[3]/dd[4]').extract()
        baihe_item['marriagetime'] = response_selector.select(u'//dl[contains(@class, "r")]/dd[1]').extract()
        baihe_item['dating'] = response_selector.select(u'//dl[contains(@class, "r")]/dd[2]').extract()
        baihe_item['otherfancy'] = response_selector.select(u'//dl[contains(@class, "r")]/dd[3]').extract()
        baihe_item['cooking'] = response_selector.select(u'//dl[contains(@class, "r")]/dd[4]').extract()
        baihe_item['manage'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[5]/dd[1]').extract()
        baihe_item['manheight'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[5]/dd[2]').extract()
        baihe_item['manedu'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[5]/dd[3]').extract()
        baihe_item['manincome'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[5]/dd[4]').extract()
        baihe_item['manaddress'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[6]/dd[1]').extract()
        baihe_item['hobbies'] = response_selector.select(u'//div[contains(@class, "like")]/div[contains(@class, "cont")]').extract()
        baihe_item['bodytype'] = response_selector.select(u'//div[contains(@class, "perData")]/dl[1]/dd[7]').extract()
        yield baihe_item
