from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'snhupass'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31177
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,password,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            return insert.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            animalList = []
            data = self.database.animals.find(criteria,{"_id": False})
            for animal in data: #iterate to find all instances
                animalList.append(animal)
            
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return animalList
    
# Create method to implement the U in CRUD.
    def update(self, currentData, newData):
        if currentData is not None:
            dataUpdate = self.database.animals.update_many(currentData, {"$set": newData})
            return dataUpdate.modified_count #return update count
        else:
            raise Exception("Error. Could not be updated, no data given.")
            
# Create method to implement the D in CRUD.
    def delete (self, data):
        if data is not None:
            dataDelete = self.database.animals.delete_many(data)
            return dataDelete.deleted_count #return delete count
        else:
            raise Exception("Error. No data given")