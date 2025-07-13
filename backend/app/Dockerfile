# select base image for python
FROM python:3.13

# set the directory that the container starts in
WORKDIR /app

COPY requirements.txt .

# run pip install to install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy all the files in app(host) to app(docker env)
COPY . .

# start the main.py file inside the container
CMD [ "python", "main.py" ]