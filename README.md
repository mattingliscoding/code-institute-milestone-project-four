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
* **Expected** - As a user of Dungeon Club, I would like to quickly navigate through the 5E Lookup menu to pull up the information I need for my game.
    * **Testing** - Initially, the cascading drop-down had issues with regards to the growing complexity of the id's and data-targets required by the Bootstrap Collapse functionality. The submenus were all the same width and the menu drop-down headings were not coloured to differentiate. The menu system fast became unwieldy and was slightly fatiguing for a user.
    * **Result** - User is able to navigate using the drop-down menu on desktop (left of screen) and mobile screen (top of screen) sizes and select the entry they wish to have displayed. The fix to clean up the UX of the menu was to use a highlighting colour for the menu category that the user has opened, and the sub-menus decreasing in width the further down through the menu structure the user goes.
* **Expected** - As a user, I would like the process of making an account be simple and secure.
    * **Testing** - Werkzeug Security provides safe hashing for password protection and therefore, when a new user clicks the register button and fills in the information, their account is created in the MongoDB users collection complete with secure password.
    With regards to secure account deletion, the session functionality from Flask allows for easy removal of accounts using a function that checks the session.user is correct and they are allowed to continue with the account deletion:
        ```
        def delete_account():
            if session.get('user'):
                username = mongo.db.users.find_one(
                    {"username": session["user"]})["username"]

                return render_template("delete_account.html", username=username)

            return redirect(url_for("login"))
        ```
        When the user confirms their deletion request on the subsequent page, the following code (session.pop()) ensures that the user is removed from the browser cache. This further protects the user's information. 
        ```
        @app.route("/account/delete-confirm", methods=["GET", "POST"])
        def delete_account_confirm():
            mongo.db.users.remove({"username": session["user"]})
            flash("User Deleted")
            session.pop("user")
            return redirect(url_for("register"))
        ```
* **Expected** - As a user, I would like to have a place to store characters I've made for various games I've been a part of. I would also like to be able to keep a to-do list/log of current missions and quests I have undertaken during my games.
    * **Testing/Bug 1** - I experienced a visual bug whereby a user would expand their character card in order to use the EDIT function. The nature of the Bootstrap Collapse functionality and my usage of it meant that all the character cards at once would extend down the page rather than just the one in use. 
    * **Result** - In order to rectify this, improve UX and also to create a much more familiar process for web form submission, I implemented Bootstrap Modal pop-ups instead for the editing of both Character and Quest items. This is a great improvement to this feature. You can see the results in this image: 
    ![Modal popup example](https://i.imgur.com/U7AGxnz.png)
    * **Testing/Bug 2** - Another issue with the Character feature was the inclusion of the HTML tables in the card deck to display stats. The table was extending out of the bounds of the card and pushing whitespace out to the right hand side of the screen, which of course looked terrible and needed a suitable fix. 
    * **Result** - To fix this, I needed to utilise the CSS property ```overflow-x:auto;``` and set it to a table container class for use across the site (I encountered a similar problem on the article text on the Lookup page which has many sets of stats in tables). This allowed the table to have its own horizontal scrollbar and the card deck kept a uniform dimensions across different screen resolutions. This can be seen in this screenshot:

        ![Scrollable table example](https://i.imgur.com/0StKmYi.png)
    * **Testing/Bug 3** - The most prominent issue found with the Character and Quest features was an oversight in my UX. Upon trying to edit their entry, the edit form did not contain their previously entered values. The edit form simply had blank inputs with placeholder text, similar to the Add Character form, except with a different route/function connected to the Submit button.
    * **Result** - To rectify this glaring UX issue, I found that the answer was frustratingly obvious. For the forms on the page, Jinja for/if loops are used to loop through any characters or quests found in the database and then ascertain if they belong to the user stored in the session cache. If this is found to be true, then their items data is populated onto the cards. The editing and deleting of these items is then handled by using each Character or Quests specific unique ID that is generated and assigned to it by MongoDB. Using this in the Jinja language of the HTML allowed me to ensure that the correlating values were being edited and also to replace ```placeholder="{{ character.character_name }}"``` with ```value="{{ character.character_name }}"```.
    
        Here is a sample of code for one of the edit form inputs that would demonstrates how the HTML is now written to display the stored values that are to be edited by the user:
        ```
        <form method="POST" action="{{ url_for('edit_character', character_id=character._id) }}">
            <div class="form-group">
                <label class="fancy-font" for="character_name">Character Name</label>
                <input name="character_name" type="text" class="form-control form-item"
                    id="edit_character_name{{character._id}}" value="{{ character.character_name }}" required />
        </form>
        ```
        In addition, here is a screenshot where you can see in the edit form modal the stored values that match the ones from the original card on the site behind it:

        ![Edit functionality example](https://i.imgur.com/URuESLH.png)




## Code Validation & Known Errors
All HTML/CSS files for the site were formatted using [this free online formatter](https://www.freeformatter.com/html-formatter.html), then validated via [W3C Markup Validation Service](https://validator.w3.org/). The W3C check did spring some errors in the code but when checked through, they were all as a result of the bad functionality for validating Jinja Templating language, and any other errors were rectified.

* RESUBMISSION NOTE JAN 2021 - I have since ran the rendered HTML code through the validators and not the template code, and have checked thoroughly that no errors remain as a result of the Jinja templating. 

The app.py Python file was checked and verified as completely PEP8 compliant, using [this checker](http://pep8online.com/checkresult):
![Python pep8 screenshot](https://i.imgur.com/wAYKNJsl.png)
## Browser Support and Functionality
The site was tested and working in several browsers; Google Chrome, Mozilla Firefox, Apple Safari and Microsoft Edge.

All site links, internal and external have been manually checked and tested thoroughly and no errors were found as a result of bad pathing.

## Responsive Design Testing
The site was extensively tested on a range of devices and screen-sizes, and was regularly tested during development, using Google Chrome DevTools. The range of responsive design can be seen in the prototype image at the top of this document but I will also include some screenshots from DevTools here from testing:

![Site on Phone display](https://i.imgur.com/9vjYgVDl.png)

![Site on Tablet display](https://i.imgur.com/FUH9cY7l.png)

![Login on Phone display](https://i.imgur.com/329ksSTl.png)

## Debugging
Extensive debugging was done throughout development of the site, mainly using Chrome DevTools to fix UI issues, and Werkzeug to debug issues with the Python/Flask code and routing.

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

## Cloning this project
In order to clone this repository, to work on the code yourself, please follow these steps:
* On the GitHub main page of the repository, above the file-list click on the 'Code' button, with the download symbol.
* In the HTTPS tab, click the clipboard symbol to copy the clone URL.
* On your system, open your terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
* Press Enter to create your local clone.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
* Install required modules using the requirements.txt using: 
```
pip install -r requirements.txt
```
* Create a .env file and add the following variables to it, PORT, IP, MONGODB_URI, SECRET_KEY and give them their needed values.
* Run your app with 
```
python3 app.py
```

# Credits
## Content, Media and Credits
Much of the assets and content was provided via the [Dungeons and Dragons Fan Site Kit](https://dnd.wizards.com/articles/features/fan-site-kit), such as many of the banner images, and of course the data from the SRD Document was also courtesy of Wizards of the Coast LLC.

The sidebar menu for the 5th Edition Database page was inspired by/is a heavily customised version of [this brilliant code snippet on CodePly](https://www.codeply.com/go/3e0RAjccRO/bootstrap-4-collapsing-sidebar-menu) by Skelly.

Articles and images linked on Dungeon Club Homepage:
* https://allthingsdnd.com/amazon-prime-orders-2-seasons-for-critical-role-the-legend-of-vox-machine/
* https://io9.gizmodo.com/joe-manganiello-takes-the-internets-toughest-and-most-f-1845873249
* https://arstechnica.com/gaming/2020/12/dungeons-dragons-linked-to-new-movie-starring-chris-pine/

Some additional Google Image searching was required for the card images on the Resources page, however the majority was simply the image file hosted on the Amazon listing for the product.






