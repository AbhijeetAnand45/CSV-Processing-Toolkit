import csv
import mysql.connector

def run_query_and_save_to_csv():
    # MySQL database configuration
    db_config = {
        'host': 'your_hostaddress',
        'user': 'your_username',
        'password': 'your_password',
        'database': 'your_db_name',
        'port': 'portno'
    }

    # Connect to MySQL
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print('Connected to MySQL')
            
            # SQL query to execute
            query = 'select hostid, name, type, vendor, macaddress_a, site_address_a, site_state, site_country from tablename where name is not null;'

            # Execute the query
            cursor = connection.cursor()
            cursor.execute(query)

            # Fetch all the rows
            rows = cursor.fetchall()

            # CSV file configuration
            csv_filename = 'output.csv'

            # Write the data to a CSV file
            with open(csv_filename, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Write header
                csv_writer.writerow([i[0] for i in cursor.description])
                
                # Write rows
                csv_writer.writerows(rows)

            print(f'Data saved to {csv_filename}')

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed')

if __name__ == "__main__":
    run_query_and_save_to_csv()

