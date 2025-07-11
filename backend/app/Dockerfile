FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy all the files in app(host) to app(docker env)
COPY . .

CMD [ "python", "main.py" ]