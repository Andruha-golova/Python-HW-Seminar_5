def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b-1)


num_1 = int(input('enter number A: '))
num_2 = int(input('enter number B: '))
print(sum(num_1, num_2))