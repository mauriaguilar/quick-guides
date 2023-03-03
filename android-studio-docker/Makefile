IMAGE=android
VERSION=2022
ANDROID_FOLDER=android-studio-2022.1.1.21-linux
ANDROID_ROOT=$(PWD)/$(ANDROID_FOLDER)/android-studio
COMMAND=/android-studio/bin/studio.sh 
UID=$(shell id -u)
USER=dev

run: del
	xhost +
	docker run -it --name=editor \
	 --net=host --env="DISPLAY" -it --volume="$(HOME)/.Xauthority:/root/.Xauthority:rw" -v /tmp/.X11-unix:/tmp/.Y11-unix \
	 -v /dev/kvm:/dev/kvm \
	 -u $(USER) \
	 -v $(ANDROID_ROOT):/android-studio \
	 -v $(PWD)/$(USER)/Android:/home/$(USER)/Android \
	 -v $(PWD)/$(USER)/AndroidStudioProjects:/home/$(USER)/AndroidStudioProjects \
	 $(IMAGE):$(VERSION) $(COMMAND)

build:
	docker build . -t $(IMAGE):$(VERSION)
	@mkdir -p $(USER) && echo "build finished."

del:
	docker rm -f editor

res:
	docker restart editor

in:
	docker exec -it editor bash
