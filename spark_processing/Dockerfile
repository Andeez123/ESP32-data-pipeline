# base spark image
FROM bitnami/spark:3.5-debian-11

USER root

# runs linux command as base is debian, update system packages, installs and upgrades pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install --upgrade pip

# set working directory to /spark_processing
WORKDIR /spark_processing

# copy requirements to working directory
COPY requirements.txt .

# install required packages
RUN pip install --no-cache-dir -r requirements.txt

# copy files from current host directory to container directory
COPY . .

# run the file
CMD [ "python", "spark_consumer.py" ]
