# Diseases Cure Finder Based On Image

A simple implementation of OpenCV and Google Cloud Vision to find out the what kind of disease can be cured by that particular plant which was given as an image input.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 2.7
* Flask
* Google Vision Api Account

    - Ubuntu
```
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python python-pip
pip install flask
pip install requests
pip install json
```

    - Mac


brew install python
sudo pip install flask
sudo pip install requests
sudo pip install json


### Installing

A step by step series of examples that tell you have to get a development env running

- Clone the repository
```
git clone https://github.com/fizan2904/Plant-Disease-Vision
cd Plant-Disease-Vision
```

- Exporting google credentials
```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/jsonfile
```

- Starting the server
```
export FLASK_APP=app.py
export FLASK_DEBUG=1 //optional
flask run
```

## Running the tests

Open the browser and enter the url

```
http://localhost:5000/
```
Follow the on screen instructions