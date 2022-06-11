import sqlite3

def returnUsedUsername():
    return usedUsername
usedUsername = "test"

conn = sqlite3.connect('database.db')

c = conn.cursor()
try:
    c.execute("""CREATE TABLE members (
                firstName text,
                lastName text,
                streetName text,
                houseNumber int,
                zipCode text,
                city text,
                email text,
                mobilePhone text,
                registrationDate text,
                memberId text
                )""")
except:
    pass

try:
    c.execute("""CREATE TABLE advisors (
                username text,
                password text,
                firstName text,
                lastName text,
                registrationDate text
                )""")
except:
    pass

try:
    c.execute("""CREATE TABLE sysadmins (
                username text,
                password text
                )""")
except:
    pass

def advisorLogin():
    username = input("Input username: ")
    password = input("Input password: ")
    c.execute("SELECT * FROM advisors WHERE username = :username AND password = :password", {'username': username, 'password': password})
    account = c.fetchall()
    if account:
        global usedUsername
        usedUsername = username
        return True
    else:
        print("Account not found")

def sysAdminLogin():
    username = input("Input username: ")
    password = input("Input password: ")
    c.execute("SELECT * FROM sysadmins WHERE username = :username AND password = :password", {'username': username, 'password': password})
    account = c.fetchall()
    if account:
        global usedUsername
        usedUsername = username
        return True
    else:
        print("Account not found")

def superAdminLogin():
    username = input("Input username: ")
    password = input("Input password: ")
    if username == 'superadmin' and password == 'Admin321!':
        return True
    else:
        print("Account not found")

# c.execute("SELECT * FROM members")
# c.execute("INSERT INTO sysadmins VALUES ('admin', 'admin')")

# print(c.fetchall())

conn.commit()

# conn.close()