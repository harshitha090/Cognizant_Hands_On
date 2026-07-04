def get_user_from_db(user_id):
    database = {
        1: {"id": 1, "name": "Harshitha"},
        2: {"id": 2, "name": "Rahul"}
    }

    return database.get(user_id)