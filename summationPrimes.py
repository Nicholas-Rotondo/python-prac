
# check if tickets can give back change to everyone
def tickets(li):
    total = 0
    # iterate up to but not including the last item
    for value in li[:-1]:
        total += value
    print(total)
    # check if sum of list items are equal to the last list item
    if total == li[-1]:
        print("YES")
    else:
        print("NO")

tickets([25,25,25,25, 100])
tickets([25,25,25, 100])
tickets([25, 100])
tickets([75, 25, 100])
