Please find my assignment 3 attached.

Question 1 should work ok.

Question 2 - I have:
                    - imported the login_required function from the django.contrib.auth.decorators library and 
                    -put @login_required decorator above the view def
                    -added a login.html to templates in the project root directory
                    -updated 'templates' in settings ('DIR')  so Django knows where to find this template
                    
                    Despite this the authentication system does not work in my porject.
                    
Question 3 - I was unsure how to relate the users in the Users database to the objects in the players model. I have set up a ForeignKey between these but this does not specify which objects in the players model to send to which users.
           - Maybe this is just a case of manually assigning user to model instance using the admin site, but either way I haven't got a working authentication system from part 2.
           Not sure where I went wrong with the authentication.