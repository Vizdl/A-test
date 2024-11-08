# docker 镜像名
DOCKER_IMAGE = atest:latest
# docker 容器名
DOCKER_CONTAINER = atest

# docker image
.PHONY += build-image run-image clean-image

# 在镜像外的操作
build-image :
	sudo docker build -t ${DOCKER_IMAGE} Docker --build-arg BUILDKIT_INLINE_CACHE=1 

run-image :
	sudo docker run \
	--privileged \
	--volume=${PWD}:/workdir:rw \
	-it ${DOCKER_IMAGE} \
	/bin/bash

clean-image :
	sudo docker rmi ${DOCKER_IMAGE}