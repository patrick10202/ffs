import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

# c.execute("""CREATE TABLE members (
#             firstName text,
#             lastName text,
#             streetName text,
#             houseNumber int,
#             zipCode text,
#             city text,
#             email text,
#             mobilePhone text,
#             resignationDate text,
#             memberId text
#             )""")

# c.execute("INSERT INTO members VALUES ('patrick', null, null, null, null, null, null, null, null, null)")
# c.execute("SELECT * FROM members")

print(c.fetchall())

conn.commit()

conn.close()