from employeeClasses import *

a = Advisor
sy = SystemAdmin
su = SuperAdmin
def main():
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
''')
    inp = input("Enter your choice: ")
    if inp == '1':
        if advisorLogin():
            print("1. Register new member")
            print("2. Search for a member")
            print("3. Modify the data of a member")
            print("4. Update own password")
            inp = input("Enter your choice: ")
            if inp == '1':
                a.registerNewMember()
            elif inp == '2':
                a.searchMember()
            elif inp == '3':
                a.modifyMember()
            elif inp == '4':
                a.updateOwnPassword()
    elif inp == '2':
        if sysAdminLogin():
            print("1. Register new member")
            print("2. Search for a member")
            print("3. Modify the data of a member")
            print("4. Update own password")
            inp = input("Enter your choice: ")
            if inp == '1':
                sy.registerNewMember()
            elif inp == '2':
                sy.searchMember()
            elif inp == '4':
                sy.updateOwnPassword()
    elif inp == '3':
        if superAdminLogin():
            print("1. Register new member")
            print("2. Search for a member")
            print("3. Modify the data of a member")
            inp = input("Enter your choice: ")
            if inp == '1':
                su.registerNewMember()
            elif inp == '2':
                su.searchMember()

main()