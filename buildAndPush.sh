docker build . -f dockerFiles/Dockerfile -t kwraight/itk-pdb-template:1.0
docker push kwraight/template-app:1.0
docker build . -f dockerFiles/Dockerfile -t kwraight/itk-pdb-template:latest
docker push kwraight/template-app:latest
