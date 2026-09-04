import os

print("The system will shut down in 60 seconds")

os.system("shutdown /s /t 60")

cancelar = input("Type 'cancel' to interrupt the shutdown: ").lower()

if cancelar == "cancel":
    os.system("shutdown /a")
    print("The computer will not be shut down")
else:
    print("Computer shutting down")
