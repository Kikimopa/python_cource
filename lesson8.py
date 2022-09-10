with open("numbers", "r") as file:
    print(file.read())

with open("numbers", "r") as file:
  file_list = file.readlines()

file_list.reverse()

with open("new_file.txt", "w") as file:
    for line in file_list:
        file.write(line)

with open("new_file.txt", "r") as file:
    print(file.read())






