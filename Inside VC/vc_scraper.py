# -*- coding: utf-8 -*-
import scrapy
import math
#cft_gd, chp_gd, bjs_gd
import os
import csv
urll = 'https://inside.com/campaigns/inside-venture-capital-2017-11-05-3886'

class GlassDoor(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['inside.com']

    csv_file = "ruru_fix.csv"

    def start_requests(self):
        a = csv.DictReader(open(self.csv_file, 'r', encoding='utf-8'))
        for row in a:
            url = "https://inside.com" + row['Title']
            date = row['Title'].split("inside-venture-capital-")[1][:-5]
            request = scrapy.Request(url, callback=self.parse)
            request.meta["date"]=date
            yield request

    def parse(self, response):
        item = {}
        date_ = response.meta["date"]
        infor = response.xpath('//div[@id="campaign-archive"]/div/section/div/div[2]/div[1]').extract()
        nubs = infor[0].count("<p")

        infos = [response.xpath('//div[@id="campaign-archive"]/div/section/div/div[2]/div[1]/p[{}]'.format(i)).extract() for i in range(1,nubs+2)]

        print(infos)
        print(nubs)
        output_file = "fufu_new.csv"

        for title in infos:
            item['Title'] = title[0]
            item['date'] = date_

            my_path = os.path.abspath(os.path.dirname(__file__))
            path_out = os.path.join(my_path, output_file)

            with open(path_out, 'a', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=item.keys())
                if not os.fstat(f.fileno()).st_size > 0:
                    writer.writeheader()
                writer.writerow(item)





