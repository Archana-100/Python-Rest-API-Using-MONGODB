# -*- coding: utf-8 -*-
"""
create CRUD REstful API from Student database using flask
@author: archna gaikwad
"""
#import required packages
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson import json_util

# creating the flask app
app = Flask(__name__)

# creating an API object
api = Api(app)

db_url= MongoClient("mongodb://localhost:27017/")

college_db=db_url["College"]
student_collection=college_db["Student2"]

class student_data(Resource):
#using get mothod ,we fetch data from mongodb database using api     
    def get(self): 
        try:
            self._jsom=request.get_json()
            self.post_data= list(student_collection.find({},{'_id':0}))#_id=0 means excluding _id column fetch remaining column from database 
            return jsonify({"result":self.post_data,"status":"success"})
        
        except Exception as e:
            responce = {"result":e,"status":"fail"}
            return jsonify(responce)
    
    def post(self): 
        #using post method , we insert new data into mongodb database using api
         try:
            _jsom=request.get_json()
            name=_jsom['name']
            address=_jsom.get('address') #using get method : if there is none value in address column it will return none instead of error message
            #print(name,address)
            records_counts = list(student_collection.find({'name':name},{'name':1}))
            if len(records_counts)==0:
                id_11 = student_collection.insert_one({'name':name,'address':address})
                #if user does not enter unique name so it will show message "Name already exists"
                return jsonify({"result":"record inserted successfully","status":"success"})
            else:
                return jsonify({"result":"Name already exists","status":"success"})
         except Exception as e:
            responce = {"result":e,"status":"fail"}
            return jsonify(responce) 
        
    def put(self):
        try:
            #using put method , we update record from mongodb database using api
            _jsom=request.get_json()
            name =_jsom.get('name')
            address_update=_jsom.get("update_address")
            upd = student_collection.update_one({'name':name},{"$set":{'address':address_update}})
            return jsonify({"result":"record updated successfully","status":"success"})
        except Exception as e:
            responce = {"result":e,"status":"fail"}
            return jsonify(responce)
    
    def delete(self):
        try:
            #using delete method ,we can delete existing record from mongodb database using api 
            data=request.get_json()
            name=data.get('name')
            print(name)
            rec= list(student_collection.find({'name':name}))
            if len(rec) > 0:
                delt=student_collection.delete_one({'name':name})
                return jsonify({"result":"record deleted successfully","status":"success"})
            else:
                return jsonify({"result":"record not found","status":"success"})
        except Exception as e:
            responce = {"result":e,"status":"fail"}
            return jsonify(responce)
            
     
# adding the defined resources along with their corresponding urls
api.add_resource(student_data, '/college_d')

if __name__ == '__main__':
    app.run(port=9091)
