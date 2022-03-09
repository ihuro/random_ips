# random_ips

Random IP addresses generator

## Usage

### Command line

#### Install requirements

    pip install -r requirements.txt

#### Execute command

    python random_ips/api.py -h

##### Docker

    docker build -t random_ips:latest .
    docker run --rm random_ips_app:latest cmd -q 10  # command line output

### Web API

#### Docker

    docker build -t random_ips:latest .
    docker run --rm random_ips_app:latest web        # web API

#### Docker Compose

> Install docker and docker-compose https://docs.docker.com/compose/install/

    docker-compose build
    docker-compose up

#### Run local

    pip install -r requirements.txt
    hug -f random_ips/api.py
