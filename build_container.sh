#!/bin/bash
DOCKER_BUILDKIT=1 docker build -f Dockerfile -t mldemo .
docker run -p 12000:12000 mldemo