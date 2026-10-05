print(True and True)
print(True and False)
print(False and True)
print(False and False)


#here found a little difficlt to understand and practice

age = int(input("how old are you ? ") )
id = input("do you have an id ? yes/no " )

eligible = age >= 18 and id == "yes"
print("Are yo eligible to enter:", eligible)# true means you are eligible & false means you are not eligible