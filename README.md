
# Friluft Night 

The purpose of this website is to provide a platform where people can find, share and review wild camping areas. 


## Contents 

1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)

    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Images](#images)

      </details></li>

    </ul>

</details>

2. <details open>
    <summary><a href="#page-elements">Page Elements</a></summary>

    <ul>

    <li>

    <summary><a href="#all-pages">All Pages</a></summary>
    
    </li>

    <li>

    <summary><a href="#home-page">Home Page</a></summary>

    </li>

    <li>

    <summary><a href="#edit-post">Edit Post</a></summary>

    </li>

    <li>

    <summary><a href="#add-post">Add Post</a></summary>

    </li>

    <li>

    <summary><a href="#post-detail">Post Detail</a></summary>

    </li>

    <li>

    <summary><a href="#admin-panel">Admin Panel</a></summary>

    </li>


    </ul>
    </details>


3. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>

    <li><details>
    <summary><a href="#validation">Validation</a></summary> 

    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)

    </details></li>

    <li><details>
    <summary><a href="#automated-testing">Automated Testing</a></summary>

    - [Lighthouse Testing](#lighthouse-testing)

    </details></li>

    <li>

    <summary><a href="#manual-testing">Manual Testing</a></summary>

    </li>
</ul>
</details>

4. <details open>
    <summary><a href="#deployment">Deployment</a></summary>
    <ul>

    <li>

    <summary><a href="#forking-the-github-repository">Forking the Github Repository</a></summary>

    </li>

    <li><details>
    <summary><a href="#local-deployment">Local Deployment</a></summary> 

    - [Cloning Your Repository to Visual Studio Code](#cloning-your-repository-to-visual-studio-code)

    </details></li>

    <li>

    <summary><a href="#heroku-deployment">Heroku Deployment</a></summary>
    
    </li>
</ul>
</details>

5. <details open>
    <summary><a href="#attributions">Attributions</a></summary>

    <ul>

    <li>

    - [Frameworks Used](#frameworks-used)
    - [Libraries Used](#libraries-used)
    - [Other Tools Used](#other-tools-used)
    - [Code From External Sources](#code-from-external-sources)
    - [Images](#images)

</li>

</ul>

</details>


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

Colours used reflect those in the default image, creating a bright, natural look. White, bright blue and red are also used to make text, buttons and links stand out, making the website easier to use whilst being complimentary with the main colour scheme. 

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

Navbar: The Bootstrap navbar contains links to the index, recommend and login or logout pages of the site and has the Friluft Night logo in its brand. The navbar links collapse down to a burger icon with a dropdown menu on smaller devices.

Footer: A Footer with a message saying "Adventure awaits!" 

## Home Page

The index page is titled "home" and contains the a paginated list of published & approved wild camping spots with images, author and time added information, aswell as links to more details. 

There are buttons allowing users to edit their own posts and delete them, aswell as move between the pages of listed posts. If the userr selects the edit button, they are directed to another page. If the delete button is selected, a pop up appears asking users to confirm they would like to delete the post. 

![first index page screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/home-page/index-page-1.png "first index page screenshot")
![second index page screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/home-page/index-page-2.png "second index page screenshot")
![third index page screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/home-page/index-page-3.png "third index page screenshot")


![delete post screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/home-page/delete-post.png "delete post screenshot")


### Edit Post 

A form, prepopulated with the information from the post selected to edit allows users to make any changes they need, but only if they adhere to the conditions of the form. 

![First edit post screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/edit-post/edit-post-1.png "first edit post screenshot")
![Second edit post screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/edit-post/edit-post-2.png "second edit post screenshot")
![Third edit post screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/edit-post/edit-post-3.png "third edit post screenshot")


## Add Post

The add post page is titled "Recommend" and contains a form which allows users to add a post title, description and image (if they are signed in). 

![Add post screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/add-post-form/add-post-form.png "add post screenshot")

Once posts have been added, they will not be displayed to other users until they have been approved by admin. Until approval is obtained, posts will only be visible to logged-in users who have written them with a message saying "this post is waiting for approval". 

## Post Detail

Each post detail page contains the summary information on the home page, as well as a more detailed description, list of reviews and a form for adding reviews (if user is signed in). 

Reviews must be approved by admin before being displayed to other users. Until approval is obtained, reviews will only be visible to the logged-in users who have written them, with a message saying "this post is waiting for approval". 

Users can also edit their reviews and delete them. 


![Post detail page screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/post-detail.png "post detail screenshot")
![First leave review screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/leave-review-1.png "first leave review screenshot")
![Second leave review screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/leave-review-2.png "second leave review screenshot")
![First edit review screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/review-edit-1.png "first edit review screenshot")
![Second edit review screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/review-edit-2.png "second edit review screenshot")
![First delete review screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/review-delete-1.png "first delete review screenshot")
![Second delete review screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/post-detail-page/review-delete-2.png "second delete review screenshot")


## Admin Panel

The admin panel allows users logged in as admin to view, edit, delete and approve posts and reviews, aswell as control user accounts. Custom images can also be added to the site via Cloudinary. 

![Admin panel home page screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/admin-panel/admin-panel.png "admin-panel screenshot")
![Admin panel post list screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/admin-panel/admin-panel-post-list.png "admin-panel post list screenshot")
![First admin panel post edit screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/admin-panel/admin-panel-post-edit-1.png "first admin panel post edit screenshot")
![Second admin panel post edit screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/admin-panel/admin-panel-post-edit-2.png "second admin panel post edit screenshot")
![Admin panel review list screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/admin-panel/admin-panel-review-list.png "admin-panel review list screenshot")
![Admin panel review edit screenshot](https://github.com/ElFalch/friluft-night/blob/main/static/images/feature-images/admin-panel/admin-panel-edit-review.png "admin panel post edit screenshot")


# Testing

## Validation 

### HTML Validation

The HTML for each page was validated used the [W3C Markup Validator](https://validator.w3.org/). For the index and post detail pages, errors occured because of django template language linking each post and review edit button to the relevant posts and reviews, something which does not present any issues. All other site pages did not present any errors upon validation. 

| Page          | Result                                                                                                                                                |   
| ------------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------:| 
| index.html    |![Index Page HTML validation](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/validation/html-validation/validation-html-index.png) | 
| post_detail.html     |![Post Detail Page HTML validation](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/validation/html-validation/validation-html-post-detail.png)  |


### CSS Validation

The CSS stylesheet was validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

| Summary         | Result                                                                                                                                                |   
| --------------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------:| 
| No errors found |![friluft Night CSS validation](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/validation/css-validation/validation-css.png)   | 
| Warnings are the result of Google fonts being used and do not present any issues |![friluft Night CSS validation warnings](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/validation/css-validation/validation-css-warnings.png)|

### JavaScript Validation 

The JavaScript for this project was validated using [JSHint](https://jshint.com/). No errors or warnings were found.

### Python Validation 

The Python written for this project was validated using [Code Institute Python Linter](https://pep8ci.herokuapp.com/). No errors or warnings were found.


## Automated Testing 

### Lighthouse 

Automated testing of the deployed site for performance, accessibility and best practises was conducted using the [Lighthouse tool](https://developer.chrome.com/docs/lighthouse) within Chrome DevTools.  

#### Lighthouse Report Summaries

The total score for performance was 97% for the index page, 98% for the post detail page and 100% for the add post page. The index and post detail pages were scored 78% for best practices. 

| Page          | Lighthouse Report Summary                                                                                                                             |   
| ------------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------:| 
| index.html    |![Index Page Lighthouse Report Summary](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/lighthouse-testing/lighthouse-summary-home.png)                       | 
| post_detail.html     |![Post detail Page Lighthouse Report Summary](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/lighthouse-testing/lighthouse-summary-post-detail.png)                     |
| add_post.html     |![Add Post Page Lighthouse Report Summary](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/lighthouse-testing/lighthouse-summary-add-post.png)                     |

#### Lighthouse performance report diagnostics

Cookies relating to cloudinary image storage caused the relatively low best practises score for the index and post detail pages.

| Page          | Lighthouse Report Diagnostics                                                                                                                         |   
| ------------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------:| 
| index.html & post_detail.html   |![Index Page Lighthouse Report Diagnostics](https://github.com/ElFalch/friluft-night/blob/main/static/images/testing/lighthouse-testing/lighthouse-diagnostics.png)                   | 


## Manual Testing 

Manual testing was carried out to ensure all links, forms and JavaScript elements of the site worked as intended. Device mode in [Chrome DevTools](https://developer.chrome.com/docs/devtools) was used to ensure that the design was responsive and that features were fully functional across all device sizes. 



# Deployment 

This project was deployed to Heroku. The deployed site can be found [here](https://friluft-night-app-4e8c3a45356d.herokuapp.com/).

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

git clone https://github.com/ElFalch/friluft-night.git .

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


# Attributions

## Frameworks Used

- [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was used for basic elements and styles. 

## Libraries Used

- Fonts used were from [Google Fonts](https://fonts.google.com/)

- Icons used were from [Font Awsome](https://fontawesome.com/v4/icons/)

## Other tools used

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) was used to check the contrast between each of the colours used in the project. 

- Favicons were generated by [favicon.io](https://favicon.io/)

- [Autoprefixer](https://autoprefixer.github.io) to add css prefixes required for consistency across browsers.

- [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) messages were used to describe each stage of the development of this project in a clear, consistant format. 

## Code from external sources

- Site layout, styling, Javascript and Python (bar a few small styling changes and the ability for normal users to add, edit and delete posts) taken from the Code Institute "I Think Therefore I Blog" walkthrough project.

- General structure and code for dropdown menu contents section of ReadMe taken from the GitHub repository [horizon-photo](https://github.com/Ri-Dearg/horizon-photo/tree/main)


# Images


## Local Images

- image used to create favicons: tweemoji, copyright 2020 Twitter. Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)

- default.jpg: [Photo by Teemu R](https://www.pexels.com/photo/photo-of-tent-by-the-beach-1840394/)

## Cloudinary Images

- Beehive Bothy: [Photo by Miro Alt](https://www.pexels.com/photo/orange-camping-tent-near-body-of-water-during-daytime-176381/)

- Campsite by Loch Ochiltree: [Photo by Olga Lioncat](https://www.pexels.com/photo/cloudy-sky-over-mountains-and-river-7244512/)

- Quiraing: [Photo by Anna Urlapova](https://www.pexels.com/photo/man-standing-on-a-rock-2975445/)