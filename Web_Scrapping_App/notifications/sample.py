#
# import psycopg2
# def fetch_table_data(table_name):
#
#     try:
#         # Connect to the PostgreSQL database
#         connection = psycopg2.connect(
#             user="postgres",
#             password="Himanshu",
#             host="127.0.0.1",
#             port="5432",
#             database="DB1")
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Fetch all data from the specified table
#         cursor.execute(f"SELECT * FROM {table_name}")
#         rows = cursor.fetchall()
#
#         # Fetch column names
#         colnames = [desc[0] for desc in cursor.description]
#
#         # Print column names and rows
#         print(f"Column names: {colnames}")
#         for row in rows:
#             print(row)
#             print("Row values by index:", row[0], row[1], row[2])
#
#     except Exception as error:
#         print(f"Error: {error}")
#     finally:
#         # Close the cursor and connection
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#
# if __name__ == "__main__":
#     table_name = "app1_wishlist"  # Replace with your table name
#     fetch_table_data(table_name)
#
#
#
#
#
#
# print("Hello")
# list=['hello','world','him','god','pray']
# print(list)
#
# print(list[0][1:])

print("₹24,499")
str="₹24,499"

print(type(str))

nstr=""

for i in range(1,len(str)):
    print(str[i])
    nstr+=str[i]
print(int(nstr.replace(',','')))


print(int("11,499".replace(',','')))