sys_user_name= "Nagarjuna"
sys_user_password= "123456"
Attempts = 3
while True:
    user_name=input("enter user name : ")
    user_password=input("enter user password : ")
    if user_name != sys_user_name and user_password == sys_user_password:
        print("invalid user name")
        Attempts-=1
    elif user_name == sys_user_name and user_password != sys_user_password:
        print("invalid password")
        Attempts -= 1
    elif user_name!=sys_user_name and user_password!=sys_user_password:
        print("invalid user name and password")
        Attempts -= 1
    
    else:
        print("welcome sir")
        break
    
    if Attempts==0:
        print("contact your admin")
        break
