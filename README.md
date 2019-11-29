# EventTracker
Mange Events
---

Django 2.0 Project (with GraphQL)


# Basic Instructions

* clone repo
* `git clone https://github.com/hirokgreen/event-tracker event_tracker`
* `cd event_tracker`

* create virtualenv with python3 using virtualenvwrapper or virtualenv 
(follow https://virtualenvwrapper.readthedocs.io/en/latest/)

with virtualenvwrapper -

* `mkvirtualenv -p python3 event_tracker` (next time only activate env by typing `workon event_tracker`)

* Install all the **requirements** using `pip install -r requirements.txt`
* Complete the migrations. `python projectile/manage.py migrate`
* Start the server. `python projectile/manage.py runserver`
* The server should be up and running in `http://127.0.0.1:8000/graphql/` :smile:
* create super user via `python projectile/manage.py createsuperuser`
(for authentication while mutation you might need authentication credential)
