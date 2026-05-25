"""
User DAO MongoDB (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User

class UserDAOMongo:
    def __init__(self):
        try:
            load_dotenv(dotenv_path=".env")
            host = os.getenv("MONGODB_HOST")
            username = os.getenv("DB_USERNAME")
            password = os.getenv("DB_PASSWORD")
            self.client = MongoClient(host=host, port=27017, username=username, password=password)
            self.collection = self.client["labo01_db"]["users"]
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        return [User(doc["_id"], doc["name"], doc["email"]) for doc in self.collection.find()]

    def insert(self, user):
        """ Insert given user into MongoDB """
        result = self.collection.insert_one({"name": user.name, "email": user.email})
        return result.inserted_id

    def update(self, user):
        """ Update given user in MongoDB """
        self.collection.update_one(
            {"_id": user.id},
            {"$set": {"name": user.name, "email": user.email}}
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.collection.delete_one({"_id": user_id})

    def close(self):
        self.client.close()
