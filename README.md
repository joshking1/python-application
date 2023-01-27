# python-application

docker build -t kubia . 

docker run -d -p 8080:8080 --name rest-server kubia
