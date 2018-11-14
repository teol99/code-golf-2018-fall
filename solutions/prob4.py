l={}
p=input()
k=1
f=[]
while(p[0].isalpha()):
 l[p]=0
 k+=1
 p=input()
for i in l:
 c=0
 for j in l:
  a=0
  if(i!=j):
   a=1
   for k in range(min(len(j),len(i))):
    if(i[k]==j[k]):a=0
  c+=a
 l[i]=c
for i in range(k,-1,-1):
 m=[]
 for j in l:
  if(l[j]==i):m.append(j)
 f+=sorted(m)
for i in range(int(p)):print(f[i])