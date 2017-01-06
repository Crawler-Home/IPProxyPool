import random
import base64
from IPProxyPool.settings import *

class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # print "**************************" + random.choice(self.agents)
        # request.headers = HEADER
        # request.headers.setdefault('User-Agent', random.choice(self.agents))

        for item, value in HEADER.items():
            request.headers[item] = value

        request.headers['User-Agent'] = random.choice(self.agents)
        # print request.headers