import mysql.connector

con = mysql.connector.connect(
user = "root",
password = "G1ly@2001",
host = "localhost",
database = "python_practice"
)

cursor = con.cursor()

#word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM dictionary")#WHERE Expression = '%s' " % word)
results = cursor.fetchall()

print(results)

#if results:
    #for result in results:
        #print(result[])
#else:
    #print("No word found!")

'''
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pn1database"
'''