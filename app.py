from database import Database
from user import User

Database.initialise(database='learning', user='postgres', password='35825328', host='localhost')

my_user = User('glocky.glock@gmail.com', 'Glocky', 'Glock', None)

my_user.save_to_db()


user_from_db = User.load_from_db_by_email('glocky.glock@gmail.com')

print(user_from_db)

