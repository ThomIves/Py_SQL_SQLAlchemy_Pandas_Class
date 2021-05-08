import pandas as pd
from Py_Sql_Alchemy_Class import DB_Table_Ops


d = {'value_1': [1, 2], 'value_2': [3, 4]}
df = pd.DataFrame(data=d)

schema_str = '''CREATE TABLE table_one (
    ident int IDENTITY(1,1) PRIMARY KEY,
    value_1 int NOT NULL,
    value_2 int NOT NULL);'''

update_cmd = '''UPDATE table_one
    SET value_1 = 7, value_2 = 10
    WHERE ident = 3;'''

dbto = DB_Table_Ops()

print(dbto.table_exists('table_one'))
dbto.create_table(schema_str)
print(dbto.table_exists('table_one'))

if True:
    dbto.insert_df_to_table(df, 'table_one')
    dbto.insert_df_to_table(df, 'table_one')
    dbto.update_DB(update_cmd)
    
query_string = 'SELECT * FROM table_one'
print(dbto.query_to_df(query_string))

dbto.drop_table('table_one')
print(dbto.table_exists('table_one'))
