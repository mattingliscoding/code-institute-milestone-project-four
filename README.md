# Data Centric Development - Code Institute Milestone Project Four - Matt Inglis

## *Sound Emporium - A fully function musical instrument store built using Django, with payments supported by Stripe.*

![Image of Site Concept](https://i.imgur.com/fDqjNJx.png)

## Deployed link via Heroku: https://ms4-sound-emporium.herokuapp.com/

# Overview

The mission of Sound Emporium is to provide a clean, hassle-free ecommerce experience for shoppers looking to browse a selection of musical instruments and equipment, displayed in a neat and initutive manner. 

In addition, the site has secure user account creation by way of Django AllAuth, allowing users to login to safely store their privat information, leave reviews of products, and comment on the site's blog feed.

# UI/UX

The wireframe for this site can be found in the README_assets directory of the repository or at [this link.](https://github.com/mattingliscoding/code-institute-milestone-project-four/blob/master/submission_assets/matt-inglis-ms3-wireframe.pdf)

The UI/UX process for Sound Emporium was in the mindset of simplicity and functional ease-of-use. Much of the site is built from very common Bootstrap parts that I have customised to my own theme. 

The framework for Sound Emporium has much of it's roots and inspiration in the Module from prior to the Project, the Boutique Ado mini project. The backend, AllAuth, and much of the simpler templates were built in conjuction with the content of this module, as I felt it lent itself greatly to the style I was going for.

# Database

There are a few iterations of the data for Sound Emporium
* In the developement stage of the project, the data is hosted in a SQLite3 database that is provided as standard by Django.
* In the Deployment stage, to Heroku, the SQLite3 data is loaded into a PostgreSQL database, which is utilised as an add-on in Heroku.
* Amazon Web Services S3 Product hosts the deployed Media and Static (CSS/JS) files for the project in their 'Bucket' functionality.

I have provided a Entity Relationship Diagram for reference as to the structure and relationships of the dataset that Sound Emporium uses. I created this using [Creately](https://app.creately.com/diagram/mgQb21pkcWK/edit). 

![Image of database graphic](https://i.imgur.com/rYV6Oau.png)


# Features
* **Navigation bar, with brand and page links (All pages)** - This header was created using Bootstrap, and provides the user with a clear point of navigational input. The collapse feature from Bootstrap also features heavily across the site, helping to keep the site expandable and accessible on smaller screens.
* **Home Page - Carousel** - Gives the landing page a sense of dynamics and movement, as well as large CTA buttons drawing the eyes to the links to purchase products.
![Screenshot of carousel](https://i.imgur.com/j6BsHez.png)
* **Products Page - Cards** - The responsive and fluid card deck that the Products screens uses is efficient, clear and doesn't get bloated or fatiguing to use on smaller devices. 
![Screenshot of cards](https://i.imgur.com/REraAGO.png)
* **Products Details Page - Basket Preview** - When adding a product to the basket from anywhere on the site, the customer is greeted with a useful information pop-up that outlines their addition, other items in the basket, and their current sub-total left to pay.
![Screenshot of basket](https://i.imgur.com/EOuAFS6.png)
* **Products Details Page - Reviews** - This section allows the customer to leave their thoughts (on the condition they sign in/sign up) on a product and those without an account can see at a glance if the product they are interested in has garnered any comments from other musicians, and therefore they can make a more informed decision.
![Screenshot of reviews](https://i.imgur.com/6nAYIvp.png)
* **Blog Page** - The list of blogs written by Sound Emporium is neatly and cleanly arranged, with card showing the title and an image to immediately give context to the browsing user.
* **Blog Page - Comments** - In a similar design vein to the Reviews, the comments feature on the Blog app allows users to engage in the discussion and become part of a community. In time, if this was a non-academic venture, I would heavily invest time turning this into a forum/social network area of the site, and build on the community aspect.
![Screenshot of comments](https://i.imgur.com/jfP6g2H.png)

# Future Features 

There are a few features I feel that I would like to add in the future, or some that I would want to improve upon:
* I would in the future make an area on the homepage displaying currently on-sale products, rather than the simple landing page I opted for. 
* The reviews portion is built inside the Products App but I think I would prefer to have created it as it's own Django App as I ran into limitations in the process of writing the views.
* I would like to add more functionality to the user on their profile page such as customisable Usernames, and more options for their account security.

# Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/ie)
- [Bootstrap](https://getbootstrap.com/)
- [Material Color Tool](https://material.io/resources/color/#!/?view.left=0&view.right=0)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

# Testing

## User Stories & Feature Testing

- [Here](https://github.com/mattingliscoding/code-institute-milestone-project-four/blob/master/README_assets/MS4%20User%20Stories%20-%20Host%20Stories.pdf) is a look at my User Stories document from the start of the Sound Emporium project:

### Bugs Encountered/Fixed & Known Issues
* **Expected** - As a user of Sound Emporium I would like to see a list of all products, to select which ones I would consider purchasing.
    * **Testing** - Possibly the most prominent issue I had with the development of the project came when having to move the data from the local SQLite3 database to the Heroku PostgreSQL one for deployment. Since I did not use fixtures in production (I created each product in the Django Admin panel), I had to do a manual data dump from SQLite3 using 
    
        ```
        python3 manage.py dumpdata
        ```

        Following this with a loaddata command caused errors linking to built-in Django models. Eventually, with the help of tutor support, we managed to get the data migrated by creating a separate .json file for the models that were causing the issues. 
        One technique that especially helped with the trial and error process was putting Print statements in my settings file to ascertain which database was being accessed when the site was launched. 
        ![Screenshot of comments](https://i.imgur.com/x9VzWry.png)

    * **Result** - The user is able to access all the data that can be hosted by either local or deployment phase databases.
* **Expected** - As a user, I would like to leave reviews on products for future prospective customers.
    * **Bug Encountered/Testing** - I encountered a frustrating bug whereby the Bootstrap 'collapse' elements that I wanted to reveal the Review form were performing very inconsistently. However the more I tinkered the form's appearance became even more sporadic, even when the Bootstrap class was not used. The solution for me, given time constraints, became to get it to the best possible place where it would perform every time. This now involves a user pressing the add review button, and the form showing but appearing as if the user has tried to submit empty fields. However the form does work, and the product detail page is now updating with the newly-created reviews.


## Code Validation
All HTML/CSS files for the site were formatted using [this free online formatter](https://www.freeformatter.com/html-formatter.html), then validated via [W3C Markup Validation Service](https://validator.w3.org/). 

This produced some unavoidable errors that occur as part of using templating language, however I did endeavour to clean up as many as possible.


## Browser Support and Functionality
Manual testing of the site's pathing and responsive-ness has been done by myself across multiple screen sizes and browsers.

The site was tested and working in several browsers; Google Chrome, Mozilla Firefox, Apple Safari and Microsoft Edge.

## Responsive Design Testing
The site was extensively tested on a range of devices and screen-sizes, and was regularly tested during development, using Google Chrome DevTools. The range of responsive design can be seen in the prototype image at the top of this document but I will also include some screenshots from DevTools here from testing:

![Site on Phone display](https://i.imgur.com/9vjYgVDl.png)

![Site on Tablet display](https://i.imgur.com/FUH9cY7l.png)

![Login on Phone display](https://i.imgur.com/329ksSTl.png)

## Debugging
Extensive debugging was done throughout development of the site, mainly using Chrome DevTools to fix UI issues, and GitPod CLI to debug issues with the Python/Django code.

# Deployment and Cloning

## Deployment
Dungeon Club is deployed on Heroku, using a free account. To set up my project for deployment on Heroku, I followed this process:
* A new requirements.txt file is needed and can be generated using 
``` 
pip freeze > requirements.txt
```
* Create a new file named Procfile (the capital P is crucial!) with no file extension, add the following to the file and save.
``` 
web: python app.py
``` 
* Login to/create account on Heroku and navigate to 'Create New App' on the dashboard.
* Fill in the details for the new app, and select a server. 
* Once created in Deploy > Deployment Method select GitHub and connect to the app GitHub repo.
* The environment variables for the project are entered on the app settings. These include the MONGO_URI, and SECRET_KEY.
* Navigate to the 'Deploy' section, and from that menu, link the existing GitHub repo master branch to the Heroku app and enable automatic deployment.

# Deployment
## Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.
- [gnicorn](https://gunicorn.org/): `gnicorn` is Python WSGI(web server gataway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
2. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
3. Create a `Procfile` write `web: gunicorn boutique_ado.wsgi:application` in the file.
4. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
5. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
7. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key | Value |
| ----------- | ----------- |
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `True` |

* I used [Djecrety](https://djecrety.ir/) to generate Django Secret Key.

8. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.
```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`
10. Load the data fixtures(color_table, flower_table, image_table, product_table) into the Postgres database using the following command:
`python3 manage.py loaddata <fixture_name>`
11. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
12. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
13. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
14. Add `'flowerydays.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
```
ALLOWED_HOSTS = ['flowerydays.herokuapp.com', 'localhost', '127.0.0.1']
```
15. In Stripe, add Heroku app URL a new webhook endpoint.
16. Update the settings.py with the new Stripe environment variables and email settings.
17. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.

### Amazon Web Service S3
The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting.
I used CORS configuration below:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py
1. Install `boto3` and `django-storages` with a command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.
```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'flowerydays'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Add [custom_storages.py](https://github.com/AsunaMasuda/FloweryDays/blob/master/custom_storages.py).
6. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
7. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS (S3 bucket), Gmail

1. In the IDE you are using, copy and paste the following commane into the terminal to clone this repository.
    `git clone https://github.com/AsunaMasuda/FloweryDays.git`
(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. Load the data fixtures(color_table, flower_table, image_table, product_table) into the database using the following command:
`python3 manage.py loaddata <fixture_name>`
6. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
7. Now you can access the app using the command `python3 manage.py runserver`

# Credits
## Content, Media and Credits
Much of the assets and content was provided via the [Dungeons and Dragons Fan Site Kit](https://dnd.wizards.com/articles/features/fan-site-kit), such as many of the banner images, and of course the data from the SRD Document was also courtesy of Wizards of the Coast LLC.

The sidebar menu for the 5th Edition Database page was inspired by/is a heavily customised version of [this brilliant code snippet on CodePly](https://www.codeply.com/go/3e0RAjccRO/bootstrap-4-collapsing-sidebar-menu) by Skelly.

Articles and images linked on Dungeon Club Homepage:
* https://allthingsdnd.com/amazon-prime-orders-2-seasons-for-critical-role-the-legend-of-vox-machine/
* https://io9.gizmodo.com/joe-manganiello-takes-the-internets-toughest-and-most-f-1845873249
* https://arstechnica.com/gaming/2020/12/dungeons-dragons-linked-to-new-movie-starring-chris-pine/

Some additional Google Image searching was required for the card images on the Resources page, however the majority was simply the image file hosted on the Amazon listing for the product.






