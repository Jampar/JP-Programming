
def OddSeqNum(n):
   n = 3*n+1
   return n
   
def EvenSeqNum(n):
   n = n/2
   return n
   
comi=0
comstartNum=0  

for x in range(1,1000000):
   
   startNum = x
   i = 1
   if startNum % 2 == 0:
      rNum= EvenSeqNum(startNum)
   else:
      rNum = OddSeqNum(startNum)

   while rNum != 1:
         if rNum % 2 == 0:
            rNum=EvenSeqNum(rNum)
            i+=1
         
         else:
            rNum=OddSeqNum(rNum)
            i+=1
      
           
   if i>comi:
      print(comstartNum)
      comi=i
      comstartNum=x
       
    
print(comstartNum)


print("End")
