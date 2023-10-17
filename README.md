# Luna discussion forum

![alt text](static/images/luna-logo_transparent.png)

## Deployment

site is live at : https://portfolio-4-1ef2f7260848.herokuapp.com/

## Frameworks

* This application is using the python frameWork Django v3.2.21
* Db is a postgresSql hosted on elephantsql.com
* Site is deployed at heroku.com
* jQuery is used as JS framwork
* Boostrap is used as HTML/css framwork


## Features 

 __HOMEPAGE__

### Exsiting Features
 
* User can create an account.
* Users can sign in and sign out.
* Users can create posts.
* Users can like posts.
* Users can add comments on posts.
* A Post needs to be approved by admin before its published.
* A Comment needs to be approved by admin before its published.
* Users can like comments.
* Users can add/change profile picture.
* Admin can create new categories.
* Admin can add a image to an category.
* Admin can add a category to a post.

![alt text](static/images/readme/luna_readme_homepage.png)

__POSTDETAIL__

On the postdetailpage the user can view the post and like the post, if the user clicks the like button again the post is unliked.

![alt text](static/images/readme/luna_readme_postdetailpage.png)

__POSTDETAIL COMMENT__

On the post detailpage there is a comment section where user can add comments with content and image. Users can like comments if the user clicks the like button again the comment is unliked. The profile picture of the user is also dispalyed by each users comment.

![alt text](static/images/readme/luna_readme_postdetailpage_comments.png)

__LOGIN PAGE__

Loginpage using allAuth framwork, defualt allauth template is modified for custom need. To navigate to login page user clicks in "login" in the navbar in the header. 

![alt text](static/images/readme/luna_readme_loginpage.png)

__LOGIN PAGE__

Signup page using allAuth framwork, defualt allauth template is modified for custom need. To navigate to signup page user clicks in "sign up" in the navbar in the header. 

![alt text](static/images/readme/luna_readme_signuppage.png)


__PRFOILE PAGE__

Profile page where user can add/change thier profile picture. The form is using the framwork crispy forms.

![alt text](static/images/readme/luna_readme_profilepage.png)



## Testing
 
 * To run python test in terminal write: "python manage.py test"
 
__Python test results__
![alt text](static/images/readme/luna_readme_pythontestresults.png)


Inspiration taken from code insitutes rock papper scissors game made by code insitute.

* For blinking effect this guide was used
https://www.w3docs.com/snippets/css/how-to-create-a-blinking-effect-with-css3-animations.html
* For to convert an png image to favicon (.ico format) 
https://cloudconvert.com/ico-converter tool was used.
* to create the logo i used adobe https://www.adobe.com/express/create/logo
* To make images transparent https://www.remove.bg/ tool was used

