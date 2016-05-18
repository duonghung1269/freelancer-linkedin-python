import scrapy
from ..items import LikedinItem
class LinkedinSpider(scrapy.Spider):

    name = "linkedinspider"
    #allowed_domains "C:\Users\sgscdhdx\Downloads\Archive\Search _ LinkedIn.htm"
    #start_urls = ["file:///C:/Users/sgscdhdx/Downloads/Archive/Search _ LinkedIn.htm"]

    def start_requests(self):
        # TODO: need to read all copany ID from csv file here
        # url format: https://www.linkedin.com/vsearch/p?f_CC={id_from_csv}&trk=rr_connectedness
        yield scrapy.Request('file:///C:/Users/sgscdhdx/Downloads/Archive/Search _ LinkedIn.htm', self.parse)
        #yield scrapy.Request('http://www.example.com/2.html', self.parse)
        #yield scrapy.Request('http://www.example.com/3.html', self.parse)

    def parse(self, response):
        # print response.body
        #for h3 in response.xpath('//h3').extract():
            #yield MyItem(title=h3)

        #for url in response.xpath('//a/@href').extract():
            #yield scrapy.Request(url, callback=self.parse)
        items = []
        for li in response.xpath('//div[@id="results-container"]/ol[@id="results"]/li'):
            aElement = li.xpath('div[@class="bd"]/h3/a')
            companies = li.xpath('dl[@class="snippet"]/p[@class="title"]//b')
            fullName = aElement.xpath('text()').extract()[0]
            fullNames = fullName.split(" ")
            firstName = ""
            lastName = ""

            if len(fullNames) > 1:
                firstName = fullNames[0]
                fullNames.pop(0)
                lastName = " ".join(fullNames)
            profileUrl = aElement.xpath('@href').extract()[0]
            profileUrl = profileUrl[0:profileUrl.index("&")]
            item = LikedinItem(fullname=fullName, firstname=firstName, lastname=lastName, profileurl=profileUrl)
            items.append(item)
        return items