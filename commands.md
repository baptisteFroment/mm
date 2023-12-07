$ docker build -t mon-caddy .
$ docker run -d -p 80:80 -p 443:443 mon-caddy