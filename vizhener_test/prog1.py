# создание ключа для первого случая
def createKey(alphabet, message, keyword):
    key = []
    for i in range(len(message)):
        for j in range(len(keyword)):
            if len(key) == len(message):
                break
            key.append(alphabet.index(keyword[j]))
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

    key = createKey(alphabet, cipherText, keyword)

    plainTextIndex = []
    for i in range(len(cipherText)):
        plainTextIndex.append((alphabet.index(cipherText[i]) - key[i] + len(alphabet)) % len(alphabet))

    for i in range(len(plainTextIndex)):
        plainText += alphabet[plainTextIndex[i]]

    return plainText

if __name__ == "__main__":

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'q', 'v', 'w', 'x', 'y', 'z'
    ]

    while True:
        mode = int(input("Введите режим: 1 - шифрование, 2 - расшифрование, 3 - выйти из программы.\n"))

        # режим шифрования
        if mode == 1:
            plainText = str(input("Введите исходное сообщение:")).replace(" ", "")
            keyWord = str(input("Введите ключевое слово:"))

            enc = encrypt(alphabet, plainText, keyWord)
            print("Зашифрованное сообщение:{}\n".format(enc))

        # режим расшифрования
        elif mode == 2:
            cipherText = str(input("Введите зашифрованное сообщение:"))
            keyWord = str(input("Введите ключевое слово:"))

            dec = decrypt(alphabet, cipherText, keyWord)
            print("Расшифрованное сообщение:{}\n".format(dec))

        # режим выхода из программы
        elif mode == 3:
            break
        else:
            print("Такого режима нет в списке!")
            continue