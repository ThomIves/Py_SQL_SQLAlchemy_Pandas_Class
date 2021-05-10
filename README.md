# Py_SQL_SQLAlchemy_Pandas_Class
A Python class that implements SQL, SQLAlchemy, and Pandas to streamline SQL from Python Operations

## Update Considerations:
1. Explore better ways (more elegant ways) to handle table indexing. Perhaps do this without defining a table shema first.
2. Explore standard data cleansing and conditioning techniques for the column names between pandas and SQL to make operations more seemless back and forth.

## Explanation:
First, we import pandas, sqlalchemy, and URL from sqlalchemy.engine. The __init__ method has default values for driver, server, database, and trusted_connection. Within __init__, we build up connection_string. The connection_string is input to the URL.create method along with other parameters as shown. The connection_url is generated and passed as an input to sqlalchemy.create_engine. This return our sqlalchemy engine, which is set as a class attribute.

The table_exists method simply checks to see if the provided table name exists in our database. In summary, this method queries with the query string (qs) shown. This query will return a list of all table names in our database. If it finds an instance of the table name, it returns true. If not, it returns false.

In case you are not familiar with context managers, consider the following

	`with self.engine.connect() as conn:`

The with is followed by a python command and is assigned an alias using `as`. The alias of conn is then used below the context manager along with other code.

Context managers are great for helping us write clean and concise code. They are usually implemented using the with statement. When the block of code indented under a with statement is done, the connection is closed. We encourage you to study context managers when you can. You can even write your own. You will see the above context manager in most of the other methods of this class.

The next method is create_table. We simply pass it a schema string. We extract the table name from this string. If the table already exists, we simply return to the calling code. Then, using our context manager, we connect to the engine. Next, we create the table. Once this code is complete, the context manager closes the engine connection.

Then we have the drop_table method. If there is no table with this name, we return to the calling code. If it does exist, we drop that table using our same context manager.

The insert_df_to_table method shows us the elegance of SQLAlchemy and Pandas working together. Pandas to_sql method accepts our engine connection and uses its own context manager. We also pass in table_name, if_exists="append", and index=False. If the table already exists, we append the dataframe data to the end of the table. We don’t want this Pandas method to use the dataframe’s indices for the SQL table’s indices. We prefer to control this by passing in our own table schema with create table.
 
When we want to query for data from SQL, we use our query_to_df method. We simply pass in our query_string. Then, our connection conn is open by the context manager. Pandas’ read_sql_query method is called with the query string and the engine connection. It returns a dataframe that we then return to the calling code. The engine connection is closed when code within the context manager is complete. 
 
The last method of our class is update_DB, which is passed a command string. We simply use the context manager again to control opening and closing the connection. Once connected we pass in our command for update. Notice how many times we’ve used the following code in the methods. with self.engine.connect() as conn:
            
	    `conn.execute(sqlalchemy.text(<some command string>))`
	    
Truly, each method is performing additional operations before using this general code. If these two lines weren’t so concise, we would have created a private function for these operations. Then, we would call that private function from within each method that uses these lines.
 
We will forego the demonstration of these methods until we use them for some projects below. As stated above, if you are eager to try them now, you can start from Py_Sql_Alchemy_Instance.py.
