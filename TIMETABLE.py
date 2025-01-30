print("GOVERNMENT POLYTECHNIC SITAMARHI\nDEPT. OF COMPUTER SCIENCE & ENGINEERING\n           TIME TABLE\n                           SATYAM KUMAR\n")
print("WORKING TIME 10:00AM to 05:00PM __ (Monday To Saturday)\n")
d = input("Enter Name of DAY:-")
if (d == "monday" or d == "Monday" or d == "MONDAY"):
    t = int(input("Enter TIME:-"))
    if (t == 10):
        print("C.N.D.C (ECE 6th) 10:00 to 11:00")
    elif (t == 11 or t == 4 or t == 12):
        print("NO CLASS TIME")
    elif (t == 1 or t == 2):
        print("PYTHON PROGRAMMING LAB (CE2 2nd) 01:00 TO 03:00")
    elif (t == 3 or t == 4):
        print("PYTHON PROGRAMMING (CSE 4th) 03:00 to 04:00")
    else:
        print("NO CLASS TIME")
        

elif (d == "tuesday" or d == "Tuesday" or d == "TUESDAY"):
    t = int(input("Enter TIME:-"))
    if (t == 10):
         print("C.N.D.C (ECE 6th) 10:00 to 11:00")
    elif (t == 11):                                                    
        print("DSA (CSE 4th) 11:00 to 12:00")
    elif ( t == 12 or t == 1):
        print("NO CLASS TIME")
    elif (t == 2):
        print("PYTHON PROGRAMMING (CSE 4th) 02:00 to 03:00")
    elif (t == 3 or t == 4):
         print("PYTHON PROGRAMMING LAB (CE1 2nd) 03:00 TO 05:00")
    else:
        print("NO CLASS TIME")

        
elif (d == "wednesday" or d == "WEDNESDAY" or d == "Wednesday"):
    t = int(input("Enter TIME:-"))
    if (t == 10):
        print("C.N.D.C (ECE 6th) 10:00 to 11:00")
    elif (t == 11):
        print("PYTHON PROGRAMMING (CSE 2nd) 11:00 to 12:00")
    elif (t == 12 or t == 1):
        print("NO CLASS TIME")
    elif (t == 2):
        print("DSA (CSE4th) 02:00 to 03:00")
    elif (t == 3 or t == 4):
        print("PYTHON PROGRAMMING LAB (CSE 4th) 03:00 to 05:00")
    else:
        print("NO CLASS TIME")


elif (d == "Thursday" or d == "thursday" or d == "THURSDAY"):
    t = int(input("Enter TIME:-"))
    if (t == 10):
        print("DSA (CSE 4th) 10:00 to 11:00")
    elif (t == 11):
        print("PYTHON PROGRAMMING (CE 2nd) 11:00 to 12:00")
    elif (t == 12 or t == 1):
        print("NO CLASS TIME")
    elif (t == 2):
        print("PYTHON PROGRAMMING (CE 2nd) 02:00 to 03:00")
    elif (t == 3 or t == 4):
        print("DSA LAB (CSE 4th) 03:00 to 05:00")
    else:
        print("NO CLASS TIME")


elif (d == "Friday" or d == "friday" or d == "FRIDAY"):
    t = int(input("Enter TIME:-"))
    if (t == 10):
        print("NO CLASS TIME")
    elif (t == 11 or t == 12):
        print("DSA LAB (CSE 4th) 11:00 to 01:00")
    elif (t == 1 or t == 2):
        print("PYTHON PROGRAMMING LAB (CE1 2nd) 01:00 to 03:00")
    elif (t == 3 or t == 4):
        print("PYTHON PROGRAMMING LAB (CE2 2nd) 03:00 to 05:00")
    else:
        print("NO CLASS TIME")


elif (d == "Saturday" or d == "SATURDAY" or d == "saturday"):
    t = int(input("Enter TIME:-"))
    if (t == 10):
        print("PYTHON PROGRAMMING (CSE 4th) 10:00 to 11:00")
    elif (t == 11 or t == 12):
        print("PYTHON PROGRAMMING LAB (CSE 4th) 11:00 to 01:00")
    elif (t == 1):
         print("C.N.D.C (ECE 6th) 01:00 to 02:00")
    else:
        print("NO CLASS TIME\n")

else:
    print("HOLIDAY")
print("\nCoder:-ANISH KUMAR AARJU____CSE/2023/028")
