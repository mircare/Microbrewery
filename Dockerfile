FROM debian:stable-slim
LABEL maintainer <torrisimirko@yahoo.com>

# satisfy the requirements
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git python3 -y
RUN apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# get Microbrewery
RUN git clone https://github.com/mircare/Microbrewery/ --depth 1 && rm -rf Microbrewery/.git

# initialize Microbrewery
WORKDIR /Microbrewery/scripts/Predict_BRNN
RUN chmod a+x Predict && cd .. && bash set_models.sh

WORKDIR /Microbrewery
