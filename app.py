from flask import Flask, request
import pandas as pd
app = Flask(__name__)
add1 = ("Antoine","Christian",1000,10)
add1 = ("Antoine","Christian",1000,10,hash(add1))
add2 = ("Antoine","Christian",200,200)
add2 = ("Antoine","Christian",200,200,hash(add2))
transaction = [add1,add2]
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
        add = (person1,person2,solde)
        add = (person1,person2,solde,hash(add))
        transaction.append(add)
        return "You have successfully added a new element:" + str(add)
    return "You have"

@app.route("/importeCSV", methods=['GET'])
def importeCSV():
    if request.method == 'GET':
      # CVS Column Names
      filePath = str(request.form.get("filePath"))
      print(filePath)
      col_names = ['first_person','second_person','date', 'value','hash']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names = col_names,engine='python',sep=';')

      # Loop through the Rows
      for i,row in csvData.iterrows():
        first_person = row['first_person']
        second_person = row['second_person']
        date = row['date']
        value =  row['value']
        hash = row['hash']
        add = (first_person,second_person,date,value,hash)
       
        transaction.append(add)
    return "ok"
if __name__ =='__main__':
    app.run()