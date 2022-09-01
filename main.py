from db_connect import send_sql_to_db,conn_info,sql_insert_robobet,sql_update_robobet,create_database
import time
from parser import create_df_robobet

def main():
    while True:
        df_robobet = create_df_robobet()
        send_sql_to_db(conn_info=conn_info,sql=sql_insert_robobet,dataframe=df_robobet)
        send_sql_to_db(conn_info=conn_info,sql=sql_update_robobet,dataframe=df_robobet)
        print('Функции запустились')
        time.sleep(600)
if __name__ == '__main__':
    create_database()
    main()