from dotenv import dotenv_values
def getDbCred():
# connection = ibm_db.connect("DATABASE=bludb ; HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; PORT= 32733; SECURITY=SSL; SSLServerertificate=/Users/pradeep/PycharmProjects/Flask SQLite/certificate.crt; UID=trk06303; PWD=YLyf6RxcgUb1iCcI;",'','' )
    data=dotenv_values("D:/IBM/Django-REST-main/myapp/api/.env")
    dsn_hostname=data["ibm_host_name"]
    dsn_uid=data["ibm_user_id"]
    dsn_pwd=data["ibm_password"]
    # dsn_driver=data["ibm_driver"]
    dsn_certificate=data["certificate"]
    dsn_security=data["security"]
    dsn_database=data["ibm_db_name"]
    dsn_port=data["ibm_port"]
    dsn_protocol=data["ibm_protocol"]
    dsn=(
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};"
        "SSLServerCertificate={8};").format(dsn_database,dsn_hostname,dsn_port,dsn_protocol,dsn_uid,dsn_pwd,dsn_security,dsn_certificate)
    return dsn