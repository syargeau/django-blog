# Django Blog Engine
What is my goal with this project? Primarily, I am creating a simple blog engine in Django for open-source use. Afterwards, I can transform my current site (www.motonowblog.com) to use this engine, hence making it easier to expand the site with future projects down the road (a.k.a. no more restrictions from Wordpress capabilities!)
## Getting Started
Biggest thing to note: this is an in-progress project! At any time in the development process I might have failing functional tests in the Master branch (yep, not an ideal use of Git, but this is just for fun! Cringe away).
### Containerize Using Docker
I want to fully containerize this project using Docker so that it's easy to deploy to a live staging and production server. I am still figuring out the best way to develop within Docker... so stay tuned! (more Docker instructions to come).
### Development
At the very least, we can ignore Docker for now and get started locally. That will require the user to manually install Python 3.6, Django, and Selenium at the very least.
Once these are installed, we can develop tests and see our site in progress through the provided Django `mangage.py`.
To get a Django server up on a local port, run:
```
python manage.py runserver
```
To run functional tests:
```
python manage.py test functional_tests
```
And to run unit tests:
```
python manage.py test blog
```
Enjoy! Feedback is always welcome and appreciated.