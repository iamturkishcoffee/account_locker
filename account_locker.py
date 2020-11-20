user_id = str(input("Set your user id:"))

password = str(input("Set your password:"))

max_attempts = 0

while max_attempts < 3:
    guess = input("Enter the user id:")
    if(guess != user_id):
        print("Attempt Failed")
        max_attempts += 1
        if max_attempts == 3:
                print("Account Locked, call the Service Desk.")
    else:
        guess2 = input("Enter the password:")
        if(guess2 != password):
            print("Attempt Failed")
            max_attempts += 1
            if max_attempts == 3:
                print("Account Locked, call the Service Desk.")
        else:
            print("Access Granted")
            break
            
