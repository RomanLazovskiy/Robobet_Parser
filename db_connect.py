from config import conn_info
from sqlalchemy import create_engine

# Create table. Adding columns to a table
def create_database():
    try:
        # connect to the database with sqlalchemy engine
        engine = create_engine('postgresql://{user}:{password}@{host}/{db_name}'.format(**conn_info))
        with engine.begin() as connaction:       # the cursor for perfoming database operations
            connaction.execute(
                """ CREATE TABLE robobet(
                    id serial   PRIMARY KEY,
                    event_start_time timestamp,
                    event_league varchar(100),
                    team_1_name varchar(50),
                    team_2_name varchar(50),
                    first_team_percentage varchar(5),
                    draw_percentage varchar(5),
                    second_team_percentage varchar(5),
                    event_forecast varchar(3),
                    first_team_odd double precision,
                    draw_odd  double precision,
                    second_team_odd double precision,
                    event_result varchar(10),
                    CONSTRAINT unique_event UNIQUE (DATE(event_start_time),team_1_name,team_2_name)
                )"""
            )
            print('[INFO] Table creation was successful') 

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connaction:
            connaction.close()    
            print('[INFO] PostgreSQL connection closed') 


def send_sql_to_db(conn_info,sql,dataframe):
    try:
        # connect to the database with sqlalchemy engine
        engine = create_engine('postgresql://{user}:{password}@{host}/{db_name}'.format(**conn_info))

        # Create and replace data in a temp table
        dataframe.to_sql('temp_table', engine, if_exists='replace',index=False)

        with engine.begin() as connaction:     # Insert data or update table.
            connaction.execute(sql)
            print('[INFO] Table update sucessfully')  
        
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connaction:
            connaction.close()    
            print('[INFO] PostgreSQL connection closed')    

sql_insert_robobet = """
    INSERT INTO robobet
    (event_start_time,event_league,team_1_name,team_2_name,
    first_team_percentage,draw_percentage,second_team_percentage,
    event_forecast,first_team_odd,draw_odd,second_team_odd,
    event_result) 
    SELECT event_start_time,event_league,team_1_name,team_2_name,
    first_team_percentage,draw_percentage,second_team_percentage,
    event_forecast,first_team_odd,draw_odd,second_team_odd,
    event_result 
    FROM temp_table AS t
    ON CONFLICT ON CONSTRAINT unique_event DO NOTHING
"""
# Query to update data in a table
sql_update_robobet = """
    UPDATE robobet AS r
    SET
    (event_start_time,event_league,team_1_name,team_2_name,
    first_team_percentage,draw_percentage,second_team_percentage,
    event_forecast,first_team_odd,draw_odd,second_team_odd,
    event_result) =
    (t.event_start_time,t.event_league,t.team_1_name,t.team_2_name,
    t.first_team_percentage,t.draw_percentage,t.second_team_percentage,
    t.event_forecast,t.first_team_odd,t.draw_odd,t.second_team_odd,
    t.event_result) 
    FROM temp_table AS t
    WHERE r.event_start_time = t.event_start_time AND r.team_1_name = t.team_1_name AND r.team_2_name = t.team_2_name
"""