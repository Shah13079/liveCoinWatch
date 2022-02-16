# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from sqlalchemy.orm import sessionmaker
from .models import db_connect, create_table, LiveCoin_data_model


class BlockchainwebsitesPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.

        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def process_item(self, item, spider):
        """
        Save data in the database.

        This method is called for every

        item pipeline component.

        """
        item_exists = (
            self.session.query(LiveCoin_data_model).filter_by(code=item["code"]).first()
        )

        if item_exists:
            item_exists.price = item.get("price")  # Update the price here
            item_exists.cap = item.get("cap")
            item_exists.totalCap = item.get("totalCap")
            item_exists.maxSupply = item.get("maxSupply")
            item_exists.totalSupply = item.get("totalSupply")
            item_exists.rank = item.get("rank")
            item_exists.circulating = item.get("circulating")
            item_exists.issued = item.get("issued")
            item_exists.volmcap = item.get("volmcap")
            item_exists.exchanges = item.get("exchanges")
            item_exists.delta = item.get("delta")
            item_exists.deltav = item.get("deltav")

        elif item_exists is None:
            new_item = LiveCoin_data_model(**item)  # Unpacking the the data
            self.session.add(new_item)

        # Commiting the changes for each item
        try:
            self.session.commit()
        except:
            self.session.rollback()
            raise

        return item

    def close_spider(self, spider):
        """
        Closing the session with db
        when spider closed

        """
        self.session.close()
