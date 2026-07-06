def magic_function(list):
    new_list = [x[::-1] for x in list]
    return new_list


list = ["Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
reverse = magic_function(list)
print(reverse)
