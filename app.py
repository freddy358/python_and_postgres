from user import User

my_user = User('glocky.glock@gmail.com', 'Glocky', 'Glock', None)

my_user.save_to_db()


user_from_db = User.load_from_db_by_email('farid.bakhishli@gmail.com')

print(user_from_db)


my_user.save_to_db()