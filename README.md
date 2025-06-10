# Friluft Night 

The purpose of this website is to provide a platform where people can find, share and review wild camping areas. 

# UX 

## Goals

### Target Audience 

- Wild campers looking to find somewhere to stay 

- Wild campers looking to contribute to the community by sharing or reviewing somewhere they have stayed. 

### User Stories

The user stories for this project can be found [here](https://github.com/users/ElFalch/projects/4/views/1).

- These user stories include some future ideas (labelled as won't-have). 

## Visual Design

### Colours

![Friluft Night colour palette](https://github.com/ElFalch/friluft-night/blob/main/static/images/colour-palette/friluft-night.png "Friluft Night colour palette")

Colours used reflect those in the default image, creating a bright, natural look. White is also used to make text stand out, making the website easier to use whilst being complimentary with the main colour scheme. 

### Fonts 

- The brand font was chosen for it's adeventurous yet clear style, giving users the feeling of being in the outdoors whilst being easy to read. 

- The main font was chosen for its clear appearance, making is easy to read even at small sizes, increasing the likelihood that users will understand the material provided. 

### Icons 

Icons are from the [FontAwsome](https://fontawesome.com/v4/icons/) icon library. 

- A tree icon was used for the navbar brand, to reflect that this website focusiese on the outdoors. 

- A comments icon was used for the review count to clarify that this is the numebr of reviews whilst appearing neat and tidy. 

### Images 

Default Image: 

- An image of a tent by the beach at sunset was used for it's bright, fresh colours that reflect those of the colour scheme, whilst being inviting and reflecting the purpose of the website (to spread the joy of wild camping!)

# Page Elements 

## All Pages 

Navbar: The Bootstrap navbar contains links to the index and login or logout pages of the site and has the Friluft Night logo in its brand. The navbar links collapse down to a burger icon with a dropdown menu on smaller devices.

Footer: A Footer with links to social media accounts, presented as icons. 

## Home Page

The index page is titled "home" and contains the a paginated list of published & approved wild camping spots with images, author and time added information, aswell as links to more details. 

Users can also edit their own posts using the same form as in the add post page, aswell as delete them.

## Add Post

The add post page is titled "recommend" and contains a form which allows users to add a post title, description and image.

## Post Detail

Each post detail page contains the above information about each site, as well as a more detailed description, list of reviews and a form for adding reviews (if user is signed in), which must be approved by admin before being displayed to other users. 

Users can also edit their reviews and delete them. 


# Deployment 

This project was deployed to Heroku. The deployed site can be found here.

## Forking the GitHub Repository

1. To create your own copy of a GitHub repository that you can edit, you must fork the repository using the following steps:

2. Open the repository you want to fork.

3. Click the fork button in the top-right corner of the screen.

4. Choose a new name for the repository, if you wish.

5. Click create fork.


## Local Deployment 

### Cloning your Github Repository to Visual Studio Code

1. In your computer's file system, create a folder for the new project within the folder containing your VS Code projects.

2. Open the folder for the new project in VS Code and open a new terminal.

3. Navigate to your GitHub dashboard and open the repository you want to clone.

4. click on the code dropdown menu and copy the URL.

5. In the VS code terminal, enter git clone and paste the URL with a space and full stop at the end. For example:

git clone https://github.com/ElFalch/seabird-survey-simulator.git .

6. You should now see the repository files on the left hand side of the screen and be able to push changes to Git.

### Install dependencies
pip install -r requirements.txt

### Run the application locally
python manage.py runserver


## Heroku Deployment 

1. Create a new Heroku application

2. Connect the GitHub repository

3. Configure environment variables and build settings

4. Enable automatic deployments from main branch

5. Click on deploy from main branch and open the app once complete (build progress can be monitored in the actvity panel)