import os
from psycopg2 import pool
from dotenv import load_dotenv
import hashlib
import uuid

# Load .env file
load_dotenv()

# Get the connection string from the environment variable
connection_string = os.getenv('DB_URL')
salt = os.getenv('SALT')

# Create a connection pool
connection_pool = pool.SimpleConnectionPool(
    1,  # Minimum number of connections in the pool
    10,  # Maximum number of connections in the pool
    connection_string
)

# Check if the pool was created successfully
def is_conn():
    if connection_pool:
        # print("Connection pool created successfully")
        return True
    else:
        return False
    
def hash_pw(password):
    return hashlib.sha256(f'{salt}{password}'.encode("utf-8")).hexdigest()

def verify_login(name,password):
    conn = connection_pool.getconn()
    
    ver_sql = "SELECT password FROM users WHERE user_name = '{}';".format(name)
    
    # try:
    cur = conn.cursor()
    cur.execute(ver_sql)
    res = cur.fetchone()
    
    if res:
        db_pw = res[0]
        if db_pw == hash_pw(password):
            return True
    else:
        return False
    
    # except Exception as e:
        # print(f'Failed to verify the login details : {e}')
        # return "unable to verify!"
        
    # finally:
    cur.close()
    connection_pool.putconn(conn)
        
    
    
def authenticate_user(name,password):
    conn = connection_pool.getconn()
    
    # try:
    cur = conn.cursor()
    cur.execute("SELECT password from users where user_name = '{}';".format(name))
    result = cur.fetchone()
    if result:
        db_pw = result[0]
        # print("db_pw")
        if db_pw == hash_pw(password):
            return True
    else:
        False
    
    # except Exception as e:
        # print(f'failed to authenticate : {e}')
        # return "unable to authenticate!"
        
    # finally:
    cur.close()
    connection_pool.putconn(conn)

def create_table(table_name):
    conn = connection_pool.getconn()
    # try:
    cur = conn.cursor()
    create_table = f'''
            CREATE TABLE IF NOT EXISTS {table_name}(
                uid TEXT PRIMARY KEY,
                user_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        '''

    cur.execute(create_table)
    conn.commit()
    # print(f'created {table_name} table succesfully!')
        
    # except Exception as e:
    #     print(f'Error occurred : {e}')
        
    # finally:
    cur.close()
    connection_pool.putconn(conn)

def insert_user(uid,name,email,password):
    conn = connection_pool.getconn()
    ins_user = '''
            INSERT INTO users VALUES(%s,%s,%s,%s);    
        '''
    
    # try:
    cur = conn.cursor()
    cur.execute(ins_user,(uid,name,email,hash_pw(password)))
    conn.commit()
    # print("User Inserted Successfully!")
        
    # except Exception as e:
    #     return "unable to register! come back later!"
        
    # finally:
    cur.close()
    connection_pool.putconn(conn)

# create_table("users")
# insert_user(uuid.uuid4().hex,"bhuvan","salva12@gmail.com","bhuv123")
# var = authenticate_user("bhuvan","bhuv123")
# print(var)
# var = verify_login("bhuvan","bhuvan123")
# print(var)