print(True or True)
print(True or False)
print(False or True)
print(False or False)

age = int(input("how old are you ? ") )
id = input("do you have an id ? yes/no " )

eligible = age >= 18 or id == "yes"
print("Are yo eligible to enter:", eligible) 
# true means you are eligible 
# false means you are not eligible
