# hackernews_web_scraper
This is a fairly simple project to scrape title, links and user scores from hackernews.com.
The code uses Beautiful Soup to handle the web scraping.
It only collects data from submissions within the 3 most recent pages that have user votes of 100 or greater.
The data is then sorted by score in descending order.
Finally, the data is written to a vertical piple deliminated .csv file. 
