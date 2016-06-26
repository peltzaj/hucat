#!/usr/bin/python
import subprocess, hashlib
from flask import Flask, request, jsonify, json
from pymongo import MongoClient

#connection to local mongo
conn = MongoClient()
collection = conn.project.users

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def starting():

  if request.method == 'POST':
    if not request.json:
      return "POST - Please Provide a Correctly Encoded JSON"

    responses = [ ]
    #Load the json (no error checking at this point, could allow for injection)
    try:
        requests = json.loads(request.data)
    except ValueError as e:
        return "POST - Please Provide a Correctly Encoded JSON"

    #loop through each json and do the needful
    for index, data in enumerate(requests):
      
      #not needed but nice to layout
      uid = data['uid']
      name = data['name']
      date = data['date']
      md5s = data['md5checksum']

      # create the string and get md5
      testdata = uid + "|" + name + "|" + date
      testmd5 =  hashlib.md5(testdata).hexdigest()

      #compare the md5s and insert if matching, send back error if not
      if md5s == testmd5:
        collection.insert(data)
        answer = 1
      else:
        answer = 0
      #aggregate each json object
      responses.append({"uid": uid,"successfullyAdded": answer})

    return json.dumps(responses)

  if request.method == 'GET':
    if request.json:
      return "GET - Please Provide a Parameters"

    #load the paramters (no error checking at this point, could allow for injection or null data)
    data = request.args
    uid = data['uid']
    date = ".*" + data['date'] + ".*"

    #start your looping
    counter = 0
    cursor = collection.find({ 'uid' : uid, 'date' : {'$regex' : date } }  )
    for data in cursor:
      counter +=1
    
    #return nice json of the count
    return jsonify({'count': counter})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)