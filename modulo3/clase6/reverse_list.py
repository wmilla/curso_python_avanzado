"""
Given a list of strings, write a function that prints a reverse version
of each string:
"""


def magic_function(list):
    new_list = []
    for elem in list:
        new_list.append(elem[::-1])
    return new_list


if __name__ == "__main__":
    list = ["Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
    print(magic_function(list))
