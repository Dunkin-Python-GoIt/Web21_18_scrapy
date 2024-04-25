# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyScrapPipeline:
    def process_item(self, item, spider):
        raw_location = item.get("location")
        if raw_location:
            item["location"] = raw_location.replace("\n", "").strip() 
        return item


class MyNewPipeline:
    def process_item(self, item, spider):
        if spider.name == "quotes":
            self.my_method()
            return item
        normal_title: str = item.get("job_title")
        normal_title: str = item.get("author")
        if normal_title:
            item["job_title_upper"] = normal_title.upper()
        return item
    
    def my_method(self):
        print("I am method")