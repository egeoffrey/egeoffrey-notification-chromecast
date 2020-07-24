### EGEOFFREY ###

### define base image
ARG SDK_VERSION
ARG ARCHITECTURE
FROM egeoffrey/egeoffrey-sdk-raspbian:${SDK_VERSION}-${ARCHITECTURE}

### install module's dependencies
RUN apt-get update && apt-get install -y python3 python3-pip nginx && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip3 install zeroconf==0.27.0 && pip3 install pychromecast gtts

### copy files into the image
COPY . $WORKDIR

