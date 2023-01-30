from flask import Flask, request
from datetime import datetime
import pandas as pd
app = Flask(__name__)

# Get the current date in second since 01-01-2023
time = datetime(2023,1,1).timestamp() 

# Tuple initialization
add1 = ("Antoine","Christian",time,10)
add2 = ("Antoine","Christian",time,200)

# Add the hash in the tuple
add1 = ("Antoine","Christian",time,10,hash(add1))
add2 = ("Antoine","Christian",time,200,hash(add2))

# Dictionary initialization
transaction = [add1,add2]


# Function to return all of the dictionary
@app.route("/display_list", methods=['GET'])
def getList():
    if request.method == 'GET':

        # Sort the dictionary by date
        transaction.sort()
        return str(transaction)


# Function to return all of the dictionary of a person
@app.route("/display_list/<Person>", methods=['GET'])
def getListPerson(Person):
    if request.method == 'GET':

        # Initialize the result
        result = ""

        # Sort the dictionary by date
        transaction.sort()

        # Loop through the dictionary
        for i in transaction:

            # Check if the person in the dictonary is egal to the person in the GET
            if i[0] == Person:
                result+= str(i)
            if i[1] == str(Person):
                result+= str(i)

        # If the person is not in the dictionary
        if(result == ""):
            return "Person not found"

        # If the person is in the dictionary return the solde of transaction
        else:
            return result


# Function to display  the solde of a person
@app.route("/display_solde/<Person>")
def getSolde(Person):

    # Initialize the solde
    solde = 0

    # Loop through the dictionary
    for i in transaction:

        # Check if the person in the dictonary is egal to the person in the GET
        if i[0] == Person:

            # Remove the solde of the person
            solde -= i[3]
        if i[1] == Person:

            # Add the solde of the person
            solde += i[3]
    return str(solde)


# Function to add an element in the dictionary
@app.route("/add_element/", methods=['POST','GET'])
def addElement():
    if request.method == 'POST':

        # Get the data from the form
        person1=str(request.form.get("p1"))    
        person2=str(request.form.get("p2"))
        solde=int(request.form.get("solde"))

        # Get the current date in second since 2023
        time = datetime(2023,1,1).timestamp()

        # Add the element in a tuple
        add = (person1,person2,time,solde)
        add = (person1,person2,solde,time,hash(add))

        # Add the tuple in the dictionary
        transaction.append(add)

        return "You have successfully added a new element:" + str(add)
    return "You have not added a new element"


# Function to import a CSV file
@app.route("/importeCSV", methods=['GET'])
def importeCSV():
    if request.method == 'GET':

      # CVS Column Names
      filePath = str(request.form.get("filePath"))
      print(filePath)

    # CSV Column Names
    # This code is used to generate an array of column names for a dataframe
    # The column names are first_person, second_person, date, value, and hash

      col_names = ['first_person','second_person','date', 'value','hash']

      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names = col_names,engine='python',sep=';')

      # Loop through the Rows
      for i,row in csvData.iterrows():

        # Get the values from the row
        first_person = row['first_person']
        second_person = row['second_person']
        date = row['date']
        value =  row['value']
        hash = row['hash']

        # Add the element in a tuple
        add = (first_person,second_person,date,value,hash)
       
        # Add the tuple in the dictionary
        transaction.append(add)
    return "ok"


# Hash verification
@app.route("/hash_verification")
def hash_vefication():
    info = ""

    # Loop through the dictionary
    for i in transaction:

        # Delete the last parameters of the tuple
        a= (i[0],i[1],i[2],i[3])

        # Check if the hash is correct
        if i[4] != hash(a):
            info += "Hash is not correct for "+ str(i) + "\n"
        else:
            info += "Hash is correct for " + str(i) + "\n"
    return info


# Hash correction
@app.route("/hash_correction")
def hash_correction():
    info = ""
    for i in transaction:

        # Create a new tuple with the first three parameters of the tuple
        a= (i[0],i[1],i[2])

        # Check if the hash is correct
        if i[4] != hash(a):

            # If not correct, correct it
            info += "Hash is not correct for "+ str(i) + " the new hash is " + str(hash(a)) + "\n"
            i = (i[0],i[1],i[2],i[3],hash(a))
        else:
            
            # If correct, do nothing
            info += "Hash is correct for " + str(i) + "\n"
    return info

if __name__ =='__main__':
    app.run()