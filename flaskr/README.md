FLASK APP FOR "FRUIT-RECOGNITION"
===
uses KERAS, TENSORFLOW and FLASK

SETUP
---
1. create an virtual python environment
```
$ python3.6 -m venv virtPyEnv
```
2. Use the creted environment
```
$ source virtPyEnv/bin/activate
```
3. install packages with pip
```
$ pip install flask keras tensorflow
```
// have a look at initFlask.sh

start up app
---
1. activate the virtual python environment
```
$ source virtPyEnv/bin/activate
```
2. start the app and set the Variable "ENV"
```
$ export ENV=local && python src/main.py
```
// have a look at startFlask.sh

start as docker container
---
1. create image 
```
$ docker build -t codecamp2019 .
```
2. run the container (with rm the container will be deleted after it is stopped)
```
$ docker run --rm codecamp2019
```
