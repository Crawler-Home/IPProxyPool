# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IpproxypoolPipeline(object):

    def __init__(self):
        self.file = open('data.json', 'wb')

    def process_item(self, item, spider):
        self.file.write('{\'ip_port\': \'' + item['ip'] + ':' + item['port'] + '\', \'user_pass\': \'\'},\n')
