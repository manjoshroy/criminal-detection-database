import pymysql


def Connect():
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="manjukohli18@",
        database="criminal_database")
    return con