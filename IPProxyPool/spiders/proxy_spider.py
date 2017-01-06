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

    def parse(self, response):
        print '***************' + response.url + '****************************'
        for trs in response.css('#ip_list tr:not(tr:first-child)'):
            if len( trs.xpath('td[7]/div/div[contains(@class, "slow")]').extract() ) == 0 :
                print trs.xpath('td[2]/text()').extract()[0] + ':' + trs.xpath('td[3]/text()').extract()[0]