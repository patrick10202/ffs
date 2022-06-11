from linecache import clearcache
from employeeClasses import *

a = Advisor
sy = SystemAdmin
su = SuperAdmin
def clearConsole():
    for x in range(20):
        print("\n")

def main():
    clearConsole()
    print('''
 ________                                 _                             
|_   __  |                               (_)                            
  | |_ \_|  __   _    _ .--.   _ .--.    __    .---.    .--.    _ .--.  
  |  _|    [  | | |  [ `/'`\] [ `.-. |  [  |  / /'`\] / .'`\ \ [ `/'`\] 
 _| |_      | \_/ |,  | |      | | | |   | |  | \__.  | \__. |  | |     
|_____|     '.__.'_/ [___]    [___||__] [___] '.___.'  '.__.'  [___]    

Welcome to furnicore!

1. Login as Advisor
2. Login as SysAdmin
3. Login as SuperAdmin
Press any other button to exit.
''')
    inp = input("Enter your choice: ")
    if inp == '1':
        if advisorLogin():
            clearConsole()
            def returnBack():
                print("1. Register new member") #DONE
                print("2. Search for a member") #DONE
                print("3. Modify the data of a member") #DONE
                print("4. Update own password") #DONE
                print("0. Back")
                inp = input("\nEnter your choice: ")
                if inp == '0':
                    clearConsole()
                    main()
                elif inp == '1':
                    clearConsole()
                    a.registerNewMember()
                    returnBack()
                elif inp == '2':
                    clearConsole()
                    a.searchMember()
                    returnBack()
                elif inp == '3':
                    clearConsole()
                    a.modifyMember()
                    returnBack()
                elif inp == '4':
                    clearConsole()
                    a.updateOwnPassword()
                    returnBack()
            returnBack()
    elif inp == '2':
        if sysAdminLogin():
            clearConsole()
            def returnBack():
                print("1. Register new member") #DONE
                print("2. Search for a member") #DONE
                print("3. Modify the data of a member") #DONE
                print("4. deleteMember") #DONE
                print("5. Update own password") #DONE
                print("6. checkListOfUsersAndRoles")
                print("7. registerNewAdvisor") #DONE
                print("8. modifyAdvisor") #DONE
                print("9. deleteAdvisor") #DONE
                print("10. resetAdvisorPassword")
                print("11. createSystemBackup")
                print("12. restoreSystemBackup")
                print("13. seeLogs")
                print("0. Back")
                inp = input("\nEnter your choice: ")
                if inp == '0':
                    clearConsole()
                    main()
                elif inp == '1':
                    clearConsole()
                    sy.registerNewMember()
                    returnBack()
                elif inp == '2':
                    clearConsole()
                    sy.searchMember()
                    returnBack()
                elif inp == '3':
                    clearConsole()
                    sy.modifyMember()
                    returnBack()
                elif inp == '4':
                    clearConsole()
                    sy.deleteMember()
                elif inp == '5':
                    clearConsole()
                    sy.updateOwnPassword()
                    returnBack()
                elif inp == '6':
                    clearConsole()
                    sy.checkListOfUsersAndRoles()
                elif inp == '7':
                    clearConsole()
                    sy.registerNewAdvisor()
                elif inp == '8':
                    clearConsole()
                    sy.modifyAdvisor()
                elif inp == '9':
                    clearConsole()
                    sy.deleteAdvisor()
                elif inp == '10':
                    clearConsole()
                    sy.resetAdvisorPassword()
                elif inp == '11':
                    clearConsole()
                    sy.createSystemBackup()
                elif inp == '12':
                    clearConsole()
                    sy.restoreSystemBackup()
                elif inp == '13':
                    clearConsole()
                    sy.seeLogs()
            returnBack()
    elif inp == '3':
        if superAdminLogin():
            clearConsole()
            def returnBack():
                print("1. Register new member")
                print("2. Search for a member")
                print("3. Modify the data of a member")
                print("0. Back")
                inp = input("\nEnter your choice: ")
                if inp == '0':
                    clearConsole()
                    main()
                elif inp == '1':
                    clearConsole()
                    su.registerNewMember()
                    returnBack()
                elif inp == '2':
                    clearConsole()
                    su.searchMember()
                    returnBack()
            returnBack()

main()