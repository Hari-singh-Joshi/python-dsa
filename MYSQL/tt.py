import mysql.connector

try:
    # Establishing the connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python"
    )
    
    cursor = conn.cursor()  # Moved inside the try block
    
    if conn.is_connected():
        # Inserting values
        q = 'INSERT INTO student (id, name, mobile) VALUES (%s, %s, %s)'
        v = (12, 'harish joshi', '7453966532')  # Values must be tuple, no quotes around numbers
        cursor.execute(q, v)

    else:
        print("Connection to MySQL database failed")

except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)

# finally:
#     # Closing the connection
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()
#         print("MySQL connection is closed")
