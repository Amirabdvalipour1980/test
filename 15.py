my_list = ["apple", "banana", "apple", "orange", "apple", "banana"]

for item in set(my_list):
    count = my_list.count(item)
    print(f"{item}: {count}")