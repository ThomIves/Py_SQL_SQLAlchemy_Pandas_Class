import pandas as pd
import sqlalchemy
from sqlalchemy.engine import URL


class DB_Table_Ops:
    def __init__(self, driver='{SQL Server}', 
                 server='localhost\SQLEXPRESS',
                 database='master',
                 trusted_connection='yes'):
        
        connection_string = f'DRIVER={driver};SERVER={server};'
        connection_string += f'DATABASE={database};'
        connection_string += f'TRUSTED_CONNECTION={trusted_connection}'

        # create sqlalchemy engine connection URL
        connection_url = URL.create(
            "mssql+pyodbc",
            query={"odbc_connect": connection_string})

        self.engine = sqlalchemy.create_engine(connection_url)

    def table_exists(self, table_name):
        qs = f'''select schema_name(t.schema_id) as schema_name,
                    t.name as table_name
                    from sys.tables t
                    order by schema_name,
                    table_name;'''

        with self.engine.connect() as conn:
            cursor = conn.execute(sqlalchemy.text(qs))
            table_exists = [t for t in cursor if table_name == t[1]]
            
            return bool(table_exists)

    def create_table(self, schema_str):
        table_name = schema_str.split()[2]
        if self.table_exists(table_name):
            return
        
        with self.engine.connect() as conn:
            conn.execute(sqlalchemy.text(schema_str))

    def drop_table(self, table_name):
        if not self.table_exists(table_name):
            return

        cs = f'''DROP TABLE {table_name}'''
        with self.engine.connect() as conn:
            conn.execute(sqlalchemy.text(cs))

    def insert_df_to_table(self, df, table_name):
        df.to_sql(table_name, self.engine,
                  if_exists="append", index=False)

    def query_to_df(self, query_string):
        with self.engine.connect() as conn:
            df = pd.read_sql_query(query_string, conn)

            return df

    def update_DB(self, command):
        with self.engine.connect() as conn:
            conn.execute(sqlalchemy.text(command))
