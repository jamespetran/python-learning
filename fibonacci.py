def fibonacciSeries(max):
    a, b = 0, 1
    while a < max:
        print(a)
        a, b = b, a+b


def main(value):
    fibonacciSeries(value)

main(1000)
