# создание ключа
def createKey(alphabet, message, symbol):
    key = [alphabet.index(symbol)]
    for i in range(len(message)-1):
        key.append(alphabet.index(message[i]))
    return key

# шифрование
def encrypt(alphabet, plainText, keyword, cipherText = ""):

    key = createKey(alphabet, plainText, keyword)

    cipherTextIndex = []
    for i in range(len(plainText)):
        cipherTextIndex.append((alphabet.index(plainText[i]) + key[i]) % len(alphabet))

    for i in range(len(cipherTextIndex)):
        cipherText += alphabet[cipherTextIndex[i]]

    return cipherText

# расшифрование
def decrypt(alphabet, cipherText, keyword, plainText = ""):

    plainTextIndex = []
    for i in range(len(cipherText)):
        plainTextIndex.append((alphabet.index(cipherText[i]) - keyword[i] + len(alphabet)) % len(alphabet))

    for i in range(len(plainTextIndex)):
        plainText += alphabet[plainTextIndex[i]]

    return plainText

if __name__ == "__main__":

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'q', 'v', 'w', 'x', 'y', 'z'
    ]

    text = str(input("Введите исходный текст:"))
    symbol = input("Введите символ для формирования ключа:")

    cipher = encrypt(alphabet, text, symbol)
    print("\nЗашифрованное сообщение: {}".format(cipher))
    plain = decrypt(alphabet, cipher, createKey(alphabet, text, symbol))
    print("\nРасшифрованное сообщение: {}".format(plain))