if __name__ == '__main__':
    names = []
    scores = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    for i in range(0,len(scores)-1):
        for j in range(i+1,len(scores)):
            if(scores[i]>scores[j]):
                temp,temp2 = names[i],scores[i]
                names[i],scores[i] = names[j],scores[j]
                names[j],scores[j] = temp,temp2
    for i in range(0,len(scores)-1):
        if(scores[i]!=scores[i+1]):
            ans.append(names[i+1])
            temp3 = i+1
            break
    i = temp3
    if(i+1!=len(scores)):
        # print(scores)
        # print(i+1)
        # print(len(scores))
        if(scores[i]==scores[i+1]):
            i = i+1
            ans.append(names[i])
            # if(i==len(scores)):
            #     break
    for j in range(0,len(ans)-1):
        for k in range(j+1,len(ans)):
            if(ans[j]>ans[k]):
                temp = ans[j]
                ans[j] = ans[k]
                ans[k] = temp         
    for i in range(0,len(ans)):
        print(ans[i])

     