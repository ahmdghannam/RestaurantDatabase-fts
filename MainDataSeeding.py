import random
import pyodbc
from datetime import datetime, timedelta
from mockData import first_names_pool
from mockData import last_names_pool
from mockData import restaurant_roles
from mockData import tables_capacities
from mockData import phone_numbers
from mockData import emails
from mockData import menu_items

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"      
    "Database=Restaurants;"   
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

cursor.execute(
    "SELECT RESTAURANT_ID FROM RESTAURANT"
)
restaurantIds = [row[0] for row in cursor.fetchall()]

#**# SEEDING EMPLOYEE TABLE 
# for i in range(1 ,101):
#     emp_id = "E" + str(i).zfill(3)
#     employee_ids.append(emp_id)
#     first_name = random.choice(first_names_pool)
#     last_name = random.choice(last_names_pool)
#     position = random.choice(restaurant_roles)
#     restaurant_id = random.choice(restaurantIds)

#     cursor.execute("""
#         INSERT INTO Employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, RESTAURANT_ID, POSITION)
#         VALUES (?,?,?,?,?)
#     """, (emp_id,first_name,last_name,restaurant_id,position))

#     conn.commit()

#**# SEEDING [TABLE] TABLE 
# for i in range(1 ,101):
#     table_id = "T" + str(i).zfill(3)
#     capacity = random.choice(tables_capacities)
#     restaurant_id = random.choice(restaurantIds)

#     cursor.execute("""
#         INSERT INTO [Table] (TABLE_ID, CAPACITY, RESTAURANT_ID)
#         VALUES (?,?,?)
#     """, (table_id, capacity, restaurant_id))

#     conn.commit()

#**# SEEDING CUSTOMER TABLE 
# for i in range(1 ,401):
#     customer_id = "C" + str(i).zfill(3)
#     first_name = random.choice(first_names_pool)
#     last_name = random.choice(last_names_pool)
#     phone_number = random.choice(phone_numbers)
#     email = random.choice(emails)

#     cursor.execute("""
#         INSERT INTO [CUSTOMER] (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE)
#         VALUES (?,?,?,?,?)
#     """, (customer_id, first_name, last_name,email,phone_number))

#     conn.commit()

#**# SEEDING MenuItems TABLE 
# for i in range(1 ,1001):
#     item_id = "I" + str(i).zfill(3)
#     name = random.choice(menu_items)
#     description = ""
#     price = random.randint(10, 500)

#     restaurant_id = random.choice(restaurantIds)

#     cursor.execute("""
#         INSERT INTO [MenuItems] (ITEM_ID, RESTAURANT_ID, NAME, DESCRIPTION, PRICE)
#         VALUES (?,?,?,?,?)
#     """, (item_id, restaurant_id,name,description,price ))

#     conn.commit()

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


#**# SEEDING RESERVATION TABLE 
# cursor.execute(
#     "SELECT TABLE_ID FROM [Table]"
# )
# tableIds = [row[0] for row in cursor.fetchall()]

# cursor.execute(
#     "SELECT CUSTOMER_ID FROM [Customer]"
# )
# customerIds = [row[0] for row in cursor.fetchall()]

# for i in range(1 ,501):
#     reservation_id = "R" + str(i).zfill(3)

#     restaurant_id = random.choice(restaurantIds)
#     table_id = random.choice(tableIds)
#     customer_id = random.choice(customerIds)
#     party_size = random.choice(tables_capacities)
#     start_date = datetime(2025, 1, 1)
#     end_date = datetime(2025, 12, 31)

#     date = random_date(start_date, end_date)


#     cursor.execute("""
#         INSERT INTO [RESERVATION] (RESERVATION_ID, TABLE_ID, RESTAURANT_ID, CUSTOMER_ID, PARTY_SIZE, RESERVATION_DATE)
#         VALUES (?,?,?,?,?,?)
#     """, (reservation_id,table_id, restaurant_id,customer_id,party_size, date ))

#     conn.commit()



#**# SEEDING [Order] TABLE 

# cursor.execute(
#     "SELECT Employee_ID FROM [Employee]"
# )
# employeeIds = [row[0] for row in cursor.fetchall()]

# cursor.execute(
#     "SELECT RESERVATION_ID FROM [RESERVATION]"
# )
# reservationIds = [row[0] for row in cursor.fetchall()]

# for i in range(1 ,501):
#     order_id = "O" + str(i).zfill(3)
#     employee_id = random.choice(employeeIds)
#     reservation_id = random.choice(reservationIds)
#     start_date = datetime(2025, 1, 1)
#     end_date = datetime(2025, 12, 31)
#     date = random_date(start_date, end_date)
#     total_amount = random.randint(10, 500)

#     cursor.execute("""
#         INSERT INTO [Order] (ORDER_ID, EMPLOYEE_ID, RESERVATION_ID, ORDER_DATE, TOTAL_AMOUNT)
#         VALUES (?,?,?,?,?)
#     """, (order_id, employee_id,reservation_id,date,total_amount ))

#     conn.commit()


#**# SEEDING [OrderItem] TABLE 

# cursor.execute(
#     "SELECT ORDER_ID FROM [ORDER]"
# )
# orderIds = [row[0] for row in cursor.fetchall()]

# cursor.execute(
#     "SELECT ITEM_ID FROM [MenuItems]"
# )
# itemIds = [row[0] for row in cursor.fetchall()]

# for i in range(1 ,1501):
#     order_item_id = "OI" + str(i).zfill(4)
#     item_id = random.choice(itemIds)
#     order_id = random.choice(orderIds)
#     quantity = random.randint(1,20)

#     cursor.execute("""
#         INSERT INTO [ORDER_ITEM] (ORDER_ITEM_ID, ITEM_ID, ORDER_ID, QUANTITY)
#         VALUES (?,?,?,?)
#     """, (order_item_id, item_id,order_id,quantity ))

#     conn.commit()




print("Connected successfully!")