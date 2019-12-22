import mysql.connector
import sys
from datetime import datetime

cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="todo_app"
)
cursor = cnx.cursor()
ts = datetime.now()

print("Welcome to your todo app!")
username = input("May I know your name? ")

if username:
	print(f"What shall we do, {username}?")
	print("")
	print("1. View Todos \n2. Create new Todo \n3. Delete a Todo \n4. Alter a Todo")
	print("")
	user_choice = input()
	print("")

	if user_choice == '1':
		cursor.execute("SELECT * FROM todos")
		result = cursor.fetchall()
		print(f"This is all of your todos, {username}")
		for row in result:
			print(row[0], row[1], row[2])

	if user_choice == '2':
		todo = input("What do you have to do? ")
		cursor.execute("INSERT INTO todos (todo, timestamp) VALUES (%s, %s)", (todo, ts))
		cnx.commit()
		print(cursor.rowcount, "record(s) added")

	if user_choice == '3':
		cursor.execute("SELECT * FROM todos")
		result = cursor.fetchall()
		for row in result:
			print(row[0], row[1], row[2])

		delete = input(f"What record would you like deleted, {username}? ")
		cursor.execute("DELETE FROM todos WHERE id = %s",(delete,))
		cnx.commit()
		print(cursor.rowcount, "record(s) deleted")

	if user_choice == '4':
		cursor.execute("SELECT * FROM todos")
		result = cursor.fetchall()
		for row in result:
			print(row[0], row[1], row[2])

		number = input(f"What record should be changed, {username}? ")
		data = input(f"What should it become, {username}? ")

		cursor.execute("UPDATE todos SET todo = %s WHERE id = %s", (data, number))
		cnx.commit()
		print(cursor.rowcount, "record(s) affected")

else:
	print("You didn't specify your name!")
	sys.exit()

