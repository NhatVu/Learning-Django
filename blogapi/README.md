## Note for BlogAPI app 

- [2021-11-04] Issue: Use CustomUser model after running Django the first time. Need to find a way to migrate data. Avoiding delete all db because of migration conflict 
- [2021-11-05] Issue: Django default use username for login. Customize to use email instead. Customize Token generation
	- Post.objects.all() in posts.views # ? do they actually get all the post ?