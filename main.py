#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
data_nato_df = pandas.DataFrame(data)

data_dict = {row.letter:row.code for (index,row) in data_nato_df.iterrows()}
print(data_dict)
print('\n')
word_inputed = input('What is the word you would like to transform into a phonetic code?  ')
word_inputed = word_inputed.upper()
word_inputed_listed = [data_dict[word_inputed[i]] for i in range(len(word_inputed))]
print(word_inputed_listed)
