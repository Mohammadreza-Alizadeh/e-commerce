# e-commerce
a simple e-commerce using django framework.

## Project Summary
The project is built using Django and Python. It includes the following features:

 - custom User model
 - login, register and edit profile
 - shoping cart using sessions
 - you can simply create a profile and edit it, ( you are able to upload an avatar )  
 - you can create new products as admin  
 - you can add products to your cart without a logged in account
 - you can see list of products you bought



## techs i used
- django
- bootstrap
- django crispy forms

## Getting Started
To get this project up and running, you should start by having Python installed on your computer. It’s advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with pip install virtualenv.

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

``` 
python -m venv env
```

That will create a new folder naemd env in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

or if you use windows activate it with this command :
```
.\env\scripts\activate
```

Then install the project dependencies with:
```
pip install -r requirements.txt
```

Now you have to migrate the migrations with this command :
```
python manage.py migrate
```

Its done, Now you can run the project with:
```
python manage.py runserver
```
