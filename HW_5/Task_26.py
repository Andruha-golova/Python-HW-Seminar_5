def exp(a, b):
   if b == 0:
      return 1
   return a * exp(a, b - 1)
    
num_1= int(input('Enter number A: '))
num_2 = int(input('Enter number B: '))
print(exp(num_1, num_2))
