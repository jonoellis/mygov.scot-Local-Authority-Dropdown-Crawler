# mygov.scot Local Authority Dropdown Crawler

A [Scrapy](https://scrapy.org/) crawler to help check for broken links on [mygov.scot](https://www.mygov.scot/).

* Run Screaming Frog with a "search" for "link-la"
* Export these URLs to "urls.txt"
* Download scrapy_crawl.py to the same folder as "urls.txt"
* Run using the following command:
```
scrapy runspider scrapy_crawl.py -t csv -o $(date +%Y%m%d-%H%M%S).csv
```
* Import to the ["LA-Links" sheet](https://docs.google.com/spreadsheets/d/1hKIUaAvNh9Izg_JXjsJx17HHTUpzdinCRf8LtXjbaD4/edit#gid=0)
* Run Screaming Frog in list mode with all LA Links
* Paste the export from Screaming Frog to the ["Broken" sheet](https://docs.google.com/spreadsheets/d/1hKIUaAvNh9Izg_JXjsJx17HHTUpzdinCRf8LtXjbaD4/edit#gid=0)

## Links
* [Scrapy](https://scrapy.org/)
* [Documentation](https://docs.scrapy.org/en/latest/index.html)

## Next Steps
* Index site recursively
* Check and report status of each link URL
* Check and report redirected URLs
