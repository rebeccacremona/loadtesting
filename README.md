To start:

- `docker build -t loadtester:0.1 .`
- `docker swarm init`
- `docker stack deploy -c docker-compose.yml grid`

To stop:
- `docker stack rm grid`
