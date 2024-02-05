def login():
    username=input("Enter username: ")
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
    details={}
    valid=False
    f=open("Student details.txt")
    line=f.readline()
    if line=="":
        ID=0
    while line:
        data=line.split(",")
        ID=data[0]
        line=f.readline()
    ID=int(ID)+1
    details["ID"]=ID
    details["surname"]=input("""--------------
Enter surname: """)
    details["forename"]=input("""---------------
Enter forename: """)
    valid=False
    while not valid:
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
Enter home address: """)
    details["phone"]=input("""------------------------
Enter home phone number: """)
    data="a"
    while data!="M" and data!="F" and data!="O":
        data=input("""----------------------------
Enter gender (M/F/O(other)): """).upper()
    details["gender"]=data
    details["group"]=input("""------------------
Enter tutor group: """)
    data="{},{},{},{},{},{},{},{}".format(details["ID"],details["surname"],details["forename"],details["date"],details["address"],details["phone"],details["gender"],details["group"])
    f=open("Student details.txt","a")
    f.write(data+"\n")
    f.close()

def output_data():
    search=input("Enter student ID:")
    f=open("Student details.txt","r")
    line=f.readline()
    found=False
    while line and not found:
        data=line.split(',')
        if data[0]==search:
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
    if not found:
        print("""------------------
Student not found.""")

def report():
    search=input("Enter student ID:")
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
        
access=False
while not access:
    access=login()
while access:
    action=input("""------------------
Would you like to:
1:Enter student details
2:Retrieve student details
3:Create a report
4:log out
>""")
    if action=="1":
        input_data()
    elif action=="2":
        output_data()
    elif action=="3":
        report()
    elif action=="4":
        access=False
