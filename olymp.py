def chunk_using_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


n, k = map(int, input().split())
inp = input().split()
numbers = [int(i) for i in inp]
d = {}
l_of_l = list(chunk_using_generators(numbers, k))
for i in range(len(l_of_l)):
    d[i] = min(l_of_l[i])
print(d)
sorted(d, key=d.items())
print(d)
