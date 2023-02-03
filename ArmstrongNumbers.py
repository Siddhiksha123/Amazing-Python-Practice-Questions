# Lets understand what an armstrong number is by an example
# Ex. 153 isan armstrong number if 1^3 + 5^3 + 3^3 = 153  , 3 is the number of digits in 153  

for i in range(10000):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=num%10
        result = result + pow(digit, n)
        i=i//10
        
    if num==result:
        print(num)
        
        


