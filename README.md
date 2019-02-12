# rmqmultithread

This project is simulating rabbitmq traffic(sender and reciver) with bots.

Installation

Project's requirements are the following:

    pika
    lorem

Project has been developed and tested with Python 2.x in mind.

I used rabbitmq on docker

Docker installation : https://docs.docker.com/install/linux/docker-ce/debian/

#Rabbitmq installation on docker

docker search rabbitmq # Search the Docker Hub for images

docker pull rabbitmq:latest # Pull an image or a repository from a registry

docker run -d -p 5672:5672 -p 15672:15672  --name rabbitmq rabbitmq

#its working 

#if you need manage images

docker images
 
#if you need container status

docker ps
 
#if you need start image

docker start imagename
 
#if you need stop image

docker stop imagename
 
#if you need restart you image
docker restart imagename

#Let's See Project Details

we have function for creat and start thread
def start_threads(thread_size,func_name):

thread_size =  how many thread we want to create
func_name = what is our function name

#we created one eksisozluk reciver
#we create one linkedin reciver
#we create one facebook reciver
#we create one instagram reciver
#we create one blanews reciver

#and we create how many bot work send new news us. we wrote 100.
start_threads(100,bot)

#and we wait for thread functions continou 
wait_for_search()

License

Project is licensed under the terms of the MIT License (see the file LICENSE).
