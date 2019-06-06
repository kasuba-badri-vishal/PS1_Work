if __name__ == '__main__':
    t = input()
    t = int(t)
    a,b = [],[]
    for i in range(0,t):
        x,y = input().split()
        a.append(x)
        b.append(y)
    for i in range(0,t): 
        try:
            a[i],b[i] = int(a[i]),int(b[i])
            c = a[i]/b[i]
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(b[i]))
        else:
            print(int(c))