def print_formatted(number):
    maximum = len(str(bin(number)[2:]))

    def format_string(item):
        return str(item).upper().rjust(maximum, " ")

    for i in range(1, number + 1):
        num = format_string(i)
        octo = format_string(oct(i)[2:])
        hexo = format_string(hex(i)[2:])
        bino = format_string(bin(i)[2:])
        print(num, octo, hexo, bino)

if __name__ == '__main__':
    number = int(input())
    print_formatted(number)