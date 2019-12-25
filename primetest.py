lower = 8
upper = 100
c=0
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if c==5:
       break
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num+(num+1))
           c=c+1
    
