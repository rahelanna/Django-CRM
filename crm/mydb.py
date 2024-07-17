import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'temes',
    passwd = 'Cokkancs_1946',
    database = 'crm_database',
    auth_plugin = 'mysql_native_password'

)

print("DONE!")



