import pymysql
from sshtunnel import SSHTunnelForwarder
from pytz import timezone 
from datetime import datetime
from socket import gethostname

# Handling Database
class DB():
    def __init__(self):
        self.DATABASE = ""
        self.SSH_USER = ""
        self.SSH_PASSWORD = ""
        self.SSH_HOST = ""
        self.SSH_PORT = 22
        self.USER = ""
        self.PASSWORD = ""

        # Establish an SSH tunnel
        self.server = SSHTunnelForwarder(
            (self.SSH_HOST, self.SSH_PORT),
            ssh_username=self.SSH_USER,
            ssh_password=self.SSH_PASSWORD,
            remote_bind_address=('127.0.0.1', 3306)
        )
        self.server.start()

        # Connect to the MySQL database through the SSH tunnel
        self.db = pymysql.connect(
            host='127.0.0.1',
            port=self.server.local_bind_port,
            database=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD
        )

    # IMP: To ensure that it's connected to Database.
    def checkConnection(self):
        try:
            print("Connected to:", self.db.get_server_info())
        except:
            print("")
            print("Connection to database halted.")

    

    def insertData(self, table, user, state):
        cursor = self.db.cursor()
        now = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')

        
        stateText = ''
        if(state):
            stateText = 'ON'
        else:
            stateText = 'OFF'

        val = (now, user, stateText, gethostname()) # HOST NAME IS THE SYSTEM NAME.
        cursor.execute("INSERT INTO " + table + " (time, user, status, host) VALUES (%s, %s, %s, %s)", val)
        self.db.commit()