# def fib(n):    # write Fibonacci series up to n
#     a, b = 1, 1
#     total = 0
#     while a < n:
#         if a % 2 == 0:
#             total += a
#         a, b = b, a+b
#     print(f"{total}")
#
# fib(5000)


prev, cur = 0, 1
total = 0
newlist = []
while True:
    prev, cur = cur, prev + cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
        total += cur
print(total)
