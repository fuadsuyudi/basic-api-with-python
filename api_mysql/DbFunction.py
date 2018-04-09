from connection import connect

class DbFunc:

	def __init__(self):
		try:
			self.cursor, self.db = connect()
			print("Database ready...")
		except Exception as er:
			print(str(er))

	def get_people(self):
		try:
			self.cursor.execute("SELECT * FROM people")
			return self.cursor.fetchall()
		except Exception as er:
			print(str(er))

	def add_people(self, first_name, last_name, email):
		try:
			self.cursor.execute("INSERT INTO people(first_name,last_name,email) value('{}', '{}', '{}')".format(first_name, last_name, email))
			return self.db.commit()
		except Exception as er:
			self.db.rollback()
			print(str(er))

	def get_people_by_name(self, name):
		try:
			self.cursor.execute("SELECT * FROM people WHERE first_name LIKE '%{}%'".format(name))
			return self.cursor.fetchall()
		except Exception as er:
			print(str(er))

	def update_people(self, id_people, first_name, last_name, email):
		try:
			self.cursor.execute("UPDATE people SET first_name='{}' ,last_name='{}' ,email='{}' WHERE id='{}'".format(first_name, last_name, email, id_people))

			return self.db.commit()
		except Exception as er:
			self.db.rollback()
			print(str(er))

	def delete_people(self, id_people):
		try:
			self.cursor.execute("DELETE FROM people WHERE id='{}'".format(id_people))

			return self.db.commit()
		except Exception as er:
			self.db.rollback()
			print(str(er))

if __name__ == '__main__':
	db = DbFunc()
else:
	DbFunc()