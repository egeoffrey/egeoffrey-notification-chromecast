### EGEOFFREY ###

### define base image
ARG SDK_VERSION
ARG ARCHITECTURE
FROM egeoffrey/egeoffrey-sdk-alpine:${SDK_VERSION}-${ARCHITECTURE}

### install module's dependencies
RUN apk update && apk add python3 py3-pip nginx && rm -rf /var/cache/apk/*
RUN pip3 install pychromecast gtts

### copy files into the image
COPY . $WORKDIR

