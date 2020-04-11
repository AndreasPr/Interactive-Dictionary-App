import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yesOrNo = input("Did you mean %s instead? Enter Y if Yes, or N if No: " % get_close_matches(word, data.keys())[0])
        if yesOrNo == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesOrNo == "N":
            return "The word does not exist! Please search another one:"
        else:
            return "We didn't understand your entry."
    else:
        return "The specific word does not exist!"

word = input("Enter the word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
