# -*- coding: utf-8 -*-
import scrapy
import math
#cft_gd, chp_gd, bjs_gd
import os
import csv
urll = 'https://inside.com/recent-issues?page=2'

class GlassDoor(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['inside.com']
    start_urls = [urll]

    def parse(self, response):
        item = {}
        try:
            infor = response.xpath("//a[text()='Inside Venture Capital']/@href").extract_first()

            output_file = "ruru.csv"

            item['Title'] = infor
            item['Title2'] = infor

            my_path = os.path.abspath(os.path.dirname(__file__))
            path_out = os.path.join(my_path, output_file)

            with open(path_out, 'a', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=item.keys())
                if not os.fstat(f.fileno()).st_size > 0:
                    writer.writeheader()
                writer.writerow(item)

            next_page = response.xpath('//li[@class="next next_page "]//@href').extract_first()

            if next_page is not None:
                next_page = response.urljoin(next_page)
                request = scrapy.Request(next_page, callback=self.parse)
                yield request

        except:

            next_page = response.xpath('//li[@class="next next_page "]//@href').extract_first()

            if next_page is not None:
                next_page = response.urljoin(next_page)
                request = scrapy.Request(next_page, callback=self.parse)
                yield request







