import logging
import sys
import sys
import concurrent.futures
import traceback
from datetime import datetime
import configparser
import inspect
# from myLogConfig import setLogConfig
import time
import mysql.connector

from mysql.connector.connection import MySQLConnection

class MySqldbconnection:
    logger=logging.getLogger(__name__)

    def __init__(self):


        print( " Creating new DB Connection")

    def get_master_db_connection(self):
        try:
            print(f"Connecting to DEV Master Database: DEV;")
            self.logger.info(f"Connecting to DB: DEV;")
            connst = datetime.now()

            master_conn = mysql.connector.connect(user='your_username', password='your_password', host='hostaddress',
                                               database='your_dbname', port='portno')
           
    
           
            if not master_conn.is_connected():
                print("Failed to connect to dev database; Re-attempting connection:")
                self.logger.info("Failed to connect to dev database; Re-attempting connection:")

            
            connend = datetime.now()
            print(f"Connected to dev;Duration:{connend - connst}")
            self.logger.info(f"Connected to dev;Duration:{connend - connst}")
            return master_conn
        except Exception as err:
            print(f"error while connecting to masterdb;" + str(err))
            self.logger.error(f"Error while connecting to masterdb" + str(err))

