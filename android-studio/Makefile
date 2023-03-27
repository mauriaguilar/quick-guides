ANDROID_STUDIO_VERSION=2022.1.1.21


IMAGE=android
VERSION=$(ANDROID_STUDIO_VERSION)
ANDROID_NAME=android-studio-$(ANDROID_STUDIO_VERSION)-linux
FILE=$(HOME)/Downloads/$(ANDROID_NAME).tar.gz
ANDROID_ROOT=$(HOME)/Downloads/android-studio
COMMAND=/android-studio/bin/studio.sh
UID=$(shell id -u)
USER=root
DATA_FOLDER=$(HOME)/Android

run: del
	xhost +
	docker run -it --name=editor \
	 --net=host --env="DISPLAY" -d --privileged --volume="$(HOME)/.Xauthority:/root/.Xauthority:rw" -v /tmp/.X11-unix:/tmp/.Y11-unix \
	 -v /dev/kvm:/dev/kvm \
	 -v /dev/bus/usb:/dev/bus/usb \
	 -u $(USER) \
	 -v $(ANDROID_ROOT):/android-studio \
	 -v $(DATA_FOLDER)/Android:/$(USER)/Android \
	 -v $(DATA_FOLDER)/AndroidStudioProjects:/$(USER)/AndroidStudioProjects \
	 -v $(DATA_FOLDER)/StudioProjects:/$(USER)/StudioProjects \
	 -v $(DATA_FOLDER)/Sdk:/$(USER)/Sdk \
	 -v $(DATA_FOLDER)/.android:/$(USER)/.android \
	 -v $(DATA_FOLDER)/.cache:/$(USER)/.cache \
	 -v $(DATA_FOLDER)/.config:/$(USER)/.config \
	 -v $(DATA_FOLDER)/.java:/$(USER)/.java \
	 -v $(DATA_FOLDER)/.local:/$(USER)/.local \
	 -v $(DATA_FOLDER)/.pub-cache:/$(USER)/.pub-cache \
	 $(IMAGE):$(VERSION) $(COMMAND)


	@# For Gradle: add -e GRADLE_USER_HOME='/dev/gradle/'
	@# --mount type=bind,source=$(PWD)/$(USER)/.flutter,target=/$(USER)/.flutter \

check:
	docker run -it --rm $(IMAGE):$(VERSION) bash

extract:
	@echo "Extract Android Studio from: $(FILE)"
	@if test -f "$(FILE)"; then \
	    echo "Android Studio has already been extracted."; \
	else \
	    cd $(HOME)/Downloads && tar -xzvf $(ANDROID_NAME).tar.gz; \
	fi

build: extract
	docker build . -t $(IMAGE):$(VERSION)
	@mkdir -p $(DATA_FOLDER) && echo "build finished."

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

