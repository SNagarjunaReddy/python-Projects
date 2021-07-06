sys_user_name= "Nagarjuna"
sys_user_password= "123456"
user_name=input("enter user name : ")
user_password=input("enter user password : ")
if user_name != sys_user_name and user_password == sys_user_password:
    print("invalid user name")
elif user_name == sys_user_name and user_password != sys_user_password:
    print("invalid password")
elif user_name!=sys_user_name and user_password!=sys_user_password:
    print("invalid user name and password")
else:
    print("welcome sir")
