a=input("Paragraph:")
b=input("Find:")
c=input("Replace:")
posi=int(input("enter the position to Replace:"))
lists=[]
ci=0
lists=a.split()
for j in range(len(lists)):
    if b==lists[j]:
        ci+=1
        if ci==posi:
            lists[j]=c
s=' '.join(lists)
print(s)