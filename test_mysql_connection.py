import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='manu@12345',  # Replace with your MySQL password
            database='Manu'  # Replace with your MySQL database name
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()

            # Assuming you want to create the required tables if they do not exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS user_data (
                ID INT NOT NULL AUTO_INCREMENT,
                Name VARCHAR(100) NOT NULL,
                Email_ID VARCHAR(50) NOT NULL,
                resume_score VARCHAR(8) NOT NULL,
                Timestamp VARCHAR(50) NOT NULL,
                Page_no VARCHAR(5) NOT NULL,
                Predicted_Field VARCHAR(25) NOT NULL,
                User_level VARCHAR(30) NOT NULL,
                Actual_skills VARCHAR(300) NOT NULL,
                Recommended_skills VARCHAR(300) NOT NULL,
                Recommended_courses VARCHAR(600) NOT NULL,
                PRIMARY KEY (ID)
            )
            """
            cursor.execute(create_table_query)
            print("Table user_data created successfully.")

            # Close cursor and connection after setup
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == "__main__":
    connect_to_database()
-