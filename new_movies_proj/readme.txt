This is a simple web app which shows a list of upcoming movies.
The list of upcoming movies was retrieved by crawling through imdb site (http://www.imdb.com/movies-coming-soon/).


1. Please run the django built in web server
using this command:

python manage.py runserver

2. The upcoming movie list can be access through:

localhost:8000/new_movies/

3. The admin page is available at:

localhost:8000/admin/

username: admin
password: p@ss1234

The admin account can add/update/delete movies from the list.


4. The imdb site crawler (http://www.imdb.com/movies-coming-soon/) is the imdb_crawler.py.

5. The crawled items are stored in db.sqlite3.

6. The items crawled were saved to the database using the populate.py script.

Thank you!

