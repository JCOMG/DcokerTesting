# Simple build Docker with Github actions 
This is a simple Flask-based system with Docker and Github actions.

Python version: 3.8

## Feature 
- Building a simple flask-based web application
- Creating docker image and container to run the application
- Push into Github Actions to run the tests

## How to use - Run in Docker
Use below curl command to call API

Required 
- install docker
  
## Steps 
### step 1 : pull docker image

```bash

docker pull jimmyomg/my-flask-version2

```

### step 2 : run docker image

```bash

docker run -it --rm -p 5000:5000 jimmyomg/my-flask-version2

```
### step 3 : execute curl

```bash
curl -X GET http://127.0.0.1:5000/health
```

## Tech 
- Python
- Flask
- RESTful API
- Docker
- Github Action


