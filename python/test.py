# char1,char2 = 'abc','bcd'
# if(char1<char2):
#     print("hii")
# else:
#     print("bye")


def print_formatted(n):
    width = len(bin(n)[2:])
    for i in range(1,n+1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))
    # for i in range(1,n+1):
    #     print(i,oct(i).lstrip('0o'),hex(i).upper().lstrip('0X'),bin(i).lstrip('0b'))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)