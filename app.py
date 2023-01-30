from flask import Flask, request
app = Flask(__name__)
transaction = [("Antoine","Christian",1000,10),("Antoine","Christian",200,200)]
#time is 
# Function to return all of the dictionary
@app.route("/display_list", methods=['GET'])
def getList():
    if request.method == 'GET':
        transaction.sort()
        return str(transaction)

# Function to return all of the dictionary of a person
@app.route("/display_list/<Person>", methods=['GET'])
def getListPerson(Person):
    if request.method == 'GET':
        transaction.sort()
        result = ""
        for i in transaction:
            if i[0] == Person:
                result+= str(i)
            if i[1] == str(Person):
                result+= str(i)
        if(result == ""):
            return "Person not found"
        else:
            return result

# Function to display  the solde of a person
@app.route("/display_solde/<Person>")
def getSolde(Person):
    solde = 0
    for i in transaction:
        if i[0] == Person:
            solde -= i[3]
        if i[1] == Person:
            solde += i[3]
    return str(solde)

# Function to add an element in the dictionary
@app.route("/add_element/", methods=['POST','GET'])
def addElement():
    if request.method == 'POST':
        person1=str(request.form.get("p1"))    
        person2=str(request.form.get("p2"))
        time=int(request.form.get("time"))
        solde=int(request.form.get("solde"))
        add = (person1,person2,time,solde)
        transaction.append(add)
        return "You have successfully added a new element:" + str(add)
    return "You have"


if __name__ =='__main__':
    app.run()