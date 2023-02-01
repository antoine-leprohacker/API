# API

By **Christian Hasbani** and **Antoine Chenevier**

Student at ESIREM in 4A ILC

 **Objectif :** Create a Flask API for CRUD management of a transaction system

 [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  

### Workflows

 [Pull](./.github/workflows/on_pull.yml) : GitHub action pull
  
 [Push](./.github/workflows/on_push.yml) : GitHub action push
  
## Documentation

We have a list of transactions, each transaction is a tuple (P1, P2, t,s,hash), where s is equal to the amount of money transferred from person P1 to person P2 at time t and hash is the key of the tuple.

 We have the current date in second since 01-01-2023.

## curl

Here are examples of `curl` commands to access the different routes in [app.py](./app.py)

### route `/display_list`

```python
@app.route("/display_list", methods=['GET'])
def getList():
```

```bash
curl -X GET http://localhost:5000/display_list
```

Function to return all of the dictionary

### route `/display_list/<Person>`

```python
@app.route("/display_list/<Person>", methods=['GET'])
def getListPerson(Person):
  ...
```

```bash
curl -X POST -d "Person=person" http://localhost:5000/display_list/<Person>
```

Function to return all of the dictionary of a person

### route `/display_solde/<Person>`

```python
@app.route("/display_solde/<Person>", methods=['GET'])
def getSolde(Person):
  ...
```

```bash
curl -X GET -d "Person=person" http://localhost:5000/display_solde/<Person>
```

Function to display  the solde of a person

### route `/add_element/`

```python
@app.route("/add_element/", methods=['POST','GET'])
def addElement():
```

```bash
curl -X GET http://loccurl -X POST http://localhost:5000/add_element/ -d "p1=christian&p2=antoine&solde=10"
```

Function to add an element in the dictionary

### route `/importeCSV`

```python
@app.route("/importeCSV", methods=['GET'])
def importeCSV():
  ...
```

```bash
curl -d  "filePath=tab.csv" -X  GET http://localhost:5000/importeCSV

```

Function to import a CSV file

### route `/hash_verification`

```python
@app.route("/hash_verification", methods=['GET'])
def hash_vefication():
  ...
```

```bash
curl -X GET http://localhost:5000/hash_verification
```

Hash verification

### route `/hash_correction`

```python
@app.route("/hash_correctionn", methods=['GET'])
def hash_vefication():
  ...
```

```bash
curl -X GET http://localhost:5000/hash_correction
```

Hash correction

## Building the docker image
We built the docker image using the following command in the terminal
```bash
docker build -t flask-app . 
```
Using the ```docker images``` command

![image](https://user-images.githubusercontent.com/117630923/216095191-fbe11e6c-5246-442c-90dd-5fe508c28e82.png)


## Running the docker image in a container
```bash
sudo docker run -it -p 5000:5000 -d flask-app
```
This will lauch our flask application on localhost port ```5000```
![image](https://user-images.githubusercontent.com/117630923/216095866-b40bdcd5-f990-47d4-befc-acd778ee1cdd.png)
We use ```docker ps``` to display running containers

We can see at the end we have the follow result
![image](https://user-images.githubusercontent.com/117630923/216096355-1586072b-1534-4aba-bf6e-84cf299e14df.png)


## Update
We have already implemented all the features in the app.py file  before releasing  
