# PaulBoddy_FinalProject_4.py
# Paul Boddy


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import matplotlib.pyplot as plt
import pprint

# using defaults for connecting
uri = "mongodb://localhost:27017"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# we now rum commands through the client

# drop database
client.drop_database("sample_airbnb")
# get database names
client.list_database_names()
# get a database
db = client.senators


# get multiple docs -- pprint is 'pretty-print' and is a helpful utility function
for doc in collection.find({"limit": 9000}):
  pprint.pprint(doc)

###############################
coll=[db.AlexPadilla.json, db.BenCardin.json, db.BernieSanders.json,
      db.Budd.json, db.GeorgeMarshall.json, db.MichaelBennet.json,
      db.MitchMcconnell.json, db.MittRomney.json, db.RobertMenendez.json,
      db.Rubio.json, db.TedCruz.json, db.Van_Hollen.json]


##############################



# loop through collections within senators and count and store document count
## store in dictionary with .name and .count

# get a database
db = client.senators



c1 = coll[0] # 60
myquery = {"content": {"$regex": "emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[1] #31
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[2] #dead
myquery = {"content": {"$regex": "emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[3] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[4] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[5] #122
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[6] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[7] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[8] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[9] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[10] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

c1 = coll[11] #dead
myquery = {"content": {"$regex":"emissions"}}
mydoc = c1.count_documents(myquery)
print(mydoc)

# titles: adj buzzwords and names/ titles of people

names = ["AlexPadilla", "BenCardin", "MichaelBennet"]
doc_count=[60,31,122]


plt.bar(names, doc_count)
plt.xticks(rotation=280, fontsize=7)
plt.xlabel("Senators")
plt.ylabel("Total Press Releases with Emissions content")
plt.title("Total Press Releases w/ Emissions Content Per Senator")
plt.legend()
plt.show()


##############################

coll[0].count_documents({})
coll[1].count_documents({})
coll[2].count_documents({})
coll[3].count_documents({})
coll[4].count_documents({})
coll[5].count_documents({})
coll[6].count_documents({})
coll[7].count_documents({})
coll[8].count_documents({})
coll[9].count_documents({})
coll[10].count_documents({})
coll[11].count_documents({})

doc_count= [765,939,16,40,810,4196,129,175,810,578,1449,811]
names=["AlexPadilla", "BenCardin", "BernieSanders",
      "Budd", "GeorgeMarshall", "MichaelBennet",
      "MitchMcconnell", "MittRomney", "RobertMenendez",
      "Rubio", "TedCruz", "Van_Hollen"]

plt.bar(names, doc_count)
plt.xticks(rotation=280, fontsize=7)
plt.xlabel("Senators")
plt.ylabel("Total Press Releases")
plt.title("Total Press Releases Per Senator")
plt.legend()
plt.show()