# random_ips

**Random IP addresses detail generator**

The idea is to generate random IP address information to use as examples of network calculations.

## Example

##### Text command line

    $ python random_ips/api.py -q 3
    
    IP               Network         Netmask Decimal      Netmask Bits  Broadcast        Host min        Host max
    ---------------  --------------  -----------------  --------------  ---------------  --------------  ---------------
    255.158.41.235   255.158.41.192  255.255.255.192                26  255.158.41.255   255.158.41.193  255.158.41.254
    45.237.77.218    45.224.0.0      255.240.0.0                    12  45.239.255.255   45.224.0.1      45.239.255.254
    139.139.67.14    136.0.0.0       252.0.0.0                       6  139.255.255.255  136.0.0.1       139.255.255.254

##### Web API (JSON)

    $ curl http://127.0.0.1:8000/random_ips/2/json
    
    [
        {
            "IP": "128.218.135.198",
            "Network": "128.218.128.0",
            "Netmask Decimal": "255.255.128.0",
            "Netmask Bits": "17",
            "Broadcast": "128.218.255.255",
            "Host min": "128.218.128.1",
            "Host max": "128.218.255.254"
        },
        {
            "IP": "195.193.69.172",
            "Network": "195.193.69.172",
            "Netmask Decimal": "255.255.255.254",
            "Netmask Bits": "31",
            "Broadcast": "195.193.69.173",
            "Host min": "195.193.69.172/31",
            "Host max": "195.193.69.173"
        }
    ]

## Usage

### Command line

#### From source

* Install requirements
    
  `pip install -r requirements.txt`
    
* Execute script
    
  `python random_ips/api.py -h`

#### Using Docker

    docker build -t random_ips:latest .
    docker run --rm random_ips:latest cmd -h

### Web API

> Access http://localhost:8000

#### Run from source

    pip install -r requirements.txt
    hug -f random_ips/api.py

#### Docker

    docker build -t random_ips_app:latest .
    docker run --rm random_ips_app:latest web

#### Docker Compose

> Install docker and docker-compose https://docs.docker.com/compose/install/

    docker-compose build
    docker-compose up
