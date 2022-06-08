from database import *

class Advisor:
  def updateOwnPassword():
    print("update own password")

  def registerNewMember():
    with conn:
      c.execute("INSERT INTO members VALUES ('patrick', null, null, null, null, null, null, null, null, null)")

  def modifyMember():
    print("modify member")
  
  def searchMember():
    r = c.execute(f"SELECT * FROM members WHERE firstName='patrick'")
    return r


class SystemAdmin(Advisor):
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

print('''
 ________                                 _                             
|_   __  |                               (_)                            
  | |_ \_|  __   _    _ .--.   _ .--.    __    .---.    .--.    _ .--.  
  |  _|    [  | | |  [ `/'`\] [ `.-. |  [  |  / /'`\] / .'`\ \ [ `/'`\] 
 _| |_      | \_/ |,  | |      | | | |   | |  | \__.  | \__. |  | |     
|_____|     '.__.'_/ [___]    [___||__] [___] '.___.'  '.__.'  [___]    
''')

a = Advisor
a.registerNewMember
print(a.searchMember)