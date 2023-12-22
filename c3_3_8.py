"""input関数での入力を数値として扱う"""
while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')