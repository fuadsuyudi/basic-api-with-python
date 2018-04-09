from bottle import route, request, abort, run
from DbFunction import DbFunc
from helper import Helper

dbf = DbFunc()

@route('/')
def index():
    abort(401, 'Sorry, access denied.')

@route('/list-people')
def list_people():
    row_data = dbf.get_people()
    data = []

    try:
        for row in row_data:
            data.append({'first_name':row['first_name'],'last_name':row['last_name'],'email':row['email']})

        return Helper(True, None, data).raw()
    except Exception as er:
        abort(500, "Internal Server Error.")

@route('/add-people')
def add_people():
    try:
        insert_id = dbf.add_people(request.query.first_name, request.query.last_name, request.query.email)
        print insert_id

        return Helper(True, 'Sucess', {"id": str(insert_id)}).raw()
    except Exception as er:
		return Helper(False, str(er), None).raw()

@route('/get-people/<name>')
def get_people(name):
    row_data = dbf.get_people_by_name(name)
    data = []

    try:
        for row in row_data:
            data.append({'first_name':row['first_name'],'last_name':row['last_name'],'email':row['email']})

        return Helper(True, None, data).raw()
    except Exception as er:
        abort(500, "Internal Server Error.")

@route('/update-people/<id_people>')
def update_people(id_people):
    try:
        dbf.update_people(id_people, request.query.first_name, request.query.last_name, request.query.email)

        return Helper(True, 'Sucess', None).raw()
    except Exception as er:
        abort(500, "Internal Server Error.")

@route('/delete-people/<id_people>')
def delete_people(id_people):
    try:
        dbf.delete_people(id_people)
        
        return Helper(True, 'Sucess', None).raw()
    except Exception as er:
        abort(500, "Internal Server Error.")

run(host='127.0.0.1', port=8080, reloader=True)