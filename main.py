# list of hard cash notes
notes = [100, 50, 20, 10, 5, 1]

# list of drinks and its price
drinks = {
    1: {
        "name": "Coca Cola",
        "price": "5"
    },
    2: {
        "name": "Sprite",
        "price": "7"
    },
    3: {
        "name": "Milo",
        "price": "15"
    },
    4: {
        "name": "Green Tea",
        "price": "10"
    },
    5: {
        "name": "Ice Lemon Tea",
        "price": "12"
    }
}

# result with amount of notes to return
result = {}


# function to calculate amount of notes to return
def calculate_notes(amount, cash_paid):
    change = cash_paid - amount
    for x in notes:
        counter = 0
        while (change - x) >= 0:
            counter = counter + 1
            result['RM'+str(x)] = counter
            change = change - x


choices = drinks.keys()
while True:
    for key, value in drinks.items():
        print(key, value['name'])
    choice = int(input('Please select a drink\n'))
    if choice in choices:
        break
    else:
        print('Invalid input\n')
        continue

print('You have selected ' + drinks[choice]['name'] + '\nPlease pay RM' + drinks[choice]['price'] + '\n')
cashGiven = int(input('Enter your cash note\n'))
calculate_notes(int(drinks[choice]['price']), cashGiven)
print('\nReturning.....')
print(result)
