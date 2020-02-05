# recipe-app-api
*Recipe app api source code
udemy course: Create an advanced REST API with Python, Django REST Framework and Docker using Test Driven Development (TDD)*

### Django project consists 2 modules (apps):
#### core
- custom user model that supports using email instead of username
- command to pause execution until database is available (Docker service for db is started)
#### user
- API for user management (rest_framework)
- use rest_framework.generics.CreateAPIView as view for /user/create/
- use rest_framework.serializers.ModelSerializer as serializer for custom user model

### Other files
#### Dockerfile
Text document containing all the commands a user could call on the command line to assemble an image. Docker can build images automatically by reading instructions from Dockerfile

#### docker-compose.yml
docker-compose is a tool for running Docker application with multiple services (containers).
- Services in this project are **app** and **db**. 
- **volumes:** files inside Docker image are automatically upapdated without restarting Docker
- **commands:** run command to start Django server (inc. migration and waiting for db service)
  
#### travis.yml
Travis is continuous integration service, that can be activated for given github repository. It can be configured to run unit tests every time a new commit is pushed to repository.
- Uses **services:** - docker - to build Docker image for testing
- runs unit tests for **core** and **user** modules
- runs flake8 for checking code syntax against PEP 8 (Style Guide for Python Code)
