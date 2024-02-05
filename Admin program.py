def login():   #Enter username and password, if correct return True
    username=input("Enter username: ")  #if not return False
    password=input("Enter password: ")
    f=open("Tutor accounts.txt")
    line=f.readline()
    valid=False
    while line:
        data=line.split(",")
        if data[0]==username and data[1]==password:
            return True
        line=f.readline()
    return False

def input_data():
    details={}  #Creates an empty dictionary
    valid=False 
    f=open("Student details.txt")
    line=f.readline()   #Read file to find out last ID in file,
    if line=="":        #then add 1 for new file.
        ID=0
    while line:
        data=line.split(",")
        ID=data[0]
        line=f.readline()
    ID=int(ID)+1
    details["ID"]=ID
    details["surname"]=input("""--------------
Enter surname: """) #input surname
    details["forename"]=input("""---------------
Enter forename: """) #input forename
    valid=False
    while not valid:  #input date of birth in form DD/MM/YY
        valid=True
        try:
            data=input("""-----------------------------------------
Enter date of birth in the form DD/MM/YY: """)
            date=data.split("/")
            for i in date:
                if valid:
                    if not (len(i)==2 and i.isnumeric() and len(date)==3):
                        print("""-------------
Invalid date.""")
                        valid=False
            if (int(date[1])>12 or int(date[1])<1) and valid:
                print("""-------------
Invalid date.""")
                valid=False
            elif (int(date[0])>31 or int(date[0])<1) and valid:
                print("""-------------
Invalid date.""")
                valid=False
            elif int(date[2])<0 and valid:
                print("""-------------
Invalid date.""")
                valid=False
        except:
            if valid:
                print("""-------------
Invalid date.""")
            valid=False
    details["date"]=data
    details["address"]=input("""-------------------
Enter home address: """) #input address
    details["phone"]=input("""------------------------
Enter home phone number: """) #input phone number
    data="a"
    while data!="M" and data!="F" and data!="O":
        data=input("""----------------------------
Enter gender (M/F/O(other)): """).upper() #input gender
    details["gender"]=data
    details["group"]=input("""------------------
Enter tutor group: """) #input tutor group
    data="{},{},{},{},{},{},{},{}".format(details["ID"],details["surname"],details["forename"],details["date"],details["address"],details["phone"],details["gender"],details["group"])
    f=open("Student details.txt","a") #input data to file
    f.write(data+"\n")
    f.close()

def output_data():
    search=input("Enter student ID:") #ID in, data out
    f=open("Student details.txt","r")  #read data from file
    line=f.readline()
    found=False
    while line and not found:
        data=line.split(',')
        if data[0]==search:  #print details
            print("""ID:           {}
----------------------------
Surname:      {}
----------------------------  
Forename:     {}
----------------------------
Date of birth:{}
----------------------------
Address:      {}
----------------------------
Phone Number: {}
----------------------------
Gender:       {}
----------------------------
Tutor Group:  {}""".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            found=True
        line=f.readline()
    if not found:  #if student doesn't exist, tell user
        print("""------------------
Student not found.""")

def register():

    absent = ""

    f=open("Student details.txt","r")
    line=f.readline()
    data=line.split(',')

    print("Use Y/N to mark if a student is present!")
    for i in range(12):
        x = ""
        x = input(print(data[1],data[2],""))
        if x == "Y":
            absent = "Present"
        elif x == "N":
            absent = "Absent"
    


def report():
    search=input("Enter student ID:")  #output_data() but formatted and can add description
    f=open("Student details.txt","r")
    line=f.readline()
    found=False
    while line and not found:
        data=line.split(',')
        if data[0]==search:
            found=True
        line=f.readline()
    description=input('Enter a description for the report:\n>')
    print('''{},{}
ID:{}
Gender:{}
Phone:{}
Tutor Group:{}
---------------------------------------
{}'''.format(data[1],data[2],data[0],data[6],data[5],data[7],description))

#Start of main program

access=False
while not access:
    access=login()
while access:
    action=input("""------------------
Would you like to:
1:Enter student details
2:Retrieve student details
3:Create a report
4:Take Register
5:log out
>""")
    if action=="1":
        input_data()
    elif action=="2":
        output_data()
    elif action=="3":
        report()
    elif action=="4":
        register()
    elif action=="5":
        access=False
