

import random
user_code = int(input("Enter a 4-digit for PIN code: "))
pin_code = random.randint(1000,9999)
if len(str(user_code)) != 4:
    print("please write 4 digits !")
elif user_code == pin_code:
        print("Success! PIN code matched ")
else:
    print(f"Failure ! PIN cod did not match .\nthe computer generated this PIN:{pin_code}")
