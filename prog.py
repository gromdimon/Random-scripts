from collections import UserDict
from collections import OrderedDict

# function for checking input format
def ch(input_lines):
    for line in input_lines:
        info = line.split(' ')
        if len(info) == 2 and info[0][0].isalpha() and (i.isdigit() for i in info[1][1:]):
            return True
        else:
            return False


# This file has to lie in the folder, where .py file lies
# The file should has format as in the beginning
file = open('test.txt', encoding='utf-8')
contacts = file.read().splitlines()
file.close()


# Applying functions
check = ch(contacts)

if check:
    userl = UserDict()
    # Making list of contacts in form of previous class
    for customer in contacts:
        info = customer.split(' ')
        name, phone = info[0], info[1]
        userl[name] = phone

    # Sorting and printing the list
    sort_list = sorted(userl, key=lambda customer: customer[0])

    # Printing sorted list of contacts
    for name in sort_list:
        print(name, userl[name])

    # Defining numbers of searches
    for _ in range(int(input())):
        # Feature of choosing specific names
        search_input = input()
        flag = True
        for customer in userl:
            if search_input.lower() in customer.lower() or search_input.lower() in userl[customer].lower():
                print(customer, userl[customer])
                flag = False
        # If there is nothing suitable
        if flag:
            print('Абонентов на запрос {} не найдено.'.format(search_input))

else:
    print('Invalid format. Please, check out test.txt.')