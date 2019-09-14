# Instagram Lite
Instagram Lite is a web app created with Django, Postgres and Docker that aims to implement the basic CRUD functionalities built around the idea of uploading images.  

![Instagram Sample Homepage](/static/images/sample_profile.png)

![Instagram Lite Homepage](/static/images/instagram_lite_homepage.png)

## POST action 
![Create](/static/images/create.png)
After the user uploads an image, he is redirected to his homepage that displays all his pictures.
![Sample User Profile Page](/static/images/post.png)

## Post detail
After clicking on an image on one's profile, one gets referred to a page with the post's uuid and post details.
![Sample Post Detail](/static/images/post_detail.png)

## UPDATE action
Initial Post:
![Before1](/static/images/before1.png)
![Before2](/static/images/before2.png)
Updated Post:
![After](/static/images/updated_pic.png)

## A Profile with comments
![Sample Post w/ Comments](/static/images/after_comment.png)

## Ways to improve
Currently in order to add a comment, another template is used.  AJAX using a JS framework like React, Vue, or JQuery is certainly better and under consideration.
Followers, likes, and the other features of Instagram are also missing.