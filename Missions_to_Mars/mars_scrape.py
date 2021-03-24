from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    browser = Browser('chrome', **executable_path, headless=False)
    title, paragraph = news(browser)
    mars = {
        'title': title,
        'paragraph': paragraph,
        'image': image(browser),
        'facts': facts(),
        'hemispheres': pheres(browser)
    }

    return mars

def news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    title = browser.find_by_css('div.content_title').text
    paragraph = browser.find_by_css('div.article_teaser_body').text
    return title, paragraph

# ### JPL Mars Space Images - Featured Image
# * Visit the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).
def image(browser):
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    return browser.find_by_css('a.showimg')['href']

# ### Mars Facts
# * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
def facts():
    return pd.read_html('https://space-facts.com/mars/')[0].to_html()

# ### Mars Hemispheres
# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
def pheres(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    links = browser.find_by_css('a.itemLink h3')
    hemispheres = []
    for i in range(len(links)):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)    
        browser.back()
    browser.quit()
    return hemispheres

