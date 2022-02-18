**About**:<br/>
This project is made with python scrapy framework, the spider "live_coint" scrape livecoinwatch website coins markets, it directly sends requst to the API of this website and fetching the data based on payload querySet.

Instead of editing the code, the spider accept start_page argument from CMD, So the spider will crawl starting from specific page provided by user.

In pipelines.py the pipelines and models are written with ORMS  using SQLAlchemy, which saving data into Postgres database, and on the second run it will update the existing stocks and add the new stocks. The website don't allow to crawl their data continously therefore some downloaded delay of 3 seconds is set in request.

**Some features**:<br/>
1) database integration
2) ORM used
3) Passing arguments with CMD
4) models
5) Crawling direct API end point


**Tools and packages used in this project:**<br/>
Python<br />
Scrapy framework<br />
Postgres: a free and open-source relational database management system<br />
ORM :Object–relational mapping<br />
SQLAlchemy: an open-source SQL toolkit and object-relational mapper for Python<br />

**Setup:**<br/>
Donwload python from official website: https://www.python.org/downloads/ <br/>
Scrapy requires Python 3.6+<br />
Make sure pip package-management system is installed

**Prerequisites:** <br />
Open CMD and change working directory into project directory and give command:<br/>
pip install -r requirements.txt <br/>
this will install all required dependencies and packges.

**Database Connection** <br />
If you want to connect to database change the db_name=<Your db name>,user="<User>", passwd="<Password>" according to your credentials in settings.py.

```
#Setting Database
CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}".format(
    drivername="postgresql", 
    user="postgres",
    passwd="khanbbbb",
    host="127.0.0.1",
    port="5432",
    db_name="livecoinwatch",
)
```


**Enable/disable pipelines:** <br />
Note:
If you don't want to use Database Simply comment out bellow piplines in settings.py:
```
ITEM_PIPELINES = {
   'blockChainWebsites.pipelines.BlockchainwebsitesPipeline': 300,
}

```

**Run:** <br />
1) Run for default Url:<br />```scrapy crawl live_coint -o data.csv```  (-o filename.csv will generate data csv file ) <br/>
2) Pass start page parameter by command:<br/>```scrapy crawl live_coint -a start_page=integer_pagenumber -o OUTPUT_FILE.csv``` <br/>


**Cancel Process:** <br />
CTRL+C to cancel.


**Licence** <br />
Feel free to contribute to code and use in your personal & commercial projects. Happy coding


-----------------------------------------------------------------------------------------
