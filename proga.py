input_example = '''
Vasja_Jak +3752933333333
Vitja_Mak +375442222222
Tanja_Va +375337777777
'''


# Class of objects
class Customer:
    def __init__(self, name, telephone):
       self.name = name
       self.telephone = telephone
    def __repr__(self):
        return repr((self.name, self.telephone))


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
    list = []
    # Making list of contacts in form of previous class
    for customer in contacts:
        info = customer.split(' ')
        name, phone = info[0], info[1]
        list.append(Customer(name, phone))

    # Sorting and printing the list
    print(sorted(list, key=lambda customer: customer.name))

    # Defining numbers of searches
    for _ in range(int(input())):
        # Feature of choosing specific names
        search_input = input()
        flag = True
        for customer in list:
            if search_input.lower() in customer.name.lower():
                print(customer)
                flag = False
        # If there is nothing suitable
        if flag:
            print('Абонентов на запрос {} не найдено.'.format(search_input))

else:
    print('Invalid format. Please, check out test.txt.')