if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for i in range(0,len(student_marks[query_name])):
        sum = sum + float(student_marks[query_name][i])
    print("%.2f" % (sum/3))