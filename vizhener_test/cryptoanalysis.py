
def createKey(alphabet, message, keyword):
    key = []
    for i in range(len(message)):
        for j in range(len(keyword)):
            if len(key) == len(message):
                break
            key.append(alphabet.index(keyword[j]))
    return key

def encrypt(alphabet, plainText, keyword, cipherText = ""):

    key = createKey(alphabet, plainText, keyword)

    cipherTextIndex = []
    for i in range(len(plainText)):
        cipherTextIndex.append((alphabet.index(plainText[i]) + key[i]) % len(alphabet))

    for i in range(len(cipherTextIndex)):
        cipherText += alphabet[cipherTextIndex[i]]

    return cipherText

def decrypt(alphabet, cipherText, keyword, plainText = ""):

    key = createKey(alphabet, cipherText, keyword)

    plainTextIndex = []
    for i in range(len(cipherText)):
        plainTextIndex.append((alphabet.index(cipherText[i]) - key[i] + len(alphabet)) % len(alphabet))

    for i in range(len(plainTextIndex)):
        plainText += alphabet[plainTextIndex[i]]

    return plainText

if __name__ == '__main__':
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    filename1 = "plaintext.txt"
    keyword = "ключ"

    plaintext = ""
    with open(filename1, "r") as file:
        for line in file:
            plaintext += line
    plaintext = list(plaintext.replace(" ",""))

    # for i in range(len(plaintext)):
    #     plaintext[i] = alphabet.index(plaintext[i])
    # print(plaintext)

    filename2 = open("ciphertext.txt", 'w')
    filename2.write(encrypt(alphabet,plaintext,keyword))
    filename2.close()

    ciphertext = list(encrypt(alphabet, plaintext, keyword))

    # создаем массив, и добавляем в него каждую четвертую букву шифротекста
    test = [ciphertext[i] for i in range(0, len(ciphertext), len(keyword))]
    testString = ''.join(test)
    filename3 = open("test.txt", 'w')
    filename3.write(testString)
    filename3.close()


     # считаем кол-во вхождений буквы
    k = []
    for i in range(len(alphabet)):
        k.append(sum(1 for element in test if element == alphabet[i]))

    # находим индекс совпадений для каждой буквы
    index = []
    for i in range(len(k)):
        l = len(test)*(len(test)-1)
        n = k[i]*(k[i]-1)
        index.append(n/l)
    index = sum(index[i] for i in range(len(index)))
    print(index)

    # разбиваем текст на 5 групп
    group1 = [ciphertext[i] for i in range(0, len(ciphertext), len(keyword))]
    print(group1)
    group2 = [ciphertext[i] for i in range(1, len(ciphertext), len(keyword))]
    print(group2)
    group3 = [ciphertext[i] for i in range(2, len(ciphertext), len(keyword))]
    print(group3)
    group4 = [ciphertext[i] for i in range(3, len(ciphertext), len(keyword))]
    print(group4)


    # находим наиболее часто встречающиеся символы в каждой группе
    groups = [group1, group2, group3, group4]

    words = []
    for i in range(len(groups)):
        max = (0, groups[i][0]) # кортеж для хранения наиболее часто встреч. буквы
        for element in groups[i]:
            count = groups[i].count(element)
            if count > max[0]:
                max = (count, element)
        words.append(max[1])
    print(words)

    # находим расстояния
    distance = []
    for i in range(len(words)):
        distance.append((alphabet.index(words[i])-15 + len(alphabet)) % len(alphabet))

    print(distance)
    key = ""
    for j in range(len(distance)):
        key += alphabet[distance[j]]
    print(key)





