def encode(phrase):  # Ryan
    phrase_list = list(phrase)
    print(phrase_list)
    for index in range(0, len(phrase)):
        value = phrase_list[index]
        value += 3
        if len(value) == 2:
            value -= 10
        phrase_list[index] = value
    "".join(phrase_list)

def decode(phrase):  # Michelle
    pass


def main():
    # looping menu
    option = '1'
    phrase = ''
    while option != '0':
        # print menu
        print('0. Exit')
        print('1. Enter a new phrase')
        print('2. Print encoded phrase')
        print('3. Print decoded phrase')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
        elif option == '2':
            print('Encoded phrase is', encode(phrase))
        elif option == '3':
            print('Decoded phrase is', decode(phrase))

