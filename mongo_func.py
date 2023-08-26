from pymongo import MongoClient


class MongoOperations:
    def client(self):
        return MongoClient(host="http:127.0.0.1")

    def get_db(self, db_name: str):
        client = self.client()
        return client.get_database(name=db_name)

    def aggregation(self, db_name, collection, pipeline):
        db = self.get_db(db_name)
        return db.get_collection(name=collection).aggregate(pipeline=pipeline)

    def insert_documents(self, db_name, collection, data: list):
        assert type(data) == list
        db = self.get_db(db_name)
        return db.get_collection(collection).insert_many(data)
