import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="Abhi@6370",
    host="localhost",
    port=3306,
    database="gietu"
)

if conn.is_connected():
    print("Database connected successfully!")

cur=conn.cursor()

#Show all databases in MySQL
cur.execute("SHOW DATABASES")
for db in cur:
    print(db)

#show all the data in the table giet
cur.execute("SELECT * FROM giet")
for row in cur:
    print(row)


 #Display only the name column.
cur.execute("SELECT name FROM giet")
for name in cur:
    print(name)


#Display name and address of all employees.
cur.execute("SELECT name, address FROM giet")
for name, address in cur:
    print(f"Name: {name}, Address: {address}")


#Show roll and salary of all employees.
cur.execute("select roll_no,salary from giet;")
for roll, salary in cur:
    print(f"Roll: {roll}, Salary: {salary}")


#Display all employees whose name is 'aman'.
cur.execute("select*from giet where name='aman';")
for row in cur:
    print(row)


#Show employees who live in 'delhi'.
cur.execute("select*from giet where address='delhi';")
for i in cur:
    print(i)

#Display all employees whose gender is 'M'.
cur.execute("select*from giet where gender='M';")
for i in cur:
    print(i)



#Show employees whose designation is 'doctor'.
cur.execute("select*from giet where Desig='doctor';")
for X in cur:
    print(X)


#Display employees having salary 15000.
cur.execute("select*from giet where salary=15000;")
for i in cur:
    print(i)


#Show employees with salary greater than 20000.
cur.execute("select*from giet where salary>20000;")
for i in cur:
    print(i)

#Display employees with salary less than 30000.
cur.execute("select*from giet where salary<30000;")
for i in cur:
    print(i)

#Show employees who are male AND have salary > 20000.
cur.execute("select*from giet where gender='M' and salary>20000;")
for i in cur:
    print(i)


#Display employees who are female OR live in 'raipur'.
cur.execute("select*from giet where gender='F' or address='raipur';")
for i in cur:
    print(i)


#Show employees whose name starts with 'a'.
cur.execute("select*from giet where name like 'a%';")
for i in cur:
    print(i)


#Display employees whose name ends with 'h'.
cur.execute("select*from giet where name like '%h';")
for i in cur:
    print(i)


#Show employees whose address contains 'pur'.
cur.execute("select*from giet where address like '%pur%';")
for i in cur:
    print(i)

#Display all employees sorted by name in ascending order.
cur.execute("select*from giet order by name asc;")
for i in cur:
    print(i)


#Show all employees sorted by salary in descending order.
cur.execute("select*from giet order by salary desc;")
for i in cur:
    print(i)


#Count total number of employees in the table.
cur.execute("select count(*) from giet;")
for i in cur:
    print(i)


#Count number of employees whose gender is 'M'.
cur.execute("select count(*) from giet where gender='M';")
for i in cur:
    print(i)


cur.close()
conn.close()