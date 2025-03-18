import MySQLdb
import settings as set

#functions


@staticmethod
def connectDatabase(usr:str, pwd:str):
    '''
    Function to connect to the MySQL server
    Returns the connection object
    usr : the username of the MySQL server
    pwd : the password of the MySQL server
    '''
    try :
        db = MySQLdb.Connect(
            host=set.HOST,
            port=set.PORT,
            user=usr,
            passwd=pwd
        )
        return db
    except Exception as e:
        print('Error: ', e) #NOTE : Change this to a logger later
        return None




@staticmethod
def showDatabase():
    '''
    Function to show all databases in the MySQL server
    '''
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)

@staticmethod
def showDatabaseData():
    '''
    Function to show all data in a database
    '''
    try :
        cursor.execute("SHOW TABLES")
        for x in cursor:
            print(x)
    except Exception as e:
        print('Error: ', e) #NOTE : Change this to a logger later
        return None

@staticmethod
def showTable(tbl:str) :
    '''
    Function to show ALL data in a table
    tbl : the table to show
    '''
    try :
        cursor.execute("SELECT * FROM " + str(tbl))
        result = cursor.fetchall()
        for x in result:
            print(x)
    except Exception as e:
        print('Error: ', e) #NOTE : Change this to a logger later
        return None

@staticmethod
def selectDatabase(dataBase:str):
    '''
    Function to select a database in the MySQL server
    dataBase : the database to be selected
    '''
    try :
        cursor.execute("USE " + str(dataBase))
        return
    except Exception as e:
        print('Error: ', e) #NOTE : Change this to a logger later
        return None

#main

# Connect to the database
print('Connecting to database...')
db = connectDatabase(set.USERNAME, set.PASSWORD) #NOTE : Change usr and pwd to be user input later
print('Connected to database!')
#create the cursor obj
cursor = db.cursor()
showDatabase()
try : dataBaseSelected = str(input('Enter the database you want to see: '))
except Exception as e:
    print('Error: ', e)
    dataBaseSelected = None
if dataBaseSelected is not None:
    selectDatabase(dataBaseSelected)
    print('Selected database: ', dataBaseSelected)
    showDatabaseData()
else: #NOTE : change to loop back into 'main menu' later
    print('No database selected')
    print('Exiting...')
    exit() #close the connection
try : tableSelected = str(input('Enter the table you want to see: '))
except Exception as e:
    print('Error: ', e) #NOTE : Change this to a logger later
    tableSelected = None
if tableSelected is not None: 
    showTable(tableSelected)
