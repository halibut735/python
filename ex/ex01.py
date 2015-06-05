def divide(dividend, divisor):
    alphabet = {chr(a):b for a,b in zip(range(65, 91), range(1, 27))}
    digit_count = 0
    num_dividend = 0

    num_divisor = 0
    for each_char in reversed(dividend):
        num_dividend += alphabet[each_char] * (26 ** digit_count)
        digit_count += 1

    digit_count = 0
    for each_char in reversed(divisor):
        num_divisor += alphabet[each_char] * (26 ** digit_count)
        digit_count += 1

    return num_dividend / num_divisor

def num_to_str(num):
    alphabet = [chr(a) for a in range(65, 91)]
    str = ''
    while(num):
        num -= 1
        str += alphabet[num % 26]
        num /= 26
    print str
    print reversed(str)
    return reversed(str)

if __name__ == '__main__':
    dividend = 'COOLSHELL'
    divisor = 'SHELL'

    print divide(dividend, divisor)
    print num_to_str(divide(dividend, divisor))
