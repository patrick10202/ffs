from database import *
import random
from datetime import date

def clearConsole():
    for x in range(20):
        print("\n")

class Advisor:
  def updateOwnPassword():
    newPassword = input("Input new password: ")
    c.execute("UPDATE advisors SET password=:newPassword WHERE username=:usedUsername", {'newPassword': newPassword, 'usedUsername': returnUsedUsername()})
    conn.commit()
    clearConsole()
    print("Password updated!")

  def registerNewMember():
    firstName = input("Enter firstname: ")
    lastName = input("Enter lastname: ")
    streetName = input("Enter Streetname: ")
    houseNumber = input("Enter housenumber: ")
    zipCode = input("Enter zipcode: ")
    city = input("Enter city: ")
    email = input("Enter email: ")
    mobilePhone = input("Enter mobilephone: ")
    #checksum
    def checksum():
      numb = random.randint(100000000, 999999999)
      checkdigit = 0
      for digit in str(numb):
        checkdigit = checkdigit + int(digit)
      checkdigit = checkdigit % 10
      finalnum = (numb * 10) + checkdigit

      c.execute("SELECT * FROM members WHERE memberId=:memberId", {'memberId': finalnum})
      listOfequalNums = c.fetchall()
      if listOfequalNums:
        checksum()
      else:
        with conn:
          c.execute("INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (firstName, lastName, streetName, houseNumber, zipCode, city, email, mobilePhone, date.today(), finalnum))
          clearConsole()
          print("Member added!")
    checksum()

  def modifyMember():
    c.execute("SELECT * FROM members")
    membersList = c.fetchall()
    x = 1
    for member in membersList:
      print(f"{x}. {member}")
      x = x + 1
    selectedNumber = int(input("Select a number of a member that you want to modify: "))
    print("""What values do you want to modify?
1. Firstname
2. Lastname
3. Streetname
4. Housenumber
5. Zipcode
6. City
7. Email
8. Phonenumber
""")
    inp = input("Enter choice: ")
    if inp == '1':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET firstName=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
      clearConsole()
      print("Member modified!")
    elif inp == '2':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET lastName=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
    elif inp == '3':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET streetName=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
    elif inp == '4':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET houseNumber=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
    elif inp == '5':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET zipCode=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
    elif inp == '6':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET city=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
    elif inp == '7':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET email=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
    elif inp == '8':
      inp = input("Enter new: ")
      c.execute("UPDATE members SET mobilePhone=:inp WHERE firstName=:firstName", {'inp': inp, 'firstName': membersList[selectedNumber - 1][0]})
      conn.commit()
  
  def searchMember():
    inp = input("enter search: ")
    c.execute("SELECT * FROM members WHERE firstName LIKE :inp OR lastName LIKE :inp OR streetName LIKE :inp OR houseNumber LIKE :inp OR zipCode LIKE :inp OR city LIKE :inp OR email LIKE :inp OR mobilePhone LIKE :inp", {'inp': '%'+inp+'%'})
    memberlist = c.fetchall()
    for x in memberlist:
      print(f"""\n{x[0]} {x[1]}
{x[2]} {x[3]} {x[4]} {x[5]}
{x[6]}
{x[7]}""")
    print("\n")

class SystemAdmin(Advisor):
  def updateOwnPassword():
    newPassword = input("Input new password: ")
    c.execute("UPDATE sysadmins SET password=:newPassword WHERE username=:usedUsername", {'newPassword': newPassword, 'usedUsername': returnUsedUsername()})
    conn.commit()
    clearConsole()
    print("Password updated!")

  def checkListOfUsersAndRoles():
    pass

  def registerNewAdvisor():
    username = input("Enter username: ")
    password = input("Enter password: ")
    firstName = input("Enter firstname: ")
    lastName = input("Enter lastName: ")
    c.execute("INSERT INTO advisors VALUES (?, ?, ?, ?, ?)", (username, password, firstName, lastName, date.today()))
    conn.commit()
    print("Advisor added!")

  def modifyAdvisor():
    c.execute("SELECT * FROM advisors")
    advisorsList = c.fetchall()
    x = 1
    for advisor in advisorsList:
      print(f"{x}. {advisor}")
      x = x + 1
    selectedNumber = int(input("Select a number of a advisor that you want to modify: "))
    print("""What values do you want to modify?
1. Username
2. Password
3. Firstname
4. Lastname
""")
    inp = input("Enter choice: ")
    if inp == '1':
      inp = input("Enter new: ")
      c.execute("UPDATE advisors SET username=:inp WHERE username=:username", {'inp': inp, 'username': advisorsList[selectedNumber - 1][0]})
      conn.commit()
      print("Advisor updated!")
    elif inp == '2':
      inp = input("Enter new: ")
      c.execute("UPDATE advisors SET password=:inp WHERE username=:username", {'inp': inp, 'username': advisorsList[selectedNumber - 1][0]})
      conn.commit()
      print("Advisor updated!")
    elif inp == '3':
      inp = input("Enter new: ")
      c.execute("UPDATE advisors SET firstName=:inp WHERE username=:username", {'inp': inp, 'username': advisorsList[selectedNumber - 1][0]})
      conn.commit()
      print("Advisor updated!")
    elif inp == '4':
      inp = input("Enter new: ")
      c.execute("UPDATE advisors SET lastName=:inp WHERE username=:username", {'inp': inp, 'username': advisorsList[selectedNumber - 1][0]})
      conn.commit()
      print("Advisor updated!")

  def deleteAdvisor():
    c.execute("SELECT * FROM advisors")
    advisorsList = c.fetchall()
    x = 1
    for advisor in advisorsList:
      print(f"{x}. {advisor}")
      x = x + 1
    selectedNumber = int(input("Select a number of a advisor that you want to delete: "))
    c.execute("DELETE FROM advisors WHERE username=:selectedNumber", {'selectedNumber': advisorsList[selectedNumber - 1][0]})
    conn.commit()
    print("advisor deleted!")

  def resetAdvisorPassword():
    print("reset advisor password")
  
  def createSystemBackup():
    pass

  def restoreSystemBackup():
    pass

  def seeLogs():
    pass

  def deleteMember():
    c.execute("SELECT * FROM members")
    membersList = c.fetchall()
    x = 1
    for member in membersList:
      print(f"{x}. {member}")
      x = x + 1
    selectedNumber = int(input("Select a number of a member that you want to delete: "))
    c.execute("DELETE FROM members WHERE firstName=:selectedNumber", {'selectedNumber': membersList[selectedNumber - 1][0]})
    conn.commit()
    print("Member deleted!")


class SuperAdmin(SystemAdmin):
  def registerNewSystemAdmin():
    print("registreer nieuwe systemadmin")
  
  def modifySystemAdmin():
    print("modify systemadmin")

  def deleteSystemAdmin():
    print("delete systemadmin")

  def resetSystemAdminPassword():
    print("reset system admin password")