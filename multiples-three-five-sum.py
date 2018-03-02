for num in range(0, 1000):
    if num % 3 == 0 or num % 5 == 0:
        num += num + num
        print(f"{num}")
