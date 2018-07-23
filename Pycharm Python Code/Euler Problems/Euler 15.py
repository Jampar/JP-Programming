import math as m

def C(n,r):

   ans=m.factorial(n)/(m.factorial(r)*m.factorial(n-r))
   return ans

print(C(9,3))
