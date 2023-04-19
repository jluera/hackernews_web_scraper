import requests
import csv
from bs4 import BeautifulSoup

# triple variations of variables to get 3 pages of hackernews
req = requests.get('https://news.ycombinator.com/news')  
req2 = requests.get('https://news.ycombinator.com/news?p=2') 
req3 = requests.get('https://news.ycombinator.com/news?p=3') 
soup = BeautifulSoup(req.text, 'html.parser')
soup2 = BeautifulSoup(req2.text, 'html.parser')
soup3 = BeautifulSoup(req3.text, 'html.parser')
links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
links3 = soup3.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
subtext3 = soup3.select('.subtext')
multi_links = links + links2 + links3
multi_subtext = subtext + subtext2 + subtext3

# sort stories by score in descesnding order
def top_stories(stories):
    return sorted(stories, key=lambda k:k['votes'], reverse=True)

# scrape hackernews for story links and title with scores of 100 or more
def scrape_hackernews(links, subtext):
    hackernews = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score >= 100:
                hackernews.append({'title': title, 'link': href, 'votes': score})
    return top_stories(hackernews)

def write_to_file(file):
    with open('scraped_hackernews.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'link', 'votes'], delimiter="|")
        writer.writeheader()
        writer.writerows(file)

if __name__ == '__main__':
    scraped_news = scrape_hackernews(multi_links, multi_subtext)
    write_to_file(scraped_news)
  
