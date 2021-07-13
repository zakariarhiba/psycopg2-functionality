

# for DB
import psycopg2   as pg
import informations_DB  as info # to change the DB config go to informations_DB.py




# # insert new item 
# username = 'ali.rhiba'
# password = '84220000'
# try:
#     pgconn = pg.connect( host = info.db_host,database = info.db_name,user = info.db_user, password = info.db_password )
#     cur = pgconn.cursor() 
#     cur.execute("INSERT INTO accounts(username,password) VALUES(%s,%s)",(username,password))
# except (Exception, pg.DatabaseError) as error:
#     print(error)
# else:
#     # commit the changes to the database
#     print("add sucessfly")
#     pgconn.commit()
#     cur.close()
# finally:
#     if pgconn is not None:
#         pgconn.close()





# search 
username = 'zak-rhiba'
password = None

def username_exists(username):
    cur = pgconn.cursor()
    cur.execute("SELECT username,password FROM accounts WHERE username like %s", (username,))
    return cur.fetchone() is not None

# search by item
# try:
#     pgconn = pg.connect( host = info.db_host,database = info.db_name,user = info.db_user, password = info.db_password )
#     cur = pgconn.cursor() 
#     if username_exists(username):
#         cur.execute("SELECT username FROM accounts WHERE username like %s ", (username,))
#         account = cur.fetchall()   
# except (Exception, pg.DatabaseError) as error:
#     print(error)
# else:
#     # commit the changes to the database
#     cur.close()
#     print(account)
# finally:
#     if pgconn is not None:
#         pgconn.close()


# search by multiple items
try:
    pgconn = pg.connect( host = info.db_host,database = info.db_name,user = info.db_user, password = info.db_password )
    cur = pgconn.cursor() 
    cur.execute("SELECT * FROM accounts WHERE username like %s AND password like %s", (username,password))
    account = cur.fetchall()   
except (Exception, pg.DatabaseError) as error:
    print(error)
else:
    # commit the changes to the database
    cur.close()
    print(account)
finally:
    if pgconn is not None:
        pgconn.close()