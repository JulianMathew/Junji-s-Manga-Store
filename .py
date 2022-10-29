#Guintu, Julian Mathew M.
#ICT-104
#October 25, 2022

#title page/header
print('-'*69)
print('\t'*2,"    Junji's Manga Store（︶^︶）")
print('-'*69)
print('\t'*3,'Title','\t'*4,'  Price')

print('\n[1]  Chainsaw Man Vol. 2','\t'*4,'₱ 649.00')
print('[2]  Jujutsu Kaisen Vol. 4','\t'*4,'₱ 649.00')
print('[3]  Demon Slayer: Kimetsu No Yaiba Complete Box Set','\t','₱ 11,859.00')
print('[4]  My Hero Academia Vol. 12','\t'*4,'₱ 649.00')
print('[5]  Spy x Family Vol. 5','\t'*4,'₱ 649.00')
print('[6]  Urusei Yatsura Vol. 1','\t'*4,'₱ 1,239.00')
print('[7]  WOTAKOI 2-In-1 Omnibus Vol. 3','\t'*3,'₱ 1,121.00')
print("[8]  Komi Can't Communicate Vol. 9",'\t'*3,'₱ 649.00')
print('[9]  Attack on Titan Vol. 10','\t'*4,'₱ 708.00')
print('[10] Tokyo Ghoul Vol. 8','\t'*4,'₱ 826.00')

print('-'*69)

#products dictionary
products = { '1' : ['Chainsaw Man Vol. 2',649],
             '2' : ['Jujutsu Kaisen Vol. 4', 649],
             '3' : ['Demon Slayer: Kimetsu No Yaiba Complete Box Set', 11859],
             '4' : ['My Hero Academia Vol. 12', 649],
             '5' : ['Spy x Family Vol. 5', 649],
             '6' : ['Urusei Yatsura Vol. 1', 1239],
             '7' : ['WOTAKOI 2-In-1 Omnibus Vol. 3', 1121],
             '8' : ["Komi Can't Communicate Vol. 9", 649],
             '9' : ['Attack on Titan Vol. 10', 708],
             '10' : ['Tokyo Ghoul Vol. 8', 826] }

#getting the order of the customer
orders = []

print('(Note: Only a maximum of 10 products can be ordered per customer.)')
product = int(input('\nInput a number to place an order and type 0 if finished ordering: '))

#receives customer's order until 0 is met
if product != 0:
    for i in range(0,10):
        if product > 10:
            product = int(input('\nOnly values between 1-10 is allowed, type 0 if done ordering: '))
            
        elif product > 0:
            orders.append(product)
            print('You have selected',orders)
            product = int(input('\nInput a number to place an order and type 0 if finished ordering: '))

#sums the total amount
total = 0
for i in orders:
    total += products[f"{i}"][1]
print('\nThe total amount is ₱',format(total,'0.2f'))
print('\n(Note: Only yes or no are allowed to be inputted.)')

#asks the customer if he/she have a student or senior citizen id
question = str(input('Do you have a student or senior citizen ID for a 20% discount? Please type yes or no: '))

while question:
    if question == 'Yes' or question == 'yes':
        disc = total * .20
        print('\nThe discounted total amount is ₱',format(disc,'0.2f'))
        break
    elif question == 'No' or question == 'no':
        disc = (total)
        break
    else:
        question = str(input('\nPlease type yes or no only: '))

#ask the customer to input his/her money for the payment
money = float(input("\nPlease enter the amount of money to confirm your purchase: ₱ "))

while money < disc:
    money = float(input("\nThe deposited money is not enough. Please enter again: ₱ "))
    
#calculates the change of the amount of money
change = money - disc

#prints the receipt
print('\nPrinting receipt....')
print('....')
print('....')
print('....')
print('....')

#title/header of the receipt
print('*'*69)
print('\n','\t'*2,"    Junji's Manga Store（︶^︶）")
print()
print('*'*69)
print('\n','\t'*2,'Title','\t'*5,'  Price')
print()

#prints the chosen product of the customer
for i in orders:
    if i > 9:
        print('1 x',products[f'{i}'][0],'\t'*5,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 8:
        print('1 x',products[f'{i}'][0],'\t'*4,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 6 :
        print('1 x',products[f'{i}'][0],'\t'*3,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 3:
        print('1 x',products[f'{i}'][0],'\t'*4,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i == 3:
        print('1 x',products[f'{i}'][0],'\t','₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 0:
        print('1 x',products[f'{i}'][0],'\t'*4,'₱',format(products[f'{i}'][1],'0.2f'))

print()
print('='*69)
print('\n\tAmount Received: ','\t'*2,'₱',format(money,'0.2f'))
print('\tTotal Amount:','\t'*2,'       -₱',format(disc,'0.2f'))
print('\tChange: ','\t'*3,'₱',format(change,'0.2f'))
print()
print('-'*69)
print("\nThank you for buying at Junji's Manga Store（︶^︶）, have a nice day!")



#Guintu, Julian Mathew M.
#ICT-104
#October 25, 2022

#title page/header
print('-'*69)
print('\t'*2,"    Junji's Manga Store（︶^︶）")
print('-'*69)
print('\t'*3,'Title','\t'*4,'  Price')

print('\n[1]  Chainsaw Man Vol. 2','\t'*4,'₱ 649.00')
print('[2]  Jujutsu Kaisen Vol. 4','\t'*4,'₱ 649.00')
print('[3]  Demon Slayer: Kimetsu No Yaiba Complete Box Set','\t','₱ 11,859.00')
print('[4]  My Hero Academia Vol. 12','\t'*4,'₱ 649.00')
print('[5]  Spy x Family Vol. 5','\t'*4,'₱ 649.00')
print('[6]  Urusei Yatsura Vol. 1','\t'*4,'₱ 1,239.00')
print('[7]  WOTAKOI 2-In-1 Omnibus Vol. 3','\t'*3,'₱ 1,121.00')
print("[8]  Komi Can't Communicate Vol. 9",'\t'*3,'₱ 649.00')
print('[9]  Attack on Titan Vol. 10','\t'*4,'₱ 708.00')
print('[10] Tokyo Ghoul Vol. 8','\t'*4,'₱ 826.00')

print('-'*69)

#products dictionary
products = { '1' : ['Chainsaw Man Vol. 2',649],
             '2' : ['Jujutsu Kaisen Vol. 4', 649],
             '3' : ['Demon Slayer: Kimetsu No Yaiba Complete Box Set', 11859],
             '4' : ['My Hero Academia Vol. 12', 649],
             '5' : ['Spy x Family Vol. 5', 649],
             '6' : ['Urusei Yatsura Vol. 1', 1239],
             '7' : ['WOTAKOI 2-In-1 Omnibus Vol. 3', 1121],
             '8' : ["Komi Can't Communicate Vol. 9", 649],
             '9' : ['Attack on Titan Vol. 10', 708],
             '10' : ['Tokyo Ghoul Vol. 8', 826] }

#getting the order of the customer
orders = []

print('(Note: Only a maximum of 10 products can be ordered per customer.)')
product = int(input('\nInput a number to place an order and type 0 if finished ordering: '))

#receives customer's order until 0 is met
if product != 0:
    for i in range(0,10):
        if product > 10:
            product = int(input('\nOnly values between 1-10 is allowed, type 0 if done ordering: '))
            
        elif product > 0:
            orders.append(product)
            print('You have selected',orders)
            product = int(input('\nInput a number to place an order and type 0 if finished ordering: '))

#sums the total amount
total = 0
for i in orders:
    total += products[f"{i}"][1]
print('\nThe total amount is ₱',format(total,'0.2f'))
print('\n(Note: Only yes or no are allowed to be inputted.)')

#asks the customer if he/she have a student or senior citizen id
question = str(input('Do you have a student or senior citizen ID for a 20% discount? Please type yes or no: '))

while question:
    if question == 'Yes' or question == 'yes':
        disc = total * .20
        print('\nThe discounted total amount is ₱',format(disc,'0.2f'))
        break
    elif question == 'No' or question == 'no':
        disc = (total)
        break
    else:
        question = str(input('\nPlease type yes or no only: '))

#ask the customer to input his/her money for the payment
money = float(input("\nPlease enter the amount of money to confirm your purchase: ₱ "))

while money < disc:
    money = float(input("\nThe deposited money is not enough. Please enter again: ₱ "))
    
#calculates the change of the amount of money
change = money - disc

#prints the receipt
print('\nPrinting receipt....')
print('....')
print('....')
print('....')
print('....')

#title/header of the receipt
print('*'*69)
print('\n','\t'*2,"    Junji's Manga Store（︶^︶）")
print()
print('*'*69)
print('\n','\t'*2,'Title','\t'*5,'  Price')
print()

#prints the chosen product of the customer
for i in orders:
    if i > 9:
        print('1 x',products[f'{i}'][0],'\t'*5,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 8:
        print('1 x',products[f'{i}'][0],'\t'*4,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 6 :
        print('1 x',products[f'{i}'][0],'\t'*3,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 3:
        print('1 x',products[f'{i}'][0],'\t'*4,'₱',format(products[f'{i}'][1],'0.2f'))
    elif i == 3:
        print('1 x',products[f'{i}'][0],'\t','₱',format(products[f'{i}'][1],'0.2f'))
    elif i > 0:
        print('1 x',products[f'{i}'][0],'\t'*4,'₱',format(products[f'{i}'][1],'0.2f'))

print()
print('='*69)
print('\n\tAmount Received: ','\t'*2,'₱',format(money,'0.2f'))
print('\tTotal Amount:','\t'*2,'       -₱',format(disc,'0.2f'))
print('\tChange: ','\t'*3,'₱',format(change,'0.2f'))
print()
print('-'*69)
print("\nThank you for buying at Junji's Manga Store（︶^︶）, have a nice day!")



