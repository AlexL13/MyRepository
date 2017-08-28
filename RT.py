from bs4 import BeautifulSoup
import requests



def get_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    names = soup.select('#contentReviews > h2 > em')
    dates = soup.select('div.meta-value > time')
    reviews = soup.select('div.review_quote > div > div.media-body > p')

    infos = soup.select('#movieSynopsis')
    ratings = soup.select('#tomato_meter_link > span.meter-value.superPageFontColor > span')
    images = soup.select_one('#poster_link > img')

    d1 = {}
    for name in names:
        name1 = name.get_text()
        d1['name'] =name1

    for rating in ratings:
        rating1 = rating.get_text()
        d1['rating'] = rating1

        
    for info in infos:
        info1 = info.get_text()
        d1['info'] = info1

    for image in images:
        image1 = image.get('src')
        d1['poster']= image1

##    for review in reviews:
##        review1 =review.get_text()
##        
        d1['review']= reviews

    for date in dates:
        date1 = date.get_text()
        d1['date']=date1
    print(d1)
##

    #content-column > div:nth-of-type(5) > div:nth-of-type(2) > div:nth-of-type(1) > div.poster_container > a
    #content-column > div:nth-child(5) > div.mb-movies > div:nth-child(1) > div.poster_container > a
#content-column > div:nth-child(5) > div.mb-movies.list-view > div:nth-child(2) > div.movie_info > a
