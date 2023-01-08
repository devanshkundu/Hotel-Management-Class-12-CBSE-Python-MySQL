import mysql.connector

# Create Database Function
def create_database():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678")
    
    try:
       mycursor = mydb.cursor()

       mycursor.execute('CREATE DATABASE hotel')
    except:
        print("\n Error")
    home()
    
# Home Function
def home():
     
    print('\t\t\t\t\t\t WELCOME TO HOTEL MANAGEMENT SYSTEM\n')
    print('-'*100)
    print('\n')
    print('\t\t\t 1 Rooms \n')
    print('\t\t\t 2 Employees\n')
    print('\t\t\t 3 IMP! Create database hotel \n')
    print('\t\t\t 0 Exit\n')
  
    ch=int(input("->"))
     
    if ch == 1:
        print(" ")
        room()
        
    elif ch == 2:
        print(" ")
        employees()
        
    elif ch == 3:
        print(" ")
        create_database()   
     
    else:
        exit()

# Room Information Menu Function
def room():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    
    mycursor = mydb.cursor()
    
    print('\t\t\t\t\t\t Edit Room Info\n')
    print('-'*100)
    print('\n') 
    print('\t\t\t 1 Add Room \n')
    print('\t\t\t 2 Show Room \n')
    print('\t\t\t 3 Update Room \n')
    print('\t\t\t 4 Update room occupation \n')
    print('\t\t\t 5 Create table roominfo IMP!\n')
    print('\t\t\t 6 Drop table roominfo \n')
    print('\t\t\t 7 Back to Home \n')
    print('\t\t\t 0 Exit\n')

    ch=int(input("->"))

    if ch == 1:
        print(" ")
        add_room()
        
    elif ch == 2:
        print(" ")
        show_room()

    elif ch == 3:
        print(" ")
        update_room()

    elif ch == 4:
        print(" ")
        update_roomstatus()
        
    elif ch == 5:
        print(" ")
        create_roominfo()    

    elif ch == 6:
        print(" ")
        drop_roominfo()
        
    elif ch == 7:
        print(" ")
        home()
        
    elif ch == 0:
        print(" ")
        exit()    
            
    else:
        room_info()

# Create Table roominfo Function
def create_roominfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")

    try:
        mycursor = mydb.cursor()
        mycursor.execute('CREATE TABLE IF NOT EXISTS `roominfo` (`id` int(10) NOT NULL AUTO_INCREMENT,`room_no` int(4) DEFAULT NULL,`room_type` char(20) DEFAULT NULL,`room_rent` float(10,2) DEFAULT NULL,`room_bed` char(20) DEFAULT NULL,`status` char(20) DEFAULT NULL,PRIMARY KEY (`id`)) ;')
    except:
        print('Error\n')
    room()
# Add Room Infomation Function     
def add_room():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    mycursor = mydb.cursor()
    print('\t\t\t\t\t\t Add New Room ')
    print('-'*100)
    try:
       room_no = input('\n Enter Room No :')
       room_type = input('\n Enter Room Type (SS/JS/PS):')
       room_rent = input('\n Enter Room Rent (INR) :')
       room_bed = input('\n Enter Room Bed Type(Single/Double/Triple) :')
       occupation = input('\n Occupation (Occupied,Maintenance,Free):')
       sql = 'insert into roominfo(room_no,room_type,room_rent,room_bed,status) values \
        ('+room_no+',"'+room_type.upper()+'",'+room_rent+',"'+room_bed.upper()+'"," '+occupation+'");'
       mycursor.execute(sql)
       mydb.commit()
    except:
        print('Error\n')

    print(mycursor.rowcount, "record inserted.")
    room()      

# Show Room Information Function 
def show_room():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM roominfo')
    print('\t\t\t\t\t\t Room Info ')
    print('-'*100)

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)

    room()

# Update Room Information Function
def update_room():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    try:
       mycursor = mydb.cursor()

       print('\t\t\t\t\t\t Update Room Information ')
       print('-'*100)
       print('1.   Room Type')
       print('2.   Room Rent')
       print('3.   Room Bed')
       print('4.   Room Status')
       choice = int(input('Enter your choice :'))
       field_name = ''
       if choice == 1:
          field_name = 'room_type'
       if choice == 2:
          field_name = 'room_rent'
       if choice == 3:
          field_name = 'room_bed'
       if choice == 4:
          field_name = 'status'   

       
       room_no  = input('Enter room No :')   
       value = input('Enter new value :')
       sql = 'update roominfo set '+field_name+' = "'+value+'" where  room_no ='+room_no +';'
       mycursor.execute(sql)

       mydb.commit()
    except:
       print("\n Error") 
    room()
# Update Room Status Function    
def update_roomstatus():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")

    mycursor = mydb.cursor()

    print('\t\t\t\t\t\t Update Room Status ')
    print('-'*100)

    room_no = input('Enter room No :')
    occupation = int(input('Occupation (1.Occupied,2.Maintenance,3.Free):'))
    if occupation == 1 :
        value = 'Occupied'
    if occupation == 2 :
        value = 'Maintenance'
    if occupation == 3 :
        value = 'Free'    
        
       
    sql = 'update roominfo set status = "'+ value +'" where  room_no =' + room_no +';'
    mycursor.execute(sql)
    mydb.commit()
    room()
    
# Drop roominfo Table
def drop_roominfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    
    mycursor = mydb.cursor()

    sql = 'DROP TABLE roominfo'

    mycursor.execute(sql)
    room()
    
# Employees Menu Function    
def employees():
    print('\t\t\t\t\t\t Employees\n')
    print('-'*100)
    print('\n') 
    print('\t\t\t 1 Add employee info \n')
    print('\t\t\t 2 Show employees info\n')
    print('\t\t\t 3 Update employees info \n')
    print('\t\t\t 4 Create table empinfo IMP!\n')
    print('\t\t\t 5 Drop table empinfo \n')
    print('\t\t\t 6 Back to Home \n')
    print('\t\t\t 0 Exit\n')

    ch=int(input("->"))

    if ch == 1:
        print(" ")
        add_empinfo()
        
    elif ch == 2:
        print(" ")
        show_empinfo()

    elif ch == 3:
        print(" ")
        update_empinfo()
        
    elif ch == 4:
        print(" ")
        create_empinfo()    

    elif ch == 5:
        print(" ")
        drop_empinfo()
        
    elif ch == 6:
        print(" ")
        home()
        
    elif ch == 0:
        print(" ")
        exit()    
            
    else:
        employees()

# Create Employees Information Function
def create_empinfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    mycursor = mydb.cursor()
    try:
        mycursor.execute('CREATE TABLE IF NOT EXISTS `empinfo` (`emp_id` int(10) NOT NULL AUTO_INCREMENT,`emp_name` varchar(30) DEFAULT NULL,`emp_occupation` varchar(20) DEFAULT NULL,`emp_salary` float(10,2) DEFAULT NULL,PRIMARY KEY (`emp_id`)) ;')
    except:
        print("\n Error")
    
    employees()        

    
# Add Employees Information Function
def add_empinfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    mycursor = mydb.cursor()
    print('\t\t\t\t\t\t Add New Room ')
    print('-'*100)

    try :
       emp_id = input('\n Enter Employee ID :')
       emp_name = input('\n Enter Employee Name :')
       emp_occupation = input('\n Enter Employee Occupation :')
       emp_salary = input('\n Enter Employee Salary :')
    
       sql = 'insert into empinfo(emp_id,emp_name,emp_occupation,emp_salary) values \
        ('+emp_id+',"'+emp_name+'","'+emp_occupation+'",'+emp_salary+');'
       mycursor.execute(sql)
    
       mydb.commit()
    except :
        print('Error\n')
        
    print(mycursor.rowcount, "record inserted.")
    employees()

# Drop empinfo Table Function    
def drop_empinfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")

    try :
       mycursor = mydb.cursor()

       sql = 'DROP TABLE empinfo'

       mycursor.execute(sql)
    except :
        print('Error\n')
        
    employees()

# Show Employees Information Function
def show_empinfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM empinfo')
    print('\t\t\t\t\t\t Room Info ')
    print('-'*100)

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)

    employees()    

# Update Employees Information Functions
def update_empinfo():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="hotel")

    mycursor = mydb.cursor()

    print('\t\t\t\t\t\t Update Employee Information ')
    print('-'*100)
    print('1.   Employee Name')
    print('2.   Employee Occupation')
    print('3.   Employee Salary')
    choice = int(input('Enter your choice :'))
    field_name = ''
    if choice == 1:
       field_name = 'emp_name'   
       
    if choice == 2:
       field_name = 'emp_occupation'
       
    if choice == 3:
       field_name = 'emp_salary'   

    try :   
        emp_id  = input('Enter Employee ID :')   
        value = input('Enter new value :')
        sql = 'update empinfo set ' +field_name +' = "'+ value +'" where  emp_id ='+ emp_id+';'
        mycursor.execute(sql)
        mydb.commit()
    except:
         print("\n Error")
    employees()

home()




           
        

        


        
