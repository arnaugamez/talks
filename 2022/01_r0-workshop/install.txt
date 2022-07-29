Build the docker image from Dockerfile
---
docker build -t r0workshop .


Run the docker image exposing jupyter-lab instance on localhost:8888
---
docker run -p 8888:8888 r0workshop
