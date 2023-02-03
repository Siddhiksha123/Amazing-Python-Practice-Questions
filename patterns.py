# 1
# 12
# 123
# 1234


n=int(input("Enter the number of your choice"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ") 
    print()
        
#Check the reference page of print. By default there is a newline character appended to the item
#being printed (end='\n'), and end='' is used to make it printed on the same line.
#And print() prints an empty newline, which is necessary to keep on printing on the next line.
        
# 1
# 22
# 333
# 4444
# 55555

n=int(input("Enter the number of your choice"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ") 
    print()