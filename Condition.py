age = int(input("Enter your age: "))

if age < 18:
    print("Minor")
elif (age < 60 )and (age>= 18):
    print("Adult")
else:
    print("Senior Citizen")