# Instagram Clone
#### This is a web clone of the instagram application to give user a feel of instagram application, 08/03/2019.
#### By **ANUM ASIF**
## Description
This application is a simplest web clone of the instagram application. A user can create an account and sign into it. The site supports uploading images. User can see posts of other users on the home page. user can also like them or post a comment on them
## Specifications
### User
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Register new account | Fill in the registration form in the home page | Sends activation link to the registration email. The link should be clicked to activate the account |
| Login | Fill in the login form with correct username and password | Redirects the user to the homepage of the user |
| Edit Bio | Click on the edit profile button in the homepage. Upload picture, and fill in the username and password | Redirects the user to the profile with changes made to profile |
| Comment on photo | Click on the comment tab to view the image and its details. Type in the comments in the comments field | Refreshed the page and reflects the changes |

## Setup/Installation Requirements
- Python 3.6
- Django Framework
- HTML, CSS, JavaScript and Bootstrap
- PostgreSQL
- python virtual environment
## Running the Application
   * To run the application, in your terminal:

    1. Clone or download the Repository
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements. Or run: 
	pip3 install -r requirements.txt 
       to automatically install all the requirements
    4. Prepare environment variables
	-export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'
	-export SECRET_KEY='Your secret key',etc
    5. Run initial migration
    	python3.6 manage.py makemigrations gram
    	python3.6 manage.py migrate
    6. Run the application
    	python3.6 manage.py runserver    	
    7. Access the application through `localhost:8000`
	
### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 
## Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/AnumAsif/instagram/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/AnumAsif/instagram/issues/new). Please include sample queries and their corresponding results.
## Technologies Used
- This project was generated with [Python3.6](https://devdocs.io/python~3.6/) and using [Django](https://docs.djangoproject.com/en/2.1/) framework
## Support and contact details
Please feel free to contact me if you have any suggestion for me to improve this website.
- Email: anum@cockar.com
## Link to live website
- [InstagramClone](https://instagramclone.herokuapp.com/)
### License
*MIT*
Copyright (c) 2018 **ANUM ASIF**
