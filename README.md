### About application
This application is intended for managing data of our [Django-app](https://github.com/prathamlahoti/django-app). The backend of the application is written in Python, using [Django Rest Framework](https://www.django-rest-framework.org/). This API has user interface, and it allows users to not only use command-line interface, but also web-interface. Any user can add categories and tags, for posts and easily manage them. However, only authenticated to the API authors of created posts can manage them. Guests are allowed to only view these posts. Now our API has 3 available routes:
1. /posts
2. /categories
3. /tags

_posts route is a standart one._

**To authorize to the API you must be authenticated to the site, for which the API was created**.

---
### Deployment
I assume, that your working machine has installed Python3.6 or higher so we must create the working virtual environment. I prefer using Pipenv. If you're using default virtual environment, anyway the applciation dependencies will be install from _requirements.txt_. In case of using Pipenv, you could easily install them from Pipfile. Once dependencies install, you need to create your custom _.env_ file, where all your secret information will be stored. In our API, we store application's **SECRET_KEY** and **DATABASE_URI** as secret data. You must specify your secret data the same way. 

Once you set up your settings, the application will be ready to be ran by standart django running procedure by typing `python manage.py runserver`. Follow the given link and the app web-interface will be displayed for your usages.

Until now, you'd better use web-interface, beacause API schema has not been created yet. So you may face with lots of confusing moments, working with command-line inteface. Also in the near future, the API will be containerized and it will be ran from the docker container. I'm currently working on these components. These updates will be available soon.
