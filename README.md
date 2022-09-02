# Learning Django project 

- **[Done]** First taste to Django by following Corey Schafer's tutorial. Available at: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1 . It contains in youtube_tutorial folder
- **[Doing]** Blog API 

	- [Done] Create/Read/Update/Delete by Django Rest Framework
	- [Doing] Custom User model
	- [Done] Using Postgres db, replace sqlite 
	- Unit testing 
	- Adding LRU cache, use MemCached (how to monitor)
	- Using RabitMQ for pub/sub event. Use it to clear local cache when deploy >= 2 server. Demo how to use RabitMQ
	- Security: cors, injection, XSS. Using library of owasp


- Basic Authentication
	- Registration/Login/Logout API
	- Token based authentication for API
	- Permission for API 
	- Unit test

- Deployment 
	- Environment variable to seperate dev/deploy mode 
	- Deploy GCP, config to deploy production wsgi, config SSL
	- Create Docker image for this app. Deploy using Kubernetes
	- Apply CI/CD

- Monitor service after deploy 
	- Stress test service 
	- UI for monitor traffic, request rate 
	- auto restart service when it dies 

- Rate Limiter 
	- Set RateLimit for API. 
	- Use Redis to create RateLimit service

- Elasticsearch
	- Intergrate Elasticsearch for searching user, blog title.

- Logger
	- Adding logger for service
	- Config rotation log 
	- How to grep log, debug from log, log format 

- *[Option]* Shorten link app 
- *[Option]* Login with facebook, google

