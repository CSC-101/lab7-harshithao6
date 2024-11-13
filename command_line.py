import sys
import convert

def arg_convert_total(input: list[str]):
    total = 0
    floats = []
    for i in input:
        num = convert.str_to_float(i)
        floats.append(num)
    for i in floats:
        if i is not None:
            total = total +i
    return total

if __name__ == '__main__':
    print(arg_convert_total(sys.argv[1:]))