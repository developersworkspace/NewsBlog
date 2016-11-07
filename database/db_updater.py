import sqlite3 as lite
from os import listdir
from os.path import isfile, join

def versionTableExist(cursor):
    cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="version"')
    result = cursor.fetchone()
    if (result is None):
        return False

    return True

def getSqlFiles():
    result = [f for f in listdir('sql') if isfile(join('sql', f))]
    result.sort()
    return result


def getSqlFileContent(filePath):
    file = open('sql/' + filePath)
    return file.read()

connection = lite.connect('../test.db')
connection.row_factory = lite.Row
cursor = connection.cursor()
for filePath in getSqlFiles():
    
    r = None
    if (versionTableExist(cursor)):
        cursor.execute('SELECT [version] FROM [version] WHERE [version] = "' + filePath + '"')
        r = cursor.fetchone()
        
    if (r is None):
        print('Executing ' + filePath + '...')
        sql = getSqlFileContent(filePath)        
        cursor.execute(sql)

        cursor.execute('INSERT INTO [version] ([version], [timestamp]) VALUES ("' + filePath + '", 10)')
        print('Inserted ' + filePath)
        
connection.commit()
   
