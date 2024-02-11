from functions import *
while True:
    print(" Welcome to WsCube Tech-E School ".center(100,"_"))

    print('''
 1.Student Admission
 2.Students Fee
 3.Principal Access
 4.Exit:___
             ''')
    choice=eval(input("Enter your choice:"))
    if choice==1:
        admission_portal()
    elif choice==2:
        student_fee_portal()
    elif choice==3:
        principal_portal()
    elif choice==4:
        print("Thanks for visiting")
        break