# Data Centric Development - Code Institute Milestone Project Four - Matt Inglis

## *Sound Emporium - A fully function musical instrument store built using Django, with payments supported by Stripe.*

![Image of Site Concept](https://i.imgur.com/fDqjNJx.png)

## Deployed link via Heroku: https://ms4-sound-emporium.herokuapp.com/

# Overview

The mission of Sound Emporium is to provide a clean, hassle-free ecommerce experience for shoppers looking to browse a selection of musical instruments and equipment, displayed in a neat and initutive manner. 

In addition, the site has secure user account creation by way of Django AllAuth, allowing users to login to safely store their private information, leave reviews of products, and comment on the site's blog feed.

# UI/UX

The wireframe for this site can be found in the README_assets directory of the repository or at [this link.](https://github.com/mattingliscoding/code-institute-milestone-project-four/blob/master/README_assets/UXPin-Matt_Inglis_MS4___Code_I.pdf)

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
The site was extensively tested on a range of devices and screen-sizes, and was regularly tested during development, using Google Chrome DevTools.

## Debugging
Extensive debugging was done throughout development of the site, mainly using Chrome DevTools to fix UI issues, and GitPod CLI to debug issues with the Python/Django code.

# Deployment and Cloning

## Deployment
This site is deployed on Heroku, using a free account. To set up my project for deployment on Heroku, I followed this process:
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

## Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install the gunicorn, psycopg2 and dj_database_url packages to your local environment, as they are required to deploy a Django project on Heroku.
2. Create a requirements.txt file and freeze all the modules with the command `pip3 freeze > requirements.txt`.
3. Create a Procfile containing `web: gunicorn boutique_ado.wsgi:application` in the file.
4. Push the changes to GitHub.
5. Go to Heroku and create a new app.
6. In the add-ons area of the app dashboard, search for Heroku Postgres and enable it.
7. It must be ensured that the config vars in Heroku correspond to those in your settings.py.
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`
11. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
12. The database settings in Django need to be as follows to ensure the right database is being accessed and the correct server is hosting the project.
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

```
ALLOWED_HOSTS = ['ms4-sound-emporium.herokuapp.com', 'localhost']
```

## Local Deployment
For local deployment: 

In order to clone this repository, to work on the code yourself, please follow these steps:
1. On the GitHub main page of the repository, above the file-list click on the 'Code' button, with the download symbol.
2. In the HTTPS tab, click the clipboard symbol to copy the clone URL.
3. On your system, open your terminal.
4.Change the current working directory to the location where you want the cloned directory.
5. Type `git clone`, and then paste the URL you copied earlier.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
6. Press Enter to create your local clone.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
7. Install required modules from the requirements.txt: 
```
pip install -r requirements.txt
```
8. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
9. Install all the required packages with `pip3 install -r requirements.txt`
10. Migrate the models to your IDE database with `python3 manage.py makemigrations` and `python3 manage.py migrate`
11. Load the data into the database using:
`python3 manage.py loaddata <fixture_name>`
12. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
13. Run the app using `python3 manage.py runserver`

# Credits
## Content, Media and Credits
* I took heavy inspiration from the Boutique Ado project from Code Institute as well as [Gear4Music](https://www.gear4music.com/) and [GuitarGuitar](https://www.guitarguitar.co.uk/) for aesthetic choices on the site. 
* Credit must also be given to [this](https://djangocentral.com/building-a-blog-application-with-django/) article that I referenced for the Blog App, and [this](https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a) article I used for the review function.
* Stock photos taken from [Unsplash](https://unsplash.com/) and the Gear4Music product pages.






