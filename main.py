import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping part table if already exists.
cursor.execute("DROP TABLE IF EXISTS part")

#Creating table as per requirement
# sql ='''CREATE TABLE part(
#    id INT NOT NULL,
#    Part_no INT,
#    SN_no INT,
#    Measure_DATE INT,
#    Measure_TIME INT,
#    CODE CHAR(3),
#    FLAG CHAR(1)
# )'''
# cursor.execute(sql)
# print("Table created successfully........")

# cursor.execute('''INSERT INTO part VALUES
#    (1001, 101, 201, 20201207, 9000, 'ggg', 'N')''')
# cursor.execute('''INSERT INTO part VALUES
#    (1002, 102, 202, 20201208, 9001, 'hhh', ' ')''')
data_part = input("enter Part_no")
data_serial = input("enter SN_no")
data_date = input("enter Measure_DATE")
data_time = input("enter Measure_TIME")
data_code = input("enter CODE")
user_code = data_code.upper()
user_part = int(data_part)
user_serial = int(data_serial)
user_date = int(data_date)
user_time = int(data_time)

print("before update")
cursor.execute(f'''SELECT * from part WHERE PN = {user_part} and SN = {user_serial} and MSR_DATE = {user_date} and 
                MSR_TIME = {user_time} and RSN_CODE = '{user_code}' ''')
print(cursor.fetchall())

sql = f'''UPDATE part SET FLAG ='1' WHERE PN = {user_part} and SN = {user_serial} and MSR_DATE = {user_date} and 
                MSR_TIME = {user_time} and RSN_CODE = '{user_code}' '''

try:
    cursor.execute(sql)
    print("Table updated...... ")
    #Commit your changes in the database
    conn.commit()


except:
    # Rollback in case there is any error
    print("Table not updated...... ")
    conn.rollback()

print("after update")
cursor.execute(f'''SELECT * from part WHERE PN = {user_part} and SN = {user_serial} and MSR_DATE = {user_date} and 
                MSR_TIME = {user_time} and RSN_CODE = '{user_code}' ''')
print(cursor.fetchall())

#Closing the connection
conn.close()