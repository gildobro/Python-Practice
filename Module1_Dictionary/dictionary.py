import json
from difflib import get_close_matches

data = json.load(open("Module1_Dictionary/data.json"))

def translate(word):
    #set variable to match lowercases in JSON file
    word = word.lower()
    #if word matches a key in the dictionary, return deffinition
    if (word in data):
        return data[word]
    #if word is similar to a key, ask user to clarify
    elif (len(get_close_matches(word, data.keys())) > 0):
        # %s is a string formatting placeholder
        answer = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(word, data.keys())[0])
        #checks the yes condition
        if (answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes"):
            return data[get_close_matches(word, data.keys())[0]]
        #checks the no condition
        elif (answer == "N" or answer == "n" or answer == "no" or answer == "No"):
            return "Sorry, but the word you are looking for doesn't exist. Please double check it"
        #checks for any random string input
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it"

#word is processed in the parameter of the function above (does not have to match the name of parameter)
word = input("\nEnter a word: ")

#call the function
output = translate(word)

if type(output) == list:
    for item in output:
        print("\nDefinition: ")
        print(item)
else:
    print(output)