# -*- coding: utf-8 -*-
import scrapy
import urllib

from scrapy.http import Request


class PdfbotSpider(scrapy.Spider):
    name = 'pdfbot'
    allowed_domains = ["https://www.privacy.gov.ph/"]
    start_urls = ["https://www.privacy.gov.ph/data-privacy-act-primer/",
                  "https://www.privacy.gov.ph/advisory-opinions/",
                  "https://www.privacy.gov.ph/memorandum-circulars/",
                  "https://www.privacy.gov.ph/advisories/",
                  "https://www.privacy.gov.ph/commission-issued-orders/"]

    def parse(self, response):
        base_url = 'https://www.privacy.gov.ph/'

        for a in response.xpath('//a[@href]/@href'):
            link = a.extract()
            # self.logger.info(link)

            if link.endswith('.pdf'):
                link = urllib.parse.urljoin(base_url, link)
                self.logger.info(link)
                yield Request(link, callback=self.save_pdf)

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)
