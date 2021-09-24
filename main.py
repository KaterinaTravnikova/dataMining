import csv
import io
import fileinput
import pandas as pd
from matplotlib import pyplot as plt
import re
from collections import Counter
import collections
import string

#  delete commas at the end of each row
with open("sms_spam_corpus.csv", "r") as source:
    reader = csv.reader(source)
    with open("without_commas_at_the_end.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            writer.writerow((r[0], r[1]))

# remove "until, to, u, a, atЭ
df = pd.read_csv('without_commas_at_the_end.csv', encoding='cp1251')
df['v2'] = df['v2'].apply(lambda x: re.sub(r'(?iu)\buntil|to|u|a|at\b', '', x))
df.to_csv('without_commas.csv', index=False)

# remove all not letter symbol
df = pd.read_csv('without_commas.csv', encoding='utf-8')
df['v2'] = df['v2'].apply(lambda x: re.sub(r'[^a-zA-Z\s]+', '', x))
df.to_csv('final.csv', index=False)

# set all file to lower case
for line in fileinput.input("final.csv", inplace=1):
    print(line.lower(), end='')

all_file = pd.read_csv("final.csv")

# get full text of ham rows
ham = all_file[all_file.v1 == "ham"]
ham.to_csv("ham.csv")
with open("ham.csv", "r") as source:
    reader = csv.reader(source)
    with open("ham_words.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            writer.writerow([r[2]])

# csv --> txt
with open('hamwordstxt.txt', "w") as my_output_file:
    with open('ham_words.csv', "r") as my_input_file:
        [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

# frequency of words in ham (type --> dictionary)
frequency = {}
document_text = open('hamwordstxt.txt', 'r')
text_string = document_text.read()
p = re.compile("([a-zA-Z-']+)")
res = p.findall(text_string)
ham_word_frequency = {}
for key in res:
    key = key.lower()
    if key in ham_word_frequency:
        value = ham_word_frequency[key]
        ham_word_frequency[key] = value + 1
    else:
        ham_word_frequency[key] = 1

# frequency of words in ham (type --> csv)
with open('ham_frequency.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["word", "frequency"])
    for key, value in ham_word_frequency.items():
        writer.writerow([key, value])

# get full text of spam rows
spam = all_file[all_file.v1 == "spam"]
spam.to_csv("spam.csv")
with open("spam.csv", "r") as source:
    reader = csv.reader(source)
    with open("spam_words.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            writer.writerow([r[2]])

# csv --> txt
with open('spamwordstxt.txt', "w") as my_output_file:
    with open('spam_words.csv', "r") as my_input_file:
        [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

# frequency of words in spam (type --> dictionary)
frequency = {}
document_text = open('spamwordstxt.txt', 'r')
text_string = document_text.read()
p = re.compile("([a-zA-Z-']+)")
res = p.findall(text_string)
spam_word_frequency = {}
for key in res:
    key = key.lower()
    if key in spam_word_frequency:
        value = spam_word_frequency[key]
        spam_word_frequency[key] = value + 1
    else:
        spam_word_frequency[key] = 1



# frequency of words in spam (type --> csv)
with open('spam_frequency.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["word", "frequency"])
    for key, value in spam_word_frequency.items():
        writer.writerow([key, value])

def get_most_frequent_words ()


sample = pd.read_csv("ham_frequency.csv")
#word = sample[sample.word == "go"]
plt.plot(word.frequency)
plt.xlabel("word")
plt.ylabel("frequency")
plt.show()
# china = sample[sample.country == "China"]
# plt.plot(us.year, us.population / 10**6)
# plt.plot(china.year, china.population / 10**6)
# plt.xlabel("year")
# plt.ylabel("population, mln")
# plt.legend(["us", "china"])
# plt.show()