school_database={}
student_fee_database={}

def admission_portal():
    print(" Welcome to Student Admission Portal ".center(100,"*"))
    StudentName=input("Enter StudentName: ")
    StudentFatherName=input("Enter StudentFatherName: ")
    StudentMotherName=input("Enter StudentMotherName: ")
    PhoneNo=input("Enter PhoneNo: ")
    Address=input("Enter Address: ")
    CardNo=1000+len(school_database)
    Class=input("Enter Class: ")
    school_database.update({CardNo:[StudentName,StudentFatherName,StudentMotherName,PhoneNo,Address,CardNo,Class]})
    print("Successfully Registered ")
    print("Card_No=",CardNo)

def student_fee_portal():
    CardNo=eval(input("Enter Card Number of student:"))
    if CardNo in school_database:
        show_student_detail(CardNo)
        print(fee_information())
        # student_class=eval(input("enter your class:"))

        # if school_database[CardNo][6]==1:
        #     print(f"you have to pay {fee_information()}")

        fee = eval(input("enter amount to pay:"))
        school_database[CardNo].append(fee)
        print(f"you successfully paid {fee} for class {school_database[CardNo][6]}")





def show_student_detail(card_no):
    print(f'''StudentName={school_database[card_no][0]}
StudentFatherName={school_database[card_no][1]}
StudentMotherName={school_database[card_no][2]}
PhoneNo={school_database[card_no][3]}
Address={school_database[card_no][4]}
CardNo={school_database[card_no][5]}
Class={school_database[card_no][6]}
    ''')


def principal_portal():
    print(" Principal Access ".center(100,"#"))
    principal_name = input("enter your name:")
    password=input("enter password:")
    if password=="qwerty":
        show_school_database()
    else:
        print("invalid password")


def show_school_database():
    crd=(input("enter student card no:"))
    # for key,values in school_database.items():
    if crd in school_database:
        print(fee_information())
        fee=eval(input("enter amount to pay:"))

    for key,values in school_database.items():
        print(f"card no:{key:<20} name={values[0]}, father name={values[1]}")

def fee_information():
    fee={"class 1":5000,
         "class 2":6000,
         "class 3":7000,
         "class 4":8000,
         "class 5":9000,
         "class 6":10000,
         "class 7":11000,
         "class 8":12000,
         "class 9":13000,
         "class 10":14000,
         "class 11":15000,
         "class 12":16000}
    return fee
