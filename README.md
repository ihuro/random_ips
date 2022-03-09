# random_ips

**Random IP addresses detail generator**

The idea is to generate random IP address information to use as examples of network calculations.

## Example

    $ python random_ips/api.py -q 15
    
    IP               Network         Netmask Decimal      Netmask Bits  Broadcast        Host min        Host max
    ---------------  --------------  -----------------  --------------  ---------------  --------------  ---------------
    255.158.41.235   255.158.41.192  255.255.255.192                26  255.158.41.255   255.158.41.193  255.158.41.254
    45.237.77.218    45.224.0.0      255.240.0.0                    12  45.239.255.255   45.224.0.1      45.239.255.254
    139.139.67.14    136.0.0.0       252.0.0.0                       6  139.255.255.255  136.0.0.1       139.255.255.254
    174.217.20.50    174.216.0.0     255.248.0.0                    13  174.223.255.255  174.216.0.1     174.223.255.254
    34.161.84.42     32.0.0.0        252.0.0.0                       6  35.255.255.255   32.0.0.1        35.255.255.254
    80.208.223.10    80.208.223.0    255.255.255.224                27  80.208.223.31    80.208.223.1    80.208.223.30
    177.33.202.100   177.32.0.0      255.248.0.0                    13  177.39.255.255   177.32.0.1      177.39.255.254
    227.58.187.93    227.58.160.0    255.255.224.0                  19  227.58.191.255   227.58.160.1    227.58.191.254
    129.72.84.156    129.72.0.0      255.255.128.0                  17  129.72.127.255   129.72.0.1      129.72.127.254
    80.82.156.147    80.82.156.128   255.255.255.192                26  80.82.156.191    80.82.156.129   80.82.156.190
    38.119.215.213   38.112.0.0      255.240.0.0                    12  38.127.255.255   38.112.0.1      38.127.255.254
    173.233.255.127  128.0.0.0       128.0.0.0                       1  255.255.255.255  128.0.0.1       255.255.255.254
    6.68.80.45       6.68.80.0       255.255.240.0                  20  6.68.95.255      6.68.80.1       6.68.95.254
    229.157.77.155   229.128.0.0     255.224.0.0                    11  229.159.255.255  229.128.0.1     229.159.255.254
    117.211.20.42    117.211.20.0    255.255.252.0                  22  117.211.23.255   117.211.20.1    117.211.23.254

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
