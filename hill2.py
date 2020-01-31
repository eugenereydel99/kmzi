import numpy as np
from math import *

# создаём ключ
def createKey(alphabet, keyWord):
    keyWordIndex = [alphabet.index(keyWord[i]) for i in range(len(keyWord))]
    keyWordIndex = np.array([keyWordIndex[:]])
    return np.reshape(keyWordIndex, (int(sqrt(len(keyWord))), int(sqrt(len(keyWord)))))

# создаем блоки
def createBlocks (alphabet, plainText):
    blocks = []
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
def encrypt(alphabet, message, keyWord1, keyWord2, cipherText = ""):

    # создаем ключи
    keys = [createKey(alphabet, keyWord1), createKey(alphabet, keyWord2)]

    blocks = createBlocks(alphabet, message)    # создаем блоки из индексов исходного сообщения

    # генерируем новые ключи
    for i in range(len(blocks)):
        if i==0 or i==1:
            continue
        else:
            key = np.dot(keys[i-1],keys[i-2]) % len(alphabet)
            keys.append(key)

    #  умножение матриц
    cipherTextIndex = []
    for i in range(len(blocks)):
        cipherTextIndex.append(np.dot(blocks[i], keys[i]) % len(alphabet))

    #  преобразование индексов в текст
    cipherTextIndex = np.ravel(np.array(cipherTextIndex).tolist())
    for i in range(len(cipherTextIndex)):
        cipherText += alphabet[cipherTextIndex[i]]

    return cipherText

def decrypt(alphabet, message, keyWord1, keyWord2, plainText = ""):

    # создаем ключи
    keys = [createKey(alphabet, keyWord1), createKey(alphabet, keyWord2)]

    # вычисляем определители матриц ключей
    detKeys = [int(fabs(round(np.linalg.det(keys[0])))), int(fabs(round(np.linalg.det(keys[1]))))]

    # обратные детерминанту элементы по модулю длины алфавита
    x = [mulinv(detKeys[0], len(alphabet)), mulinv(detKeys[1], len(alphabet))]

    blocks = createBlocks(alphabet, message)  # создаем блоки из индексов исходного сообщения

    # заполняем ранее объявленные списки
    for i in range(len(blocks)):
        if i == 0 or i == 1:
            continue
        else:
            key = np.dot(keys[i - 1], keys[i - 2]) % len(alphabet)
            keys.append(key)

            detKeys.append(int(fabs(round(np.linalg.det(keys[i])))))
            x.append(mulinv(detKeys[i], len(alphabet)))

    # находим обратную матрицу
    invMatrix = []
    for j in range(len(blocks)):
        invMatrix.append(
            np.linalg.inv(keys[j]) * detKeys[j] * x[j] % len(alphabet)
        )
        # округляем и преобразуем в целочисленный тип
        invMatrix[j] = np.round(invMatrix[j]).astype(int)

    #  умножение матриц
    plainTextIndex = []
    for k in range(len(blocks)):
        plainTextIndex.append(np.dot(blocks[k], invMatrix[k]) % len(alphabet))

    #  преобразование индексов в текст
    plainTextIndex = np.ravel(np.array(plainTextIndex).tolist())
    plainTextIndex = [int(round(plainTextIndex[i])) for i in range(len(plainTextIndex))]

    for i in range(len(plainTextIndex)):  #  преобразуем в индексы в буквы
        plainText += alphabet[plainTextIndex[i]]

    return plainText.replace(alphabet[-1],"")


#  функция ввода данных
if __name__== '__main__':

    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя., ?"

    while True:
        mode = int(input("Введите режим: 1 - шифрование, 2 - расшифрование, 3 - выйти из программы.\n"))

        # режим шифрования
        if mode == 1:
            plainText = str(input("Введите исходное сообщение:"))

            while True:
                keyWord1 = str((input("Введите первое ключевое слово:")))
                keyWord2 = str((input("Введите второе ключевое слово:")))
                if sqrt(len(keyWord1)) != int(sqrt(len(keyWord1))) != 1:
                    print("Неверный первый ключ.\n")
                elif sqrt(len(keyWord2)) != int(sqrt(len(keyWord2))) != 1:
                    print("Неверный второй ключ.\n")
                elif np.linalg.det(createKey(alphabet, keyWord1) % len(alphabet) == 0):
                    print("Детерминант матрицы ключа не должен быть равен нулю.")
                elif np.linalg.det(createKey(alphabet, keyWord2) % len(alphabet) == 0):
                    print("Детерминант матрицы ключа не должен быть равен нулю.")
                elif mulinv(int(fabs(np.linalg.det(createKey(alphabet,keyWord1)))), len(alphabet)) == 0:
                    print("Детерминант матрицы ключа должен быть взаимно простым с длиной алфавита.")
                elif mulinv(int(fabs(np.linalg.det(createKey(alphabet,keyWord2)))), len(alphabet)) == 0:
                    print("Детерминант матрицы ключа должен быть взаимно простым с длиной алфавита.")
                else:
                    break

            enc = encrypt(alphabet, plainText, keyWord1, keyWord2)
            print("Зашифрованное сообщение:{}\n".format(enc))

        # режим расшифрования
        elif mode == 2:
            cipherText = str(input("Введите зашифрованное сообщение:"))

            # проверка ключевого слова
            while True:
                keyWord1 = str((input("Введите первое ключевое слово:")))
                keyWord2 = str((input("Введите второе ключевое слово:")))
                if sqrt(len(keyWord1)) != int(sqrt(len(keyWord1))) != 1:
                    print("Неверный первый ключ.\n")
                elif sqrt(len(keyWord2)) != int(sqrt(len(keyWord2))) != 1:
                    print("Неверный второй ключ.\n")
                elif np.linalg.det(createKey(alphabet, keyWord1) % len(alphabet) == 0):
                    print("Детерминант матрицы ключа не должен быть равен нулю.")
                elif np.linalg.det(createKey(alphabet, keyWord2) % len(alphabet) == 0):
                    print("Детерминант матрицы ключа не должен быть равен нулю.")
                elif mulinv(int(fabs(np.linalg.det(createKey(alphabet,keyWord1)))), len(alphabet)) == 0:
                    print("Детерминант матрицы ключа должен быть взаимно простым с длиной алфавита.")
                elif mulinv(int(fabs(np.linalg.det(createKey(alphabet,keyWord2)))), len(alphabet)) == 0:
                    print("Детерминант матрицы ключа должен быть взаимно простым с длиной алфавита.")
                else:
                    break

            dec = decrypt(alphabet, cipherText, keyWord1, keyWord2)
            print("Расшифрованное сообщение:{}\n".format(dec))

        # режим выхода из программы
        elif mode == 3:
            break
        else:
            print("Такого режима нет в списке!")
            continue