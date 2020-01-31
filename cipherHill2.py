import numpy as np
from math import *

# создаём ключ
def createKey(alphabet, keyWord):
    keyWordIndex = [alphabet.index(keyWord[i]) for i in range(len(keyWord))]
    keyWordIndex = np.array([keyWordIndex[:]])
    return np.reshape(keyWordIndex, (int(sqrt(len(keyWord))), int(sqrt(len(keyWord)))))

# создаем блоки
def createBlocks (alphabet, plainText, blocks = []):
    for s in plainText:
        index = alphabet.find(s)
        if (index != -1):
            blocks.append(index)
    while ((len(blocks) % 3) != 0):
        blocks.append(len(alphabet) - 1)    # заменяем пустые значение на последний символ алфавита
    blocks = np.array(blocks)
    blocks.shape = (len(blocks) // 3, 3)

    return blocks

# расширенный алгоритм Евклида
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# нахождение обратного числа
def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b
    else:
        return 0

#  функция шифрования
def encrypt(alphabet, message, keyWord, cipherTextIndex = [], cipherText = ""):

    #  нумеруем символы открытого текста
    #messageIndex = [alphabet.index(message[i]) for i in range(len(message))]

    key = createKey(alphabet, keyWord)  # создаем матрицу ключа

    blocks = createBlocks(alphabet, message)

    #  умножение матриц
    for i in range(len(blocks)):
        cipherTextIndex.append(np.dot(blocks[i], key) % len(alphabet))

    #  преобразование индексов в текст
    cipherTextIndex = np.ravel(np.array(cipherTextIndex).tolist())
    for i in range(len(cipherTextIndex)):
        cipherText += alphabet[cipherTextIndex[i]]

    return cipherText

def decrypt(alphabet, message, keyWord, plainTextIndex = [], plainText = ""):

    #  нумеруем символы закрытого текста
    #messageIndex = [alphabet.index(message[i]) for i in range(len(message))]

    key = createKey(alphabet, keyWord)  # создаем матрицу ключа
    detKey = int(round(np.linalg.det(key)))  # детерминант ключа

    # обратный детерминанту элемент по модулю длины алфавита
    x = mulinv(detKey, len(alphabet))

    # создаем матрицу индексов сообщения
    blocks = createBlocks(alphabet, message)

    # находим обратную матрицу
    invMatrix = np.linalg.inv(key) * detKey
    invMatrix = x * invMatrix % len(alphabet)

    invMatrix = np.round(invMatrix).astype(int) # округляем и преобразуем в целочисленный тип

    #  умножение матриц
    for i in range(len(blocks)):
        plainTextIndex.append(np.dot(blocks[i], invMatrix) % len(alphabet))

    #  преобразование индексов в текст
    plainTextIndex = np.ravel(np.array(plainTextIndex).tolist())
    plainTextIndex = [int(round(plainTextIndex[i])) for i in range(len(plainTextIndex))]

    for i in range(len(plainTextIndex)):  #  преобразуем в индексы в буквы
        plainText += alphabet[plainTextIndex[i]]

    return plainText.replace(alphabet[-1],"")


#  функция ввода данных
if __name__== '__main__':

    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя., ?"
    plainText = str(input("Введите исходное сообщение:"))

    # проверка ключевого слова
    while True:

        keyWord = str((input("Введите ключевое слово:")))
        if sqrt(len(keyWord)) != int(sqrt(len(keyWord))) != 1:
            print("Неверный ключ.\n")
        elif np.linalg.det(createKey(alphabet, keyWord) % len(alphabet) == 0):
            print("Детерминант матрицы ключа не должен быть равен нулю.")
        else:
            break


    #enc = encrypt(alphabet, plainText, keyWord)
    dec = decrypt(alphabet, plainText, keyWord)

    print("Зашифрованное сообщение:{}".format(dec))

