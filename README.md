# **ESP32 Sensor Pipeline**

## 🚀 About
**ESP32 sensor pipeline** is a project which uses the WiFi capability of the ESP32 to send sensor data via the internet using HTTP protocols. This project aims to simulate real-life systems where embedded microcontrollers are reading data from the environment and storing that data in a database somewhere on the internet, and using APIs to query that data within the database. 

## ⚙️ Tech Stack
- [ESP32](https://www.espressif.com/en/products/socs/esp32) is chosen for its WiFi capabilities 
- [Flask](https://flask.palletsprojects.com/en/stable/) is chosen as it uses Python, which fits with the rest of the stack
- [Apache Kafka](https://kafka.apache.org/) industry standard for handling streaming data
- [Apache Spark](https://spark.apache.org/) industry standdard for data engineering pipelines
- [MongoDB](https://www.mongodb.com/) is chosen for its flexible structure type compared to traditional SQL databases
- [Docker](https://www.docker.com/) to eliminate dependency issues, Docker compose allows multiple containers to be maintained and run multiple services at once
  
Currently, this project has an ESP32 with a DHT11 sensor and a HC04 ultrasonic wired to it. In the main.cpp file, the ESP32 connects to my local WiFi network, and sends json data to a Flask server I have running locally using HTTP POST request. This json data consists of the temperature measured, distance measured, and the time of data production and the id of the sensor. 

The Flask server is configured to run in a docker container, along with Apache Kafka, Apache Spark and MongoDB. Docker Compose is used to run and manage all these containers at once. Docker is used in this application as I ran into multiple dependencies issues while running Apache Spark, hence a container is setup to simplify this process. The Flask application streams HTTP data to Kafka, which is the passed over to Spark streaming to process the data and store it in a local instance of MongoDB.

A sample GET request has been written, however this GET request is merely a sample request and will be updated in the future, to retrieve more useful data to be used, for web applications, monitoring, data science, and machine learning model purposes. These API methods are tested using [Postman API testing software](https://www.postman.com/downloads/).


## ✏️ Future Plans
Future plans include expanding the sensor array to capture more data, such as an Ultrasonic/Infrared sensor to capture distance data, Light sensors to capture brightness. As the number of sensors and data scales, Apache Kafka and Apache Spark may be used to process large volumes of data. The API methods need additional work to be able to query more useful data than the placeholder method currently setup, once the API methods have been setup correctly, a frontend will be built using React to display sensor data, along with some visualisations. Another functionality I have planned will be to host the database and the servers on a Raspberry PI, using Cloudfare services to serve my self hosted web application. 
