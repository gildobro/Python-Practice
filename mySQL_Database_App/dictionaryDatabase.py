import mysql.connector
from difflib import get_close_matches
from dictionary import translate

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("\nEnter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print("\nDefinition: ")
        print(item)
else:
    print(output)

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

print(results)


#Why even when I comment this out, I still get [] from no words found?

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")