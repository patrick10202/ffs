from database import *
import random
from datetime import date

class Advisor:
  def updateOwnPassword():
    newPassword = input("Input new password: ")
    c.execute("UPDATE advisors SET password=:newPassword WHERE username=:usedUsername", {'newPassword': newPassword, 'usedUsername': returnUsedUsername()})
    conn.commit()
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
    checksum()

  def modifyMember():
    c.execute("SELECT * FROM members")
    membersList = c.fetchall()
    x = 1
    print(membersList[1])
    for member in membersList:
      print(f"{x}. {member}")
      x = x + 1
    input("Select a number of a member that you want to modify: ")
  
  def searchMember():
    inp = input("enter search: ")
    c.execute("SELECT * FROM members WHERE firstName LIKE :inp OR lastName LIKE :inp OR streetName LIKE :inp OR houseNumber LIKE :inp OR zipCode LIKE :inp OR city LIKE :inp OR email LIKE :inp OR mobilePhone LIKE :inp", {'inp': '%'+inp+'%'})
    memberlist = c.fetchall()
    for x in memberlist:
      print(f"""\n{x[0]} {x[1]}
{x[2]} {x[3]} {x[4]} {x[5]}
{x[6]}
{x[7]}""")

class SystemAdmin(Advisor):
  def updateOwnPassword():
    newPassword = input("Input new password: ")
    c.execute("UPDATE sysadmins SET password=:newPassword WHERE username=:usedUsername", {'newPassword': newPassword, 'usedUsername': returnUsedUsername()})
    conn.commit()
    print("Password updated!")

  def checkListOfUsersAndRoles():
    pass

  def registerNewAdvisor():
    print("registreer nieuwe advisor")
  
  def modifyAdvisor():
    print("modify advisor")

  def deleteAdvisor():
    print("delete advisor")

  def resetAdvisorPassword():
    print("reset advisor password")
  
  def createSystemBackup():
    pass

  def restoreSystemBackup():
    pass

  def seeLogs():
    pass

  def deleteMember():
    pass


class SuperAdmin(SystemAdmin):
  def registerNewSystemAdmin():
    print("registreer nieuwe systemadmin")
  
  def modifySystemAdmin():
    print("modify systemadmin")

  def deleteSystemAdmin():
    print("delete systemadmin")

  def resetSystemAdminPassword():
    print("reset system admin password")