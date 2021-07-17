n = int(input())

if n<=1:
    print(n)
    quit()

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n-1):
        c = a + b
        b = c
        a = b
    print(c)

fibonacci(n)