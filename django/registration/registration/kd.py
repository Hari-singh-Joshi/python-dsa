from pymongo import MongoClient

# Replace with your MongoDB connection URI
uri = "mongodb://username:password@localhost:27017/detail"

try:
    client = MongoClient(uri)
    db = client.get_database()
    print("Connected to MongoDB successfully.")
except Exception as e:
    print("Error connecting to MongoDB:", e)
