if __name__ == '__main__':
    n = int(input())
    ans = []
    for _ in range(n):
        op, *line = input().split()
        val = list(map(int, line))
        if(op =="remove"):
            ans.remove(val[0])
        elif(op=="pop"):
            del ans[len(ans)-1]
        elif(op=="reverse"):
            ans.reverse()
        elif(op=="append"):
            ans.append(val[0])
        elif(op=="print"):
            print(ans)
        elif(op=="sort"):
            for i in range(0,len(ans)-1):
                for j in range(i+1,len(ans)):
                    if(ans[i]>ans[j]):
                        temp = ans[i]
                        ans[i] = ans[j]
                        ans[j] = temp
        else:
            ans.insert(val[0],val[1])