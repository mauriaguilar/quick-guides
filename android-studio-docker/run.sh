#!/usr/bin/env bash

IMAGE=$1

# clean old containers
docker rm android_studio_container > /dev/null || echo ''

# Run Android-Studio with empty configurations
docker run -it --name=android_studio_container \
--net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -v /tmp/.X11-unix:/tmp/.Y11-unix \
mauriaguilar/android-studio:latest /android-studio/bin/studio.sh ; \
  docker commit android_studio_container $IMAGE
