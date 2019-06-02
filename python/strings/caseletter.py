# 

# def print_full_name(a, b):
#     print("Hello {} {}! You just delved in python".format(a,b))

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


def count_substring(string, sub_string):
    count = string.count('CDC')
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)