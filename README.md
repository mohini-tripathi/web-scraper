## web-scraper using Python

#### Overview

This project is about web crawling and web scraping framework, used to crawl websites and extract structured data (pdf, in this case) from their webpages. It can be used for organised collection of pdf files.

#### Requirements to run this project
- Python 3.5+ 
- Scrapy


#### Installation Requirement
Follow the quick way: 

```pip install scrapy```
Check out the install section in the documentation at https://docs.scrapy.org/en/latest/intro/install.html for more details.

#### How to run

- Clone this repository
```git clone repository's link``` 
- Go into Project's Directory 
- Install all the missing dependencies using pip
``` cd directory-name``` 
- Run  ```scrapy crawl file's name``` in terminal

#### How to run this project on localhost

- Install scrapyd 
```pip install scrapyd```
- Run server using
```scrapy``` in terminal 
- Open the localhost link 
- Run command ```scrapyd-deploy default``` while scrapy server is still running
- Use curl commands to send http requests 
```curl http://localhost:6800/schedule.json -d project=pdfscraper -d spider=pdfbot``` 

CA:B1:AF:0D:2B:EC:8F:81:74:61:0B:A4:9F:FB:C6:AE:3C:3B:50:58


