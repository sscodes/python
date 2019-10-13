a = int(input())
b = int(input())

## Exponent with Arithmetic Operator
## Syntax: base ** exponent
exp = a ** b

## Exponent with Built-in Function
## Syntax: pow(base,exponent)
# exp = pow(a,b)

#function for modular exponentiation i.e., (b^n)%m
## usage pow(b,n,m)
def pow(b,n,m):
  r=1
  while n:
    if n%1:
      r=(r*b)%m
    b=(b*b)%m
    n>>=1
  return r
      

## Using Math Library
# import math
# exp = math.pow(a,b)

print(exp)
