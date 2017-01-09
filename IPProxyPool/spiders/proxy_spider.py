# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from IPProxyPool.items import IpproxypoolItem


class ProxySpider(CrawlSpider):
    name = "proxy"
    allowed_domains = ["xicidaili.com"]
    start_urls = [
        "http://www.xicidaili.com/nt",
    ]
    rules = [
        Rule(LinkExtractor(allow=(r'/nt/\d+')), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        print '***************' + response.url + '****************************'

        items = []
        for trs in response.css('#ip_list tr:not(tr:first-child)'):
            if len( trs.xpath('td[7]/div/div[contains(@class, "slow")]').extract() ) == 0 :
                item = IpproxypoolItem()
                item['ip'] = trs.xpath('td[2]/text()').extract()[0]
                item['port'] = trs.xpath('td[3]/text()').extract()[0]
                items.append(item)

        return items