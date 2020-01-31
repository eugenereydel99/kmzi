ALPHABET = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z']

LENGTH = len(ALPHABET)

def tabula_recta():
    square = []
    for i in range(LENGTH, 0, -1):
        square.append(ALPHABET[LENGTH-i:] + ALPHABET[:-i])

    return square

def autokey(text, symbol):
    return symbol + text[:len(text)-1]

def encrypt(text, key):
    square = tabula_recta()
    new_text = ''
    for i in range(0, len(text)):
        n = ALPHABET.index(key[i])
        m = ALPHABET.index(text[i])
        new_text += square[n][m]

    return new_text

def decrypt(text, key):
    square = tabula_recta()
    new_text = ''
    for i in range(0, len(text)):
        n = ALPHABET.index(key[i])
        m = ALPHABET.index(text[i])
        new_text += square[-n][m]

    return new_text

text = input("Input your text: ")
symbol = input("Input your symbol: ")
key = autokey(text, symbol)
text = encrypt(text, key)

print("Encrypted text: {}".format(text))

text = decrypt(text, key)

print("Decrypted text: {}".format(text))