import random

# расширенный алгоритм Евклида
def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# нахождение обратного числа
def mulinv(a, b):
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b
    else:
        return 0

def test_Ferma(p):
    for i in range(256):
        a = random.randint(2, p)
        if pow(a, p - 1, p) != 1:
            return 1
    return 0


def gen_key():
    while True:
        p = random.randint(pow(2, 255), pow(2, 256) - 1)
        if test_Ferma(p) == 0:
            break
    while (1):
        q = random.randint(pow(2, 255), pow(2, 256) - 1)
        if test_Ferma(q) == 0:
            break
    n = p * q
    fi = (p - 1) * (q - 1)
    while True:
        while True:
            e = random.randint(10000, 100000)
            if test_Ferma(e) == 0:
                break
        if (fi % e != 0):
            break
    d = mulinv(e, fi)
    key = [e, n, d]
    return key


def encription(num, e, n):
    return (pow(num, e, n))


def decription(num, d, n):
    return (pow(num, d, n))


if __name__ == '__main__':

    # генерация ключа
    key = gen_key()
    e, n, d = key[0], key[1], key[2]
    print("Модуль алгоритма n: {}".format(str(n)))
    print("Открытая экспонента e: {}".format(str(e)))
    print("Закрытая экспонента d: {}\n".format(str(d)))

    # шифрование
    message = int(input('Введите исходное сообщение: '))
    ciphertext = encription(message, e, n)
    print("Зашифрованное сообщение: " + str(ciphertext))

    # расшифрование
    message = input("Введите зашифрованное сообщение:")
    plaintext = decription(int(ciphertext), d, n)
    print("\nРасшифрованное сообщение: " + str(plaintext))
