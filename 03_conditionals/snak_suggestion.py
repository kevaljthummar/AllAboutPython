snack = input("Enter your preferred snak: ").lower()

print(f"user said: {snack}")
if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve cookies or samosa with tea")
else:
    print("Sorry unavaiilable")