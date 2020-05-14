## web-scraper

#### Overview

This project deals with web crawling and web scraping framework, used to crawl websites and extract structured data (pdf, in this case) from their webpages. It can be used for organised collection of pdf files.

#### Requirements
- Python 3.5+ \
- Works on Linux\
- Windows\
- macOS\
- Scrapy

#### Installation Requirement
The quick way: 

```pip install scrapy```\
See the install section in the documentation at https://docs.scrapy.org/en/latest/intro/install.html for more details.

#### How to run

- Clone this repository\
```git clone repository's link``` \
- Go into Project's Directory \
- Install all other dependencies \
``` cd directory-name``` \
- Run \ ```scrapy crawl file's name``` in terminal

#### How to run this project on localhost

- Install scrapyd 
```pip install scrapyd```\
- Run server using
```scrapy``` in terminal \
- Open the localhost link \
- Run command ```scrapyd-deploy default``` \ while scrapy server is still running
- Use curl commands to send http requests \
```curl http://localhost:6800/schedule.json -d project=pdfscraper -d spider=pdfbot``` 


