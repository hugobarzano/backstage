#Makefile

docker-image:
	docker build -f Dockerfile -t python-workshop-graphql .


docker-run:
	docker run -p 0.0.0.0:80:8080/tcp --name python-app --rm -t python-workshop-graphql:latest

