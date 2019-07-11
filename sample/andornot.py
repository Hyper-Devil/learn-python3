user_name = "whd"
email = "tywhd@qq.com"
password = "123"
# user_name = input("user_name=")
# email = input("email=")
# password = input("passward=")
if (user_name == "whd" or email == "tywhd@qq.com") and password == "123":
    print("Log in")
elif (user_name == "whd" or email == "tywhd@qq.com") or not password == "123":
    print("Forget password?")
else:
    print("Please contact with the system administrator.")
    # else后面不要少了冒号：
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
