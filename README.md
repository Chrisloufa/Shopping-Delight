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



# Frameworks, Libraries, Programs and Tools Used

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