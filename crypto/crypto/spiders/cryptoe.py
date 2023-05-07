import scrapy
from scrapy_playwright.page import PageMethod
from asyncio.windows_events import *
import json



class CryptoeSpider(scrapy.Spider):
    name = 'cryptoe'
    #allowed_domains = ['coinmarketcap.com']
    #start_urls = ['http://coinmarketcap.com/']

    def start_requests(self):
        yield scrapy.Request('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap')
    
    def parse(self, response):
        data = json.loads(response.body)
        parsed = []
        
        for items in data['data']['cryptoCurrencyList']:
            name = items['name']
            data = items
            #for values in data['quotes']:
            yield{
                'infoname':name,
                'name':data['quotes'][2]['name'],
                'price':data['quotes'][2]['price'],
                'volume24h':data['quotes'][2]['volume24h'],
                'volume7d':data['quotes'][2]['volume7d'],
                'volume30d':data['quotes'][2]['volume30d'],
                'lastUpdated':data['quotes'][2]['lastUpdated'],
                'marketCapByTotalSupply':data['quotes'][2]['marketCapByTotalSupply'],
                }

