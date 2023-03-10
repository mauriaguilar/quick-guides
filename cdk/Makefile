IMAGE=cdk
VERSION=2023
CONTAINER_NAME=cdk
COMMAND=bash || sh
UID=$(shell id -u)
USER=root


run: del
	xhost +
	docker run -it --name=$(CONTAINER_NAME) \
	 --net=host --env="DISPLAY" -d --volume="$(HOME)/.Xauthority:/root/.Xauthority:rw" -v /tmp/.X11-unix:/tmp/.Y11-unix \
	 -v $(PWD)/infrastructure:/infrastructure \
	 -u $(USER) \
	 $(IMAGE):$(VERSION) $(COMMAND)

check:
	docker run -it --rm $(IMAGE):$(VERSION) bash

build:
	docker build . -t $(IMAGE):$(VERSION)
	@mkdir -p $(USER) && echo "build finished."

b: build

del:
	docker rm -f $(CONTAINER_NAME)

res:
	docker restart $(CONTAINER_NAME)

in:
	docker start $(CONTAINER_NAME)
	docker exec -it $(CONTAINER_NAME) bash || sh

