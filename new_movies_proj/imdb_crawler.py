import requests
import lxml
from lxml import html

# download photo
# f = open('00000001.jpg','wb')
# f.write(requests.get('http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_UY209_CR0,0,140,209_AL_.jpg').content)
# f.close()


class MovieCrawler(object):
    '''

    '''

    def __init__(self, movie_url):
        '''
        '''

        self.url = movie_url

    def __get_page_content(self):
        '''
        '''

        response = requests.get(self.url)

        # Check status code
        if response.status_code != 200:
            print('There is something wrong with the connection to the page')
            return

        # convert page content to lxml object
        root = lxml.html.fromstring(response.content)
        list_detail_node = root.find_class('list detail')
        nodes = root.xpath('//table[@class="nm-title-overview-widget-layout"]')

        movie_list = list()
        for html_elem in nodes:
            # get only the part where the movie overview details are
            overview_row = html_elem.xpath('tbody/tr')[0]
            movie_list.append(self.__get_movie_overview_details(overview_row))
        return movie_list

    def __get_movie_overview_details(self, parent_elem):
        '''
        '''

        # Get the movie poster url
        img_src = parent_elem.xpath('td[1]/div/a/div/img/@src')[0]

        # Get the movie title
        movie_title = parent_elem.xpath('td[2]/h4[@itemprop="name"]/a/text()')[0].strip()

        # Get the IMDB rating
        imdb_rating = 'Not Available'
        rating_node = parent_elem.xpath('td[2]/div[@class="rating_txt"]/div/strong')
        if rating_node:
            imdb_rating = rating_node[0].xpath('text()')[0] + '/100'

        # Get movie description
        description = parent_elem.xpath('td[2]/div[@itemprop="description"]/text()')[0].lstrip()

        return (img_src, movie_title, imdb_rating, description)

    def get_upcoming_movies(self):
        '''
        '''
        return self.__get_page_content()


if __name__ == '__main__':
    imdb = MovieCrawler('http://www.imdb.com/movies-coming-soon/')
    print(imdb.get_upcoming_movies())