#  Armstrong nubers 
# 153 is a three no. , if 1^3 +5^3 +  3^3 = 153 , then 153 is an armstrong number 

num=input("Enter the number ")
l=len(num)
print(l)
ok=False
n=int(num)
result=0
for i in range(1,l+1):
    a=int(n%10)
    aexp=pow(a,l)
    result=result+aexp
    n=n//10
    
print(result)

if result==n:
    ok=True
    
if ok==True:
    print("Armstrong nuomber")
else:
    print("Not an armstrong number")    