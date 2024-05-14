import pandas as pd
from datetime import datetime
import mysql.connector
import numpy as np
# from myLogConfig import setLogConfig
from MysqldbConfig import MySqldbconnection
import os

class read_and_insert_data_mdb:
    def __init__(self):
        self.master_db_connection=MySqldbconnection().get_master_db_connection()
        self.dataframe=None
        self.input_file="filename.csv"
        self.table_name="your_tablename"


    def read_files(self):
        try:
            read_start= datetime.now()
            print("Process: read_files; Started;")

            result_df = pd.read_csv(self.input_file, on_bad_lines="skip", engine="python")
            result_df = result_df.where(pd.notna(result_df), None)
            result_df.replace({np.nan: None}, inplace=True)
            # result_df['creation_time'] = pd.to_datetime(result_df['creation_time']).dt.strftime('%Y-%m-%d %H:%M:%S')
            # result_df.sort_values(by='creation_time', ascending=False, inplace=True)
            # result_df.drop_duplicates(subset='oltfullport', keep='first', inplace=True)
            # result_df.reset_index(drop=True, inplace=True)
            read_end=datetime.now()
            print(f"Process:Read files; DONE;Duration:{read_end-read_start};Nrows:{len(result_df)}")
            return result_df


        except Exception as err:
            print("ERROR in reading files "+str(err))



    def insert_to_database(self,dfd):
        try:
            insert_start = datetime.now()
            print(f"Process: Inserting Data into {self.table_name}; Started")
            cursor = self.master_db_connection.cursor(buffered=True)
            print(f"Inserting data to table: {self.table_name}")
            colsname = dfd.columns

            # checking insert into on duplicate key update:
            colsname = tuple(colsname)
            t1 = ''

            for cols in colsname:
                t1 = t1 + f'{cols} = VALUES({cols}), '
            t1 = t1.rstrip(', ')
            len_cols = len(colsname)

            colsname = str(colsname).replace("'", "")

            str_seq = '%s, ' * len_cols
            str_seq = str_seq.rstrip(', ')

            sql_query = f"INSERT IGNORE INTO {self.table_name} {colsname} VALUES ({str_seq}) "
            print("insert query:--")
            print(sql_query)


            tuplelist = [tuple(row) for row in dfd.values.tolist()]

            # Insert in batches of 100
            batch_size = 500
            for i in range(0, len(tuplelist), batch_size):
                batch = tuplelist[i:i + batch_size]
                cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")
                cursor.executemany(sql_query, batch)
                self.master_db_connection.commit()

            insert_end = datetime.now()
            print(f"Process: Insert Data; Done; Duration:{insert_end - insert_start}; Nrows:{len(tuplelist)}")

        except Exception as err:
            print("error in inserting data to df:" + str(err))


    # def create_tables(self):
    #     try:
    #         read_start= datetime.now()
    #         print("Process: read_files; Started;")
    #         csv_file=[file for file in self.input_dir if file.endswith(".csv")]
    #         df=pd.read_csv("MDBColumnDetails.csv")
    #         print(df.columns)
    #         table_creation_query = "CREATE TABLE mdb_data ("
    #         for index, row in df.iterrows():
    #             column_name = row['COLUMN_NAME']
    #             data_type = row['DATA_TYPE']
    #             table_creation_query += f"{column_name} {data_type} DEFAULT NULL,"
    #
    #         table_creation_query = table_creation_query.rstrip(',') + ")"
    #         # cursor.execute(table_creation_query)
    #         print(table_creation_query)
    #
    #         read_end=datetime.now()
    #         print(f"Process:Read files; DONE;Duration:{read_end-read_start}")
    #

    #     except Exception as err:
    #         print("ERROR in reading files"+str(err))


    def run(self):
        try:
            run_start=datetime.now()
            data_from_file=self.read_files()
            self.insert_to_database(data_from_file)
            run_end=datetime.now()
            print(f"Process:Run; Completed; Duration:{run_end-run_start}")
        except Exception as err:
            print("ERROR IN RUN:-"+str(err))



def main():
    mainstart=datetime.now()
    print("STARTING MAIN :")
    read_and_insert_data_mdb().run()
    mainend=datetime.now()
    print(f"Main function completed; Duration:{mainend-mainstart}")
    print("END OF MAIN <<<")

if __name__ == '__main__':
    main()