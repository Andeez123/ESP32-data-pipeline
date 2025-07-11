# **ESP32 Sensor Pipeline**

## 🚀 About
**ESP32 sensor pipeline** is a project which uses the WiFi capability of the ESP32 to send sensor data via the internet using HTTP protocols. This project aims to simulate real-life systems where embedded microcontrollers are reading data from the environment and storing that data in a database somewhere on the internet, and using APIs to query that data within the database. 

## ⚙️ Tech Stack
Currently, this project has an ESP32 with a DHT11 sensor wired to it. In the main.cpp file, the ESP32 connects to my local WiFi network, and sends json data to a Flask server I have running locally using HTTP POST request. This json data consists of the temperature measured, the time of data production and the id of the sensor. 

The Flask server is connected to a MongoDB database running on my machine. Connection, writing and reading from this mongodb database is done using PyMongo. The POST method is used to write data to the mongodb database. A sample GET request has been written, however this GET request is merely a sample request and will be updated in the future, to retrieve more useful data to be used, for web applications, data science, and machine learning model purposes. These API methods are tested using [Postman API testing software](https://www.postman.com/downloads/).

Sample data in MongoDB database:

![image](https://github.com/Andeez123/ESP32-sensor-pipeline/blob/main/461642985-e47b5611-2400-4cd1-9cd8-dfa500859a99.png)

## ✏️ Future Plans
Future plans include expanding the sensor array to capture more data, such as an Ultrasonic/Infrared sensor to capture distance data, Light sensors to capture brightness. As the number of sensors and data scales, Apache Kafka and Apache Spark may be used to process large volumes of data. The API methods need additional work to be able to query more useful data than the placeholder method currently setup, once the API methods have been setup correctly, a frontend will be built using React to display sensor data, along with some visualisations. Another functionality I have planned will be to host the database and the servers on a Raspberry PI, using Cloudfare services to serve my self hosted web application. 
