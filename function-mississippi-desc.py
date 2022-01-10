""" Function to create Dictionary with number of occurences
of each letter in 'Mississippi' in Descending Order """


def occurrences(dict, str):
    for x in str:
        dict[x] += 1
    desc_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for i in desc_list:
        print(i[0].lower(), 'occurs', i[1], 'time(s)')


str = 'Mississippi'
list = []
for x in str:
    if x not in list:
        list.append(x)
dict = {key: 0 for key in list}
occurrences(dict, str)
