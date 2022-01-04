""" Function to create Dictionary with number of occurences
of each letter in 'Mississippi' """


def occurrences(dict, str):
    for x in str:
        dict[x] += 1
    for x in dict:
        print(x.lower(), 'occurs', dict[x], 'time(s)')


str = 'Mississippi'
list = []
for x in str:
    if x not in list:
        list.append(x)
dict = {key: 0 for key in list}
occurrences(dict, str)
