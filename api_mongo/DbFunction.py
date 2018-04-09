from connection import connect
from bson.objectid import ObjectId

class DbFunc:

	def __init__(self):
		try:
			self.db = connect()
			print("Database ready...")
		except Exception as er:
			print(str(er))

	def get_people(self):
		try:
			db = self.db.people
			
			return db.find({})
		except Exception as er:
			print(str(er))

	def add_people(self, first_name, last_name, email):
		try:
			db = self.db.people

			return db.insert_one({"first_name": first_name, "last_name": last_name, "email": email}).inserted_id
		except Exception as er:
			print(str(er))

	def get_people_by_name(self, name):
		try:
			db = self.db.people
			
			return db.find({"first_name": name})
		except Exception as er:
			print(str(er))

	def update_people(self, id_people, first_name, last_name, email):
		try:
			db = self.db.people

			return db.update_one(
					{ "_id": ObjectId(id_people)},
					{ "$set": { "first_name": first_name, "last_name": last_name, "email": email }}
				)
		except Exception as er:
			print(str(er))

	def delete_people(self, id_people):
		try:
			db = self.db.people

			return db.delete_one({"_id": ObjectId(id_people)})
		except Exception as er:
			print(str(er))

if __name__ == '__main__':
	db = DbFunc()
else:
	DbFunc()