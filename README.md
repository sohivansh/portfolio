# Personal website
## Video Demo: https://youtu.be/qalr-Nip0y0
## Description:
### Step 1: Design
#### Firstly I had to design the webiste layout in a online designing tool called **Figma**. After playing a bit, i got to know the basics of it and started my design. I then designed the navbar and its elements. The **avatar** is copyright free and was customised from a **avatar kit** in figma. It was very important to have the right **colour pallete** and so I decided to go with these **warm colours**. Once my design was ready, I was ready to move on to the next step which was to actually design the webiste in **Code**.

### Step 2 : Frontend design
#### I decided to go with **bootstrap** framework for my frontend design as it was something i was familiar with but still , I ha d to go through a lot of **documentation** in order to implement my design as well as make it **responsive** across different **viewports**. Firstly i setup **flask in my local system** along with its dependencies. I followed flask's documentation to lay the basics of my working directory in order to properly run the website. In templates, I created a layout.html file which has navbar and it elements. This layout is used accross all pages using **jinja templating**. I also added all the links to bootstrap and styles.css in the header of this file so that it does not need to be linked again and again.THE js script link is also in this file. Navbar also required a **collapse button** for responsive design across viewports. 
#### Nextly, index.html is the file that forms the homepage of the website. This contains a **responsive image** along with a intro paragraph and an **easter egg** which you find by clicking on different spots of the site. Lastly i added a form that uses post method which consists of a button to like the site. The **backend** for the same will be discussed in the upcoming paragraphs.
#### The rest of the pages were fairly **simple to implement** but making them **responsive** was a task in itself because i had to learn about container and measuring length in **vw(view width)**.

### Step 3 : Backend 
#### I configured my app with flask using flask's documentation. I defined different routes for all of the web pages and rendered the templates in those routes. 
#### ***Configuring the database :***
#### I imported **sqlite3** into **python** and had to learn a lil bit more about the library because i did not want to use cs50's lib as i wanted to complete this project without any **training wheels** and get some real world experience. I learned how to **connect a database** and make a cursor object. Moreover, i got to know about fetchone and fetchall methods and used them to update the number of likes. I also got to know about **commit** function in sqlite3 which is used to permanently store the changes to the database, otherwise, the database lost the changes on re running the server.

### Step 4 : Styling
#### ***Css***:
#### All the elements had to be spaced by adding padding so that they dont overlap each other. Styling the elements keeping in mind the **responsive** nature of the website was a task in itself. After reading bootstrap documentation, i got to know about **over riding** the css properties **pre implemented by bootstrap** and the method i used was **!important**.

#### ***Animate.css library : animations***
#### After going through the docs for animate.css , I **linked it into layout.html** using a **cdn link** and added animations to the necessary elements using **helper classes** as given in the library's documentation. The about page has a **delay class** added so that the paragraph elements appear after the **nav-brand animation** is done playing.

### Easter egg:
#### The easter egg is fairly simple and implemented in the script file in the static folder. I Hope that you find it after looking at the code.

### Step 5 : Deploying to heroku:
#### I followed through with **cs50 docs** on heroku and got to know about **gunicorn** and added it to the requirements file along with flask. After searching for a while on the internet, i got to know about a **procfile** and added the procfile to the root directory of the project. Then i deplyed the app to heroku by linking my github account.
