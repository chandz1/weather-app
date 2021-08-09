import mysql.connector
from mysql.connector import errorcode

dailyData = []

db = mysql.connector.connect(
    host="127.0.0.1", user="root", passwd="37588941", database="WeatherData"
)
if db.is_connected():
    print("Successful")

cursor = db.cursor(buffered=True)

cursor.execute("DROP TABLE IF EXISTS AllData")

try:
    cursor.execute(
        "CREATE TABLE AllData (_date varchar(32) NOT NULL PRIMARY KEY, tempHigh varchar(32), tempLow varchar(32), windSpeed varchar(32), Humidity varchar(32), descrip varchar(64), realFeel varchar(32), precipChance varchar(32));"
    )
except mysql.connector.Error as err:
    # if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
    #     print("Table Already Exists")
    print(err.msg)

file = open("tempData.txt")
dailyData = file.readlines()
for i in range(0, 127, 9):
    cursor.execute(
        "INSERT INTO AllData VALUES (%s,%s,%s,%s,%s,%s,%s,%s);",
        (
            (dailyData[i]).rstrip(),
            (dailyData[i + 1]).rstrip(),
            (dailyData[i + 2]).rstrip(),
            (dailyData[i + 3]).rstrip(),
            (dailyData[i + 4]).rstrip(),
            (dailyData[i + 5]).rstrip(),
            (dailyData[i + 6]).rstrip(),
            (dailyData[i + 7]).rstrip(),
        ),
    )
    db.commit()

cursor.execute("SELECT * from AllData;")
fname = cursor.fetchall()
print(fname)

# cursor.close()
db.close()
