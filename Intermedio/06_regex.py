import re
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# [(6, 'love'), (5, 'you'), (3, 'can'), (2, 'what'), (2, 'teaching'), (2, 'not'), (2, 'else'), (2, 'do'), (2, 'I'), (1, 'which'), (1, 'to'), (1, 'the'), (1, 'something'), (1, 'if'), (1, 'give'), (1, 'develop'), (1, 'capabilities'), (1, 'application'), (1, 'an'), (1, 'all'), (1, 'Python'), (1, 'If')]

regex_pattern = r'\w+'
# matches = re.findall(regex_pattern, paragraph)

def most_frequent_word(text):
    words_count = {}
    matches = re.findall(regex_pattern, text)
    for match in matches:
        if match in words_count:
            words_count[match] += 1
        else:
            words_count[match] = 1

    return [(count, word) for word, count in sorted(words_count.items(), key=lambda item: item[1], reverse=True)]


print(most_frequent_word(paragraph))


# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned = re.sub(r'[%$@&#;!]', '', sentence) # I am a teacher, and I love teaching. There is nothing as more rewarding as educating and empowering people. I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?

# cleaned = re.sub(r'[^\w ]', '', sentence) # I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(cleaned)