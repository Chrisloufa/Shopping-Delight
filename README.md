# Shopping Delight

![Responsive](media/readme/amiresponsive.png)

Shopping delight is a retail e-commerce site to allow users to easily browse different clothing products with categorisation or even through personalized searches to make the process smoother. Users are able to sign up to have individual profiles and save their user information.

The site is fully responsive and designed in a simplistic and easy to navigate manner. It has been coded using HTML, CSS, JavaScript, Python and Django and the Bootstrap frameworks.

# User Experience

Link to Kanban board can be found here [https://github.com/users/Chrisloufa/projects/2/views/1](https://github.com/users/Chrisloufa/projects/2/views/1)

## Strategy

This website is for a Business to Consumer (B2C) business that sells clothing products.

Customers who visit the site will be able to:

- Easy to Navigate and filter/search by category.
- Has the ability to view and purchase items.
- Has an email subscription service.
- Has links to Social Media sites Facebook and Instagram.
- User Account functionality, to keep track of order history and store delivery information.

And the owner of the site will be able to add:

- Appealingly displays their products.
- Allows them to add, edit and remove products.
- Allows customers to get in contact if required.

# User Stories

- As a **Shopper** I can **view a list of product** so that **I can choose what to buy.**
- As a **Shopper** I can **sort the list of available products** so that **I can easily identify the best rated products and best prices etc.**
- As a **Store Owner** I can **add a product** so that **I can add new items to my store.**
- User can view lists of items for sale and search by name, filter by price.
- As a **Site User** I can **easily register for an account** so that **I have a personal account and. can view my profile.**
- As a **Shopper** I can **easily select the size and quantity of a product when purchasing it** so that **I can ensure that I do not accidentally select the wrong product, quantity or size.**
- User can signup/login/logout.
- User can add items to shopping cart and the app remembers it next time you login. User can view all the items in their shopping cart. User can delete items in the shopping cart. Shopping cart uses an integer column to store "state".
- User can fill in form and submit billing info. After submitting billing info, items in the shopping cart will move to a different "state".

![Kanban](media/kanban.png)

# WireFrames

## Desktop Wireframes

<details>
<summary>Desktop Wireframes - Click Here:</summary>
<img src="media/readme/wireframes/desktop-index.png" width="500">
<img src="media/readme/wireframes/desktop-products.png" width="500">
</details>

## Tablet Wireframes

<details>
<summary>Tablet Wireframes - Click Here:</summary>
<img src="media/readme/wireframes/tablet-index.png" width="500">
<img src="media/readme/wireframes/tablet-products.png" width="500">
</details>

## Mobile Wireframes

<details>
<summary>Mobile Wireframes - Click Here:</summary>
<img src="media/readme/wireframes/mobile-index.png" width="500">
<img src="media/readme/wireframes/mobile-products.png" width="500">
</details>


# Design

The colour scheme was selected to be cool and basic as to not take the focus away from the content that is important on the screen.

## Colour Scheme

The colour scheme was kept clean to keep the focus on the products on the site. Also looks modern and contemporary.
The body uses black(rgb(0,0,0)) to keep writing clear and easy to read on a white (rgb(255,255,255)) background. All main function buttons and the website logo uses Blue (#007bff) to stand out from the rest of the webite, this makes it easy for the user to be aware of what buttons they can interact with.

Here you can see a color palette:

<p align="center">
<img src="media/readme/color-palette.png" width="500">
</p>

## Font Choice

I chose the Google Font Raleway to act as the primary font for the website, including for the logo. It provides a nice clean and clear style without any readability problems - a vital design feature for any website. This is available for free via [https://fonts.google.com/]. Sans Serif is used as a secondary option in case of failure to load the font into the website correctly. 

There are some stylistic changes to the font (the use of <strong>), but mostly with just colour changes for impact, attention or contrast and readability purposes.

# Database

## Database Schema

<p align="center">
<img src="media/readme/databaseschema.png">
</p>

It shows each model present in the project and the relationship between them.
This schema is vital in developing the website's functionality, its features and what users are capable of doing.

# Features

## Custom User Model
To capture additional user information, such as address, I opted to override the default Django user model and create a custom one. This enabled me to store all the necessary user data in one object. It will also make any future user model changes easier to make.

Given the additional data input requirements, I had to specify custom forms in order to capture all the required information. This included overriding Django default forms, for example, the admin forms for adding/modifying user details.

## Accounts
This is where all customer information is retained via the custom user model. I also made the decision to use Django-allauth which added the ability to override the username field, using the email address as the login. It also brought with it the ability to verify email addresses and reset passwords.

Within this app I have overriden a number of the default forms provided by allauth to integrate with the customer user model. To produce responsive forms I have used the django-crispy-forms helper function which allows me to create custom form layouts with individual element styling. I have also modified the rendering of the django admin site for the user object, to provide a better structure.

Outlined below are the views that are produced by this app:

a) **Signup:** a custom form used to create a new user account with the custom user model. The username field is removed, with the email address used in it's placed. Given this is an ecommerce application, it made more sense to proceed with email only, as a username would not serve any other function than to login.

b) **Login:** Enables users to login using their email address and password. If any products exist in a user's basket before they login, these will be merged into any existing basket when the user logs in.

c) **Logout:** Enables users to logout of their account. The user will be asked to confirm they wish to logout of their account, this prevents accidental logout. When a user logs out any items added to their basket will no longer be visible, however, the basket will be stored in the account and visible upon login.

d) **Profile - Personal Details:** The user can update their billing address from here. I made the decision to only allow billing address to be changed here for security, so that a user can only use payment cards for one billing address. The billing address is passed through to Stripe upon payment processing. When updating details the user will be provided with feedback flash messages to give a more interaction experience and confirm to the user if an update took place or not.

e) **Profile** - Change email: A user can have multiple emails if they wish, this functionality is leveraged from django-allauth. The user can log in with all email addresses under their account. I decided to include this functionality to enable users to have one householder account if they wish.

f) **Profile - Change password:** For security, a user must provide their current password alongside a new password before it will be accepted and updated.

## Basket
The Basket app is made up of two models, Basket and BasketItem. The Basket model is used as a container and linked to a user account. BasketItems are then linked to the Basket, via a Many-to-One relationship (i.e. one basket can have many items). The BasketItems record what products a user has added to their basket and the quantity of each (up to a maximum of 5 for each product).

Given this is an ecommerce application, the basket is a critical component of the application's functionality. It enables anonymous users to create a basket of items, this will be automatically linked to their account/merged with an existing basket upon account login. Users can access their basket at any time to add/update/remove items.

When a basket contains at least one item, the basket icon will display the total item count, to enable the user to keep track of contents without having to click into the basket.

There are a number of components to the basket app, which I have outlined below:

a) **Add to Basket:** This view is used to add items to the Basket object. If a Basket object does not yet exist it will be created and the product added as a related BasketItem object. Products are automatically added with a quantity of 1, which can be updated in the basket view.

This view will only accept valid product IDs. To prevent accidentally adding the wrong products, the product object ID has been changed to use a UUID.

Feedback flash messages are provided to the user when a product is successfully added, and when adding an item will result in it exceeding the maximum permitted single-item quantity.

b) **View/Update Basket:** This template makes use of the Django inline formset factory functionality, this enables the updating of multiple database objects at once through a single form. I have setup the form to permit the user to change product quantity and/or remove a product.

Feedback messages are provided to inform the user whether the basket update was successful or not.

c) **Customised Admin Functionality:** Given the relationship between Basket and BasketItem, I have amended the admin view so that when accessing a basket, the contents (basketitems) will be displayed with it. The contents can be modified.

d) **Create Order:** The Basket model also contains a helper method which is used to 'convert' a basket into an order. This is only called once payment has been verified. This will be discussed further under the Checkout app.

## Checkout
The Checkout app is used to process an order and can only be accessed when a user is logged in with at least one item in their basket. This process captures the user's billing address (from user object) and shipping address (pre-populated from user object address) which is modifiable. Prior to processing payment, the user is asked to review and confirm their order, with payment processing handled by a third-party payment processing service, Stripe.

The models for this app have a similiar structure to that of the Basket app, Checkout and CheckoutItem, the difference in this instance, is that more information is captured. An important distinction is the additional of an Order status field AND an OrderItem status field, enabling site admins and users to clear understand the status of relevant orders. Prices are also saved, as user's are charged at a point-in-time, whereas, product pricing may fluctuate overtime.

The BasketItem object is converted to CheckoutItem, with each CheckoutItem representing a single-item (quantity=1), so if a BasketItem has a quantity of 5, this will result in the creation of 5 CheckoutItems. This enables me to individually handle each item of a user's order, i.e. I can provide status against each item, for example, the stock for a product = 2, but the user ordered 3. I can ship those which I have, updating them to reflect this, and ship the third item when it becomes available.

This app is made-up of the following key components:

a) **Process Order:** This is a view that combines two forms, user shipping and billing details, and the Stripe payment form. The forms are customised using django-crispy-forms with custom kwargs passed-through.

The structure of the form has been designed to capture the required user details, before displaying a summarised version of the user's order, with the payment form only being displayed once the user has confirmed their order.

The payment form is handled using Stripe v3 with a combination of JavaScript (JS) and server-side rendering. Once the payment has been made, a custom JS function adds a hidden field to the form, before posting the form. With the POST request, the serverside verifies the token using Stripe's PaymentIntent API. If there were any user related issues, for example, declined card, this will be fedback to the user.

Once the payment is verified through Stripe the Basket model create_order method is called - see below for further detail.

d) **Basket create_order() method:** This creates an Order object, using the information captured from the billing/shipping details form and the user's Basket Object - note: no information is stored from the payment form, other than a token reference for verification. All BasketItems are converted to OrderItems, with each OrderItem representing a single-item, i.e. quantity of 1.

Given that this process is only called once payment has been updated, the status of the Order is set to PAID. This is not the default status because an admin could manually create a new order without payment having been received.

d) **Customised Admin Functionality:** Given the importance of clearly understanding order pipeline, the admin area has been heavily customised. OrderItems are displayed as part of the Order (as with BasketItems in Basket).

Focus has been placed on ensuring that admins are able to clearly identify the status of orders upfront, hence the list view includes an editable order status. When viewing the detail of a specific order, each order item also contains a similiar breakdown, clearly detailing status of each individual item.

The aforementioned customisations have been made with workflow management in mind.

## Products
The Products app provides the majority of the application's functionality. It delivers this through two models, Product and Review.

The Product model enables the site administrator to add/edit/remove products, with custom templates (i.e. outside Django Admin), providing a layer of seperation, with only staff given permission to do so. For example, if a member of staff only needs to add/edit/remove products, they can be given the individual permissions to these functions and access them from the front-end website, they do not need access to the Django Admin area.

From the front-end user perspective, this app provides the views and templates to list the products and enable the user to interact with them. It also enables users to add reviews for products.

The functionality of this app is detailed below:

a) **is a Add/Edit/Remove Products from the Front-end:** Custom views have been written to enable staff to perform CRUD functions from the main website. If the user has the required permission admin functionality will appear throughout the product areas, for example, on a product detail view they will be presented with a dropdown menu to update or delete the product.

Having this functionality built-in to the main website, and not hidden away in the Django Admin area, makes for a more user friendly experience.

b) **Product Views:** Products are displayed either in list form, for multiple views, or in detail form, for a specific product. Within the detail view a user will be able to view product reviews, and add their own, in future this will be confined to users that have purchased the product. Listing views are paginated.

Product ratings are displayed for all products, which are an aggregate of the review scores for each product. The rating stars are produced using a Django custom template tag as detailed below.

c) **Product Search:** To provide users with an optimal experience, reducing the number of steps it takes them to add items to their basket, a search function is incorporated into the Navbar, thus appearing on all pages.

The search functionality performs a case-insensitive search across the product fields, 'title', 'brand', 'category', and, 'description' for matches. Any results are displays in a list view with pagination.

d) **Custom Template Tags:** In order to provide a more visual and user friendly experience for product reviews I wanted to provide star rating. To do so I had to write a custom templatetag which takes in the average product rating and uses this to produce HTML output which assigns the 'checked' class to all those stars up to and including the score. For example, a product with an average rating of 3 will have 3 stars render with 'checked' css class and 2 stars render with 'unchecked'.


# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))


## Frameworks, Libraries, Programs and Tools Used

1. [Django](https://docs.djangoproject.com/en/4.1/releases/3.2/)
    * Django is the framework.

2. [Django-allauth](https://www.intenct.nl/projects/django-allauth/)
    * Django app that allows for both local and social authentication.

3. [Google Fonts](https://fonts.google.com/)
    * Google fonts is used to import the 'Raleway' font into the style.css file which is used on all fonts within the website.

4. [Font Awesome](https://fontawesome.com/)
    * Font Awesome is used on all pages throughout the website to add icons for aesthetic and UX purposes.

5. [jQuery](https://jquery.com/)
    * jQuery is used to simplify and manipulate some tasks instead of regular JS.

6. [GitHub](https://github.com/)
    * GitHub is used to store the projects code after being pushed from Git.

7. [GitPod](https://gitpod.io/workspaces)
    * Development environment to build the website.

8. [Balsamiq](https://balsamiq.com/)
    * Balsamiq is used to create the wireframes during the design process.

9. [Coolors](https://coolors.co/)
    * This was used to show the color palette.

10. [AmIResponsive](https://ui.dev/amiresponsive)
    * Used to create the image at the very top of this document.

11. [PsycoPG2](https://pypi.org/project/psycopg2/)
    * PsycoPG2 is a database adapter. Library for connecting Python to PostgreSQL.

12. [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
    * Bootstrap was used for building responsive font-end content and styling.

13. [Heroku](https://dashboard.heroku.com/apps)
    * Used to deploy the website.

14. [ElephantSQL](https://www.elephantsql.com/)
    * ElephantSQL is used for hosting the PostgreSQL database.

15. [Stripe](https://stripe.com/gb)
    * Stripe. Card payment processing, security features and webhooks.

16. [Cloudinary](https://cloudinary.com/blog/heroku_add_on_for_image_management_in_the_cloud)
    * Cloudinary is used for storing images and static files.

17. [Pip](https://pip.pypa.io/en/stable/)
    * An installer for Python.

# Testing

## Validation

The W3C Markup Validator, W3C CSS Validator and JSHint tools were used to validate every page of the project to ensure there were no syntax errors in the project. If any were found during development, they were addressed or explained below.

### W3C Markup Validator - HTML Testing

[W3C Markup Validator](https://validator.w3.org/#validate_by_input)

**First Run Errors**

<details>
<summary>First run errors - Click Here:</summary>
<img src="media/readme/w2c-error1.png">

<img src="media/readme/w3c-error2.png">
</details>

Most of these errors were easy fixes. The javascript errors were addressed by deleting the type="text/javascript" and tested again.

**Second Run Errors**

<details>
<summary>Second run errors - Click Here:</summary>
<img src="media/readme/w2c3-error-rerun.png">
</details>

After running the validator for a second time the only errors displaying are from code taken from the Boutique Ado walkthrough project.


### W3C CSS Validator - CSS Testing

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)

<details>
<summary>Base.css - Click Here:</summary>
<img src="media/readme/basecss.png">

<img src="media/readme/stylecss.png">   
</details>

CSS run through the W3C Validator and passing.


### JSHint - JavaScript Testing

[JSHint](https://jshint.com/)

<details>
<summary> stripe_elements.js - Click Here:</summary>
<img src="media/readme/stripe-elementsjs.png">

<summary> countryfield.js - Click Here:</summary>
<img src="media/readme/countryfieldjs.png">   
</details>

### PEP8 Python Testing

Python code was tested to ensure that it met PEP8 style guidelines. This was done within the terminal console, which displayed errors and warnings throughout the project which were in parallel to the project being produced.

### Lighthouse

<details>
<summary> Lighthouse Results - Click Here:</summary>

Homepage
<img src="media/readme/homepagelh.png">

Products
<img src="media/readme/productslh.png"> 

Product Detail
<img src="media/readme/productdetaillh.png"> 

Wishlist
<img src="media/readme/wishlistlh.png"> 

</details>

## Manual Testing

<img src="media/readme/manualtesting.png"> 

# Deployment

## GitHub Pages
1. Log into GitHub and locate the repository.
2. On the nav bar look for the settings option and click on it.
3. Scroll towards to the bottom of the page.
4. Click the yellow "check it out here" link under GitHub pages.
4. Under 'Source' dropdown, click 'Main' from the options.
5. Click the save button.
6. The sitre will then be published. 
7. The site URL is visible on the green bar under the "Github Pages".

## Gitpod

1. You will need to search for and download the Gitpod browser extension.
2. Then proceed to login to GitHub.
3. Find the repository you wish to view.
3. Click the green "Gitpod" button.
4. Now you will be taken to a new tab and will be able to view the Gitpod repository.

## Heroku

1. Create the Heroku App:
    - Before creating the Heroku app make sure your project has the following files:
        - requirements.txt to create this type the following within the terminal: **pip3 freeze --local > requirements.txt**.
        - Procfile to create this type the following within the terminal: **python run.py > Procfile**.
    - Select "Create new app" within Heroku.
2. Attach the Postgres database:
    - Search "Postgres" within the Resources tab and select the Heroku Postgres option.
3. Create the settings.py file:
    - In Heroku navigate to the Settings tab, click on Reveal Config Vars and copy the DATABASE_URL.
    - Within the GitPod workspace, create an env.py file within the main directory.
    - Import the env.py file within the settings.py file.
    - Create a SECRET_KEY value within the Reveal Config Vars in Heroku.
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Run the following command in your terminal **python3 manage.py migrate**.
    - Add the CLOUDINARY_URL to the Reveal Config Vars in Heroku and add this to your settings.py file.
    - Add the following sections to your settings.py file:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILES_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com','localhost']
4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the top level directory: media, storage and templates.
    - Create a file named "Procfile" in the main directory and ass the following: [web: gunicorn project-name.wsgi].
    - Login to Heroku within the terminal window using **heroku login -i**
    - Run the following command in the terminal window: **heroku git:remote -a your_app_name_here**. By doing this you will link the app to your GidPod terminal.
    - After linking the app you can deploy new versions to Heroku by running the command **git push heroku main**.
5. Follow the steps directly from the Stripe website.

    - Create a Stripe account here.
    - Go to Developers > API Keys.
    - Find and copy the 'Publishable key', which will be for the STRIPE_PUBLIC_KEY in your env.py file in Gitpod.
    - Find and copy the 'Secret key', which will be for the STRIPE_SECRET_KEY in your env.py file in Gitpod.
    - Go to Webhooks > Add Endpoint button.
    - Add the url for the website (followed by /checkout/wh/).
    - Click Select Events > tick Select All Events > click Add Events button.
    - Reveal the Signing secret key, copy it, and add it to the env.py file in Gitpod as STRIPE_WH_SECRET.
    - A webhook will now be set up and ready to be tested on your local database.

# Media

[Google](https://images.google.com/)
Images sourced from Google

# Future Updates

- Email when orders are set to completed (i.e. items shipped).
- More admin/superuser rights from the website itself.
Quick-Buy options directly from the product pages.

# Credits

- Homepage Carousel](https://azmind.com/bootstrap-carousel-multiple-items/)

- Stack Overflow

- Boutique Ado walkthrough project



