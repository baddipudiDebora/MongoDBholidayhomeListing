## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

# Holiday Home Search
A portal to connect to AirBNB, users can add listing of their home, and link it to AirBnb.



## UX - Requirements

### Wire Frame and UX design
(https://github.com/bsdebora/holidayhomesearch/blob/master/UI%20Wireframes%20-%20Holiday%20Home.docx)

## MongoDB design
(https://github.com/bsdebora/holidayhomesearch/blob/master/Mongo%20DB%20Design%20-%20Holidayhome.docx)

## Features
In user stories format
(https://github.com/bsdebora/holidayhomesearch/blob/master/User%20stories-%20Holiday%20home.docx)
### Existing Features
1. User able to access the website to add/ view / edit / delete listings
2.  index (home) page
3.  register feature
4.  login feature
5.  add listing feature
6.  view listing feature
7.  edit listing feature
8.  delete listing feature
9.  fetching the contact details from the form and writing to MongoDB
10. Test to check if the website is responsive on different devices
11. Test to check system displays appropriate error message whne user enteres invalid data

### Features Left to Implement
1. paginition in vew lsiting
2. forget passoword
3. search listing based on country / city/ other property characteristics
4. Online payment for booking
5. Admin login


### Technologies Used
* The project uses HTML to add content to the website.
* The project used CSS to style the content.
* The project used BootStrap theme to have reusable CSS styling and make tyhe site responsive.
* Icons / Images were taken from Font-Awesome website
* Styling was taken from Google fonts 
* Used Python for business logic implementatin
* Python framework to speedup development - Flask
* database used - MongoDB (to store Listing info, user login info, info from contactus form)


## Testing

### Manual Testing
Testing has been performed to verify and validate the software as per the requirements.
Manual Testing performed for the below
 #### Test senarios 

1. Test to check if  all the pages layout is as perthe wireframes from the UX design
2. Test to check functionality of index (home) page
3. Test to check functionality of register 
4. Test to check functionality of login 
5. Test to check functionality of add listing
6. Test to check functionality of view listing
7. Test to check functionality of edit listing
8. Test to check functionality of delete listing
9. Test to check functionality of fetching the contact details from the form and writing to MongoDB
10. Test to check if the website is responsive on different devices
11. Test to check system displays appropriate error message whne user enteres invalid data


## How your project looks and works on different browsers and screen sizes
  -  The website is designed with bootstrap and is tested for responsiveness on Desktop / Laptop /Tablet /Mobile View.

 - Please check the attached Wireframes PDF on different devises from the UX requirements section

 (https://github.com/bsdebora/holidayhomesearch/blob/master/UI%20Wireframes%20-%20Holiday%20Home.docx)

###    It has been tested for iphone6/7/8 , also in iPad. 
  


## Any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
- Pagination is not addressed
- current page not highlighted in the navbar

## Deployment
Code was written in gitpod and deployed to heroku



#### the published github page is below

![Heroku URL] (https://mongodbpractisedemo.herokuapp.com/)

## Credits
### Bootstrap theme taken from
www.themefisher.com


