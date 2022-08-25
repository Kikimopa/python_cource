dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
my_list = []
for k, v in dict.items():
    if v >= 3:
        continue
    else:
        my_list.append(k)

for item in my_list:
    dict.pop(item)

print(dict)