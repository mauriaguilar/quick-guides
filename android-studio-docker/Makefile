IMAGE=android
VERSION=2022
ANDROID_FOLDER=android-studio-2022.1.1.21-linux
ANDROID_ROOT=$(PWD)/$(ANDROID_FOLDER)/android-studio
COMMAND=/android-studio/bin/studio.sh 
UID=$(shell id -u)
USER=root

run: del
	xhost +
	docker run -it --name=editor \
	 --net=host --env="DISPLAY" -d --privileged --volume="$(HOME)/.Xauthority:/root/.Xauthority:rw" -v /tmp/.X11-unix:/tmp/.Y11-unix \
	 -v /dev/kvm:/dev/kvm \
	 -v /dev/bus/usb:/dev/bus/usb \
	 -u $(USER) \
	 -v $(ANDROID_ROOT):/android-studio \
	 -v $(PWD)/$(USER):/$(USER) \
	 $(IMAGE):$(VERSION) $(COMMAND)
	# For Gradle: add -e GRADLE_USER_HOME='/dev/gradle/'

build:
	docker build . -t $(IMAGE):$(VERSION)
	@mkdir -p $(USER) && echo "build finished."

del:
	docker rm -f editor

res:
	docker restart editor

in:
	docker exec -it editor bash
