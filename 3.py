#program to check for prime numbers
def is_prime(n):
       if n<2:
          return False
       for i in range(2,n//2+1):
              if n % i == 0:
                 return False
       return True

LB=int(input("Enter the lowerbound.:"))
UB=int(input("Enter the upperbound.:"))
for i in range(LB,UB+1):
              if is_prime(i):
                 print(i)

