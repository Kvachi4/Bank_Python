greeting = input("Dear bank officers, Please greet bank users properly :").lower().title().strip()
print(greeting)
if greeting == "Hello":
    print("Greeting :", greeting, "\n$0")
elif greeting[0] == "H" and greeting != "Hello":
    print("Greeting :", greeting, "\n$20")
else:
    print("Greeting :", greeting, "\n$100")