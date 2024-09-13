import pymysql

def mysqlconnect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        port=3306,
        db='assignment_db',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print('db connected')
    return conn


def disconnect (conn):
    conn.close()
    
if __name__ == "__main__":
    mysqlconnect()    
    