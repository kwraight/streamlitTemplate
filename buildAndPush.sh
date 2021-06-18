docker build . -f dockerFiles/Dockerfile -t kwraight/template-app:1.0
docker push kwraight/template-app:1.0
docker build . -f dockerFiles/Dockerfile -t kwraight/template-app:latest
docker push kwraight/template-app:latest
