import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Poorni@123",
    database="toll_management",
    port=3306
)

if conn.is_connected():
    print("✅ Connected to MySQL successfully")


import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root@localhost/toll_management"
)

query = """
SELECT 
    DATE(payment_date) AS date,
    SUM(amount) AS total_collection
FROM toll_payment
GROUP BY DATE(payment_date);
"""

df = pd.read_sql(query, engine)

print(df)


"""Daily Toll Collection (Line Chart)"""
import matplotlib.pyplot as plt

plt.figure()
plt.plot(df['date'], df['total_collection'])
plt.xlabel("Date")
plt.ylabel("Total Collection (₹)")
plt.title("Daily Toll Collection")
plt.show()

'''Toll Collection by Tollgate (Bar Chart)'''
query = """
SELECT t.toll_name, SUM(p.amount) AS collection
FROM toll_payment p
JOIN tollgate t ON p.toll_id = t.toll_id
GROUP BY t.toll_name;
"""

df2 = pd.read_sql(query, conn)

plt.figure()
plt.bar(df2['toll_name'], df2['collection'])
plt.xlabel("Tollgate")
plt.ylabel("Collection (₹)")
plt.title("Toll Collection by Tollgate")
plt.show()

'''Peak Traffic Hours (Traffic Analysis)'''
query = """
SELECT HOUR(payment_date) AS hour, COUNT(*) AS vehicle_count
FROM toll_payment
GROUP BY HOUR(payment_date)
ORDER BY hour;
"""

df3 = pd.read_sql(query, conn)

plt.figure()
plt.plot(df3['hour'], df3['vehicle_count'])
plt.xlabel("Hour of Day")
plt.ylabel("Vehicle Count")
plt.title("Peak Traffic Hours")
plt.show()

'''Low FASTag Balance Vehicles (Alert Table)'''
query = """
SELECT v.vehicle_number, f.balance
FROM fastag f
JOIN vehicle v ON f.vehicle_id = v.vehicle_id
WHERE f.balance < 100;
"""

df4 = pd.read_sql(query, conn)
print(df4)

query = """
SELECT 
    vt.type_name,
    COUNT(v.vehicle_id) AS vehicle_count
FROM vehicle v
JOIN vehicle_type vt ON v.type_id = vt.type_id
GROUP BY vt.type_name;
"""

df5 = pd.read_sql(query, engine)

print(df5)

explode = [0.05] * len(df5)

plt.figure()
plt.pie(
    df5['vehicle_count'],
    labels=df5['type_name'],
    autopct='%1.1f%%',
    explode=explode,
    startangle=90
)
plt.title("Vehicle Distribution by Type")
plt.show()


