# Sizzle and Steak

Sizzle and Steak is a fictional restaurant located beside the sea in County Antrim, Northern Ireland. The app is a restaurant management system designed too allow staff to easily manage the menus and bookings. It also provides customers with a simple, easy to use booking system where they can view and manage their own reservations.

## Table of Contents
* [User Experience Design (UX)](#User-Experience-Design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Agile Planning](#Agile-Planning)
          * [Epics](#Epics)
          * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
      * [Features](#Features)
      * [Future Features](#Features-Left-to-Implement)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
        * [Security](#Security)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
    * [Test Results](#Test-Results)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed to helped restaurant staff to easily manage their menus displayed on the website, as well as keeping track of upcoming bookings and capacity, editing and deleting as neccessary. 

The site also aims too provide customers with a simple, hassle free way to make reservations without the need to call the restaurant. They will also be able to cancel their bookings or update when needed.

### Agile Planning

This project was developed using agile methadologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over four weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to sprints and story pointed according to complexity. Must have stories were completed first, should haves and then finally should haves. It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak/projects/1) and can be viewed to see more information on the project cards. All stories expect the documentation tasks have full set of aceptance criteria in order to define the functionality that marks that story as complete.

![Kanban image](docs/readme_images/kanban.PNG)

#### Epics

The project had 7 main Epics (milestones):

**EPIC 1 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

**EPIC 2 - Stand alone Pages**

The stand alone pages epic are for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

**EPIC 3 - Authentication Epic**

The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it the staff would not be able to managed the bookings securely without regular site visitors also being able to see and perform actions.

**EPIC 4 - Menu**

The menu epic is for all stories that relate to the creating, deleting, editing and viewing of menus. This allows for regular users to view menus and for staff to manage them with a simple UI interface.

**EPIC 5 - Booking**

The booking epic is for all stories that relate to creating, viewing, updating and deleting bookings. This allows the staff to easily view upcoming bookings, manage the bookings and also for customers to book and manage their own reservations.

**EPIC 6 - Deployment Epic**

This epic is for all stories related to deploying the app to heroku so that is live for staff and customer use.

**EPIC 7 - Documentation**

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

#### User Stories

The following user stories (by epic) were completed over the 3 sprints:

**EPIC 1 - Base Setup**

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

As a developer, I need to create static resources so that images, css and javascript work on the website

As a developer, I need to set up the project so that it is ready for implementing the core features

As a developer, I need to create the footer with social media links and contact information

As a developer, I need to create the navbar so that users can navigate the website from any device

**EPIC 2 - Stand alone Pages**

As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist

As a developer, I need to implement a 500 error page to alert users when an internal server error occurs

As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views

As a restaurant owner, I would like a home page so that customers can view information on my restaurant

**EPIC 3 - Authentication Epic**

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

As a Site Owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used.

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling

**EPIC 4 - Menu**

As a staff user, I want to be able to create a new menu when we have new dishes to offer

As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant

As a staff user, I want to be able to edit a menu when updates are needed

As a staff member, I would like to receive feedback when I create or update menus so that I can see they have worked

As a staff user, I want to be able to delete a menu when it is no longer used

**EPIC 5 - Booking**

As a user, I would like to be able to create a new booking when I want to visit the restaurant

As a user, I would like to view my bookings when I need to check the information

As a user, I would like to be able to edit a booking so that I can make changes when needed

As a user, I would like to receive feedback when I create a booking or edit one so I know it was completed successfully

As a staff user, I want to be able to search a booking by reference to save time searching

As a user I would like to delete a booking when I no longer require it

**EPIC 6 - Deployment Epic**

As a developer, I need to set up whitenoise so that my static files are served in deployment

As a developer, I need to deploy the project to heroku so that it is live for customers

**EPIC 7 - Documentation**

Tasks:

* Complete readme documentation
* Complete testing documentation write up

## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Ham burger menu for mobile devices
* Ability to perform CRUD functionality on Menus and Bookings
* Restricted role based features
* Home page with resturant information

## The-Structure-Plane

### Features

``USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device``

Implementation:

**Navigation Menu**

 The Navigation contains links for Home, Bookings, Menus and has allauth options.

The following navigation items are available on all pages:
  * Home -> index.html - Visible to all
  * Bookings (Drop Down):
    * Manage Bookings -> managebookings.html - Visible to logged in users
    * New Booking -> booking.html - Visible to logged in users
  * Menus (Drop Down):
    * View Menus -> menus.html - Visible to all
    * Create Menu -> create_menu.html - Visible to staff
    * Manage Menus -> managemenus - Visible to staff
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

``USER STORY - As a restaurant owner, I would like a home page so that customers can view information on my restaurant``

Implementation:

**Home Page**

The home page contains resturant information at the top of the page. This will immediately make it evident to the user, what the purpose of the web site is.

Under the information section are two buttons, 'Make a booking' and 'View Menus'. These buttons will allow the user a quick way to the respective pages if they wish to make a booking or view the restaurants active menus.

The last section of the home page contains a google map, marking the location of the restaurant and the opening hours of the restaurant. This will allow the user to locate the restaurant and operating times.

``USER STORY - As a developer, I need to create the footer with social media links and contact information``

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a Twitter and Facebook link so that users can follow the restaurant on social media if they want to keep up to date with special offers not advertised on the website. These icons has aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.


Favicon
    * A site wide favicon will be implemented with .....
    * This will provide an image in the the tabs header to allow the user to easily identify the website if they have multiple tabs open.


**Error Pages**

``USER STORY - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist``

Implementation:

**404 Page**

As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need  of the browsers back button.

``USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs``

Implementation:

**403 Page**

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete or access pages that are restricted. 

This covers:

* Create Menu - Only authorized to staff
* Edit Menu - Only authorized to staff
* Delete Menu - Only authorized to staff
* Edit Booking - Only authorized to the customer who created the booking or a staff member
* Delete booking - Only authorized to the customer who created the booking or a staff member

``USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs``

Implementation:

**500 Page**

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

``USER STORY - As a staff user, I want to be able to create a new menu when we have new dishes to offer``

Implementation:

**Create Menu Page**

A create menu page was implemented to allow staff users to create new menus via the UI without having to use the backend admin panel. This will allow staff the ability to quickly update menus when they have made changes to the food being offered.

``USER STORY -As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant``

Implementation:

**View Menu Page**

A menu page has been implemented to allow users to see the current active menus and decide whether they are interested in the food we offer before booking. This is visible to all users regardless of logged in state as it is not user friendly to restrict core information from users to force them into signing up.

``USER STORY -As a staff user, I want to be able to edit a menu when updates are needed``

Implementation:

**Edit Menu Page**

On the manage menus page a button was added to allow staff members to edit a menu when changes need to be made.

``USER STORY -As a staff member, I would like to receive feedback when I create or update menus so that I can see they have worked``

Implementation:

**Toasts**

Custom toasts were added on successful creation and deletion of menus which dsplay success messages to the user to enable them to see that the action completed successfully.

``USER STORY -As a staff user, I want to be able to delete a menu when it is no longer used``

Implementation:

**Delete Menu Page**

On the manage menus page, a delete button has been implemented that will take staff users to a confirmation page to allow them to delete a menu. This will allow staff to delete menus when they are no longer needed

**Base Setup User Stories**

The following stories were implemented in order to set up a base structure for all the HTML pages and the core installations and configurations needed to run the application. While these do not show as individual features, they were stories completed that were needed to implement all of the stories above.

``As a developer, I need to create the base.html page and structure so that other pages can reuse the layout``

``As a developer, I need to create static resources so that images, css and javascript work on the website``

``As a developer, I need to set up the project so that it is ready for implementing the core features``

### Features Left To Implement
- Add any features that are not yet implemented


## The-Skeleton-Plane

### Wireframes

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the the main booking and menu tables, linked by primary/foreign key relationships.

The Menu Items model holds objects that are linked to the Menu Models by a many to many relationship. This allows for staff to create menus with many menu items on.

Bookings are related to the customer (user) by a Foreign Key which allows the users to be able to view and update bookings attached to their accounts.

Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.

![Entity Relationship Diagram](docs/readme_images/erd.JPG)

### Security


## The-Surface-Plane
### Design
### Colour-Scheme
### Typography
### Imagery


## Wireframes

- Home page

- 404 page


## Technolgies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - .
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - .
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- Canva
  - This was used to create the logo in header 

## Testing

### Responsiveness



### Accessibility



**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

| Navigation Link | Page to Load    |
| --------------- | --------------- |
|                 |                 |




**Footer**

Testing was performed .......




**Validator Testing**



**Lighthouse Report**

Lighthouse report generated showed.....


## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:

The live link can be found here:

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

## Credits 


