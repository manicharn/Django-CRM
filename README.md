# Django-CRM

# To pull the postgres image from dockerhub
# --> docker pull postgres:14.1-alpine
# To create a container of postgres docker image 
# --> docker run --name mypgadmin -e POSTGRES_USER=demo -e POSTGRES_PASSWORD=demo -e POSTGRES_DB=mylocaldb -p 5432:5432 -d postgres:14.1-alpine
# To view all images
# --> docker image ls
# To view all containers
# --> docker ps --all
# To run a container 
# --> docker start <container-id>
# To stop a container
# --> docker stop <container-id>
# To view logs of  a container
# --> docker logs <container-id>
# To inspect a container
# --> docker inspect <container-id>
# To remove/delete a container
# --> docker rm <container-id>
# To remove/delete a image note: first we need to remove those containers which are using this image
# --> docker rmi <image-id>
# To check version of docker
# --> docker --version
# To check version of image
# --> docker images <image_name>
# To get the BASH terminal of the container
# --> docker exec -it <container_id> bash
# To connect to postgres database and work with query in bash(this cmd should be runned in bash terminal)
# --> psql -U username -d databasename -w


