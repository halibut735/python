import sys

B = {
    4000: 1.38,
    4500: 1.48,
    5000: 1.58,
    5500: 1.69,
    6000: 1.81,
    6500: 1.94,
    7000: 2.10,
    7500: 2.28,
    8000: 2.50,
    8500: 2.76,
    9000: 3.06,
    9500: 3.41,
    10000: 3.83,
    10500: 4.33,
    11000: 4.93
}

def first_forward_difference(k):
    return B[4500 + k * 500 ] - B[4000 + k * 500]

def first_backward_difference(k):
    return B[4000 + k * 500 ] - B[3500 + k * 500]

def second_forward_difference(k):
    return first_forward_difference(k + 1) - first_forward_difference(k)

def second_backward_difference(k):
    return first_backward_difference(k) - first_backward_difference(k - 1)

def Newton_forward(k, t):
    return B[4000 + k * 500] + t * first_forward_difference(k) + t * (t - 1) * second_forward_difference(k) / 2

def Newton_backward(k, t):
    return B[11000] + t * first_backward_difference(k) + t * (t + 1) * second_backward_difference(k) / 2

def main(num):
    k = (num - 4000) / 500
    t = (num - 4000 - k * 500) / 500.0
    if num <= 10500 and num >= 4000:
        print '%.2f' %(Newton_forward(k, t))
    else:
        print '%.2f' %(Newton_backward(14, t - 1))

if __name__ == '__main__':
    main(int(sys.argv[1]))
