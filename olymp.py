t, answer = int(input()), []
for i in range(t):
    n, k = map(int, input().split())
    index = None
    for j in range(n):
        number = input()
        index = (index ^ int(number, 2)) if index != None else int(number, 2)
    answer.append('NO' if index else 'YES')
print('\n'.join(answer))
