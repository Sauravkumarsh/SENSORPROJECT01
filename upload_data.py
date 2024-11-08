from pymongo.mongo_client import MongoClient
import pandas as pd
import json


#url
uri="mongodb+srv://kumarsaurav2905:lfK7jknW4X4D8Vs9@cluster0.5ijy3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to server
client=MongoClient(uri)

#create a database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\Saurav Kumar\Desktop\Sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
