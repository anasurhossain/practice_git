#Validate user input exercise
#1.username not more than 10 characters
#2.Username dosen't contain spaces
#3. Username dosen't conatin any number

user_name = input("Enter your name please: ")

if len(user_name)> 10 :
    print("Name should be 10 characters.")
elif user_name.find(" ")!= -1 :
    print("Remove space from username.")
elif not user_name.isalpha() :
    print("Remove numbers from username.")
else:
    print(f"Welcome {user_name}.")