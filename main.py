'''
This program reads in a text file that shows credit card purchases with date, merchant and expense.
It then converts this to a list of purchases and calculates the amount spent by merchant.
'''

def main():
    bill_dict = read_file('bill2.txt')
    purchase_list = create_purchase_list(bill_dict)
    #print(f'This is purchase_list: {purchase_list}')
    purchase_dict =  sum_purchases(purchase_list)
    print('----------------------')
    print_by_merchant(purchase_dict)

def read_file(file):
    """In this exercise, write a function, passwd_to_dict, that reads from a Unix-style
    “password file,” commonly stored as /etc/passwd, and returns a dict based on it.
    The function passwd_to_dict should return a dict based on /etc/passwd in
    which the dict’s keys are usernames and the values are the users’ IDs."""
    my_dict = {}
    pieces = []
    with open(file) as fileobj:
        for line in fileobj:
            line = line.strip()
            line = line.replace(']','')
            #print(f'line is {line}')
            key, value = line.split('[')
            my_dict[key] = value
    return my_dict

def create_purchase_list(bill_dict):
    purchase_list = []
    for item in bill_dict:
        add_on = bill_dict.get(item)
        add_on = add_on.split('$')
        purchase_list.append(add_on)
    return(purchase_list)

'''
def create_final_dict(bill_dict,purchase_list):
    counter = 0
    for key in bill_dict:
        value = purchase_list[counter]
        bill_dict[key] = value
        counter +=1
    return bill_dict
'''
def sum_purchases(purchase_list):
    purchase_dict = {}
    for item in purchase_list:
        merchant = item[0]
        value = int(item[1])
        if merchant not in purchase_dict:
            purchase_dict[merchant] = value
        else:
            purchase_dict[merchant] +=value
    return purchase_dict

def print_by_merchant(purchase_dict):
    print(f'Purchases by merchant')
    print('----------------------')
    for key in purchase_dict:
        print(f'{key}: ${purchase_dict[key]}')

if __name__ == '__main__':
    main()

# See P
