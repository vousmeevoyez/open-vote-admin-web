## Run Copyright Management System in a docker container

### 1. Fetch the image on dockerhub
    docker run -d -p 5000:5000 --name gentelella --restart always afourmy/flask-gentelella

### 2. Go to http://server_address:5000/, create an account and log in

## Run Flask Gentelella in a docker container with nginx and a PostgreSQL database

### 1. Get the code
    git clone https://github.com/afourmy/flask-gentelella.git
    cd flask-gentelella

### 2. Start all services
    sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d

### 3. Go to http://server_address, create an account and log in
