from app import db
from bson.objectid import ObjectId

class DocumentModel:
    @staticmethod
    def get_all_documents():
        collection = db['sales']  # Replace with your collection name
        return list(collection.find({}, {'_id': 0}))

    @staticmethod
    def get_document_by_id(document_id):
        collection = db['sales']
        return collection.find_one({"_id": ObjectId(document_id)}, {'_id': 0})

    @staticmethod
    def insert_document(data):
        collection = db['sales']
        inserted_id = collection.insert_one(data).inserted_id
        return str(inserted_id)

    @staticmethod
    def update_document(document_id, data):
        collection = db['sales']
        result = collection.update_one({"_id": ObjectId(document_id)}, {"$set": data})
        return result.modified_count

    @staticmethod
    def delete_document(document_id):
        collection = db['sales']
        result = collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count
