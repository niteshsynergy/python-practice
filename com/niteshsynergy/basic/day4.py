# 4. Loops
print("Loop Control Statements")
print(" i*i : ")
for i in range(1,10):
    print(i,"*",i,"=",i*i)
print("Loop Control Statements")

t=2
print("Table of ",t)
for i in range(1,11):
    print(t,"*",i,"=",t*i)

print("While Control Statements")

w=10
print("Table of ",w)
wi=1
while wi<11:
    print(w,"*",wi,"=",w*wi)
    wi+=1

print("Loop Control Statements")
for i in range(1,11):
    if i%2==0:
        print(i,"*",i,"=",i*i)
    else:
        continue


