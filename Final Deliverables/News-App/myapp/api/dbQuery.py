import ibm_db
# from .dbConfig import getDbCred
from dotenv import dotenv_values

def connecting():
    try:
        data=dotenv_values("D:/IBM/Django-REST-main/myapp/api/.env")
        con = "DATABASE=%s ; HOSTNAME=%s; PORT= %s; SECURITY=%s; SSLServerCertificate=%s; UID=%s; PWD=%s;"%(data["ibm_db_name"],data["ibm_host_name"],data["ibm_port"],data["ibm_security"],data["ibm_certificate"],data["ibm_user_id"],data["ibm_password"])
        connection = ibm_db.connect(con,'','' )
        print("Connected to database!")
        return connection
    except:
        print("Unable to connect!")

def selectQuery(conn,query,params=None):
    try:
        stmt=ibm_db.prepare(conn,query)
        if(params==None):
            ibm_db.execute(stmt)
            data=ibm_db.fetch_assoc(stmt)
            return data
        ibm_db.execute(stmt,params)
        data=ibm_db.fetch_assoc(stmt)
        return data
    except: 
        return False

def insertQuery(conn,query):
    try:
        print("before")
        # stmt=ibm_db.prepare(conn,query)
        server = ibm_db.server_info(conn)
        print("DBMS_NAME",server.DBMS_NAME)
        print("DBMS_VER",server.DBMS_VER)
        print("DB_NAME",server.DB_NAME)
        ibm_db.exec_immediate(conn,query)
        print("Succeeded!")
        return True
    except:
        print("Failed!")
        return False

# conn = connecting()
# user = '5533'
# name = 'abcd'
# fn = 'ab'
# ln = 'cd'
# em = 'abcd@gmail.com'
# ph = '8239492381'
# ps = 'qwerty'
# query = f"INSERT INTO USER(user_id,username,first_name,last_name,email,phone_number,pass_word) values('{user}','{name}','{fn}','{ln}','{em}','{ph}','{ps}');"
# # query = "INSERT INTO USER(user_id,username,first_name,last_name,email,phone_number,pass_word) values('5555','dummy','dummy','1','abcd@gmail.com','9877654312','dummy');"
# insertQuery(conn,query)
