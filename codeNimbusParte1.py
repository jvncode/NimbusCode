prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print('{}u{}'.format(letter, suffix))
    else:
        print('{}{}'.format(letter, suffix))
