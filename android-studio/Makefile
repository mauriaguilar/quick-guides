IMAGE=android
VERSION=2022
ANDROID_FOLDER=android-studio-2022.1.1.21-linux
ANDROID_ROOT=$(PWD)/$(ANDROID_FOLDER)/android-studio
COMMAND=/android-studio/bin/studio.sh 
UID=$(shell id -u)
USER=root


run: del
	xhost +
	# echo 'export PATH="$$PATH:/flutter/bin"' >> $(USER)/.bashrc
	# echo 'export PATH="$$PATH:/android-studio"' >> $(USER)/.bashrc
	docker run -it --name=editor \
	 --net=host --env="DISPLAY" -d --privileged --volume="$(HOME)/.Xauthority:/root/.Xauthority:rw" -v /tmp/.X11-unix:/tmp/.Y11-unix \
	 -v /dev/kvm:/dev/kvm \
	 -v /dev/bus/usb:/dev/bus/usb \
	 -u $(USER) \
	 -v $(ANDROID_ROOT):/android-studio \
	 -v $(PWD)/$(USER)/Android:/$(USER)/Android \
	 -v $(PWD)/$(USER)/AndroidStudioProjects:/$(USER)/AndroidStudioProjects \
	 -v $(PWD)/$(USER)/StudioProjects:/$(USER)/StudioProjects \
	 -v $(PWD)/$(USER)/Sdk:/$(USER)/Sdk \
	 -v $(PWD)/$(USER)/.android:/$(USER)/.android \
	 -v $(PWD)/$(USER)/.cache:/$(USER)/.cache \
	 -v $(PWD)/$(USER)/.config:/$(USER)/.config \
	 -v $(PWD)/$(USER)/.java:/$(USER)/.java \
	 -v $(PWD)/$(USER)/.local:/$(USER)/.local \
	 -v $(PWD)/$(USER)/.pub-cache:/$(USER)/.pub-cache \
	 $(IMAGE):$(VERSION) $(COMMAND)


	@# For Gradle: add -e GRADLE_USER_HOME='/dev/gradle/'
	@# --mount type=bind,source=$(PWD)/$(USER)/.flutter,target=/$(USER)/.flutter \

check:
	docker run -it --rm $(IMAGE):$(VERSION) bash

build:
	docker build . -t $(IMAGE):$(VERSION)
	@mkdir -p $(USER) && echo "build finished."

b: build

del:
	docker rm -f editor

res:
	docker restart editor

in:
	docker exec -it editor bash

check-virtualization:
	grep -E --color=auto 'vmx|svm' /proc/cpuinfo

fix-virtualization:
	sudo usermod -aG kvm root
	sudo chown root:root -R /dev/kvm
	sudo chmod 777 /dev/kvm
