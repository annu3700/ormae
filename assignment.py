import requests
import json
from pymongo import MongoClient
from ratelimit import limits
from time import sleep

#Constants declaration
FIVE_MINUTES = 300
API_URI = "https://jsonplaceholder.typicode.com/comments/"

#Get mongoDB client
client = MongoClient('localhost',27017)
db = client.ormae
col = db.comments

@limits(calls=300, period=FIVE_MINUTES)
def call_api(url):
    try:
        response = requests.get(url)
        ret = {}
        if response.status_code != 200:
            ret["status_code"] = 404
            return ret

        ret["status_code"] = 200
        ret["data"] = json.loads(response.text)

    except Exception as e:
        print(e.__str__())
    
    return ret
def update_data(comment):
    #print("Updating data")
    query_condition = {"id": comment["id"]}
    query_values = {"$set": {"postId": comment["postId"], "name": comment["name"], "email": comment["email"], "body": comment["body"]}}

    col.update_one(query_condition, query_values)

def insert_data(comment):
    #print("inserting data")
    query_values = {"id":comment["id"], "postId": comment["postId"], "name": comment["name"], "email": comment["email"], "body": comment["body"]}
    col.insert_one(query_values)

def save_data_to_mongo(data):
    print("Saving data to mongoDB")
    for comment in data:
        if col.find_one({"id": comment["id"]}):
            update_data(comment)
        else:
            insert_data(comment)

    sleep(0.1)

if __name__=="__main__":    
    while True:
        try:
            data = call_api(API_URI)
            print(f"status_code: {data['status_code']}" )
            if data["status_code"] == 200:
                save_data_to_mongo(data["data"])
            else:
                print("not")
        except Exception as e:
            print(e.__str__())
            pass

