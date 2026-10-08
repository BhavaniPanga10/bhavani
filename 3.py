prices=[250,1200,750,1800,400,950]
f=list(filter(lambda x:x>=500,prices))
print(f)
m=list(map(lambda x:x-x*10/100,f))
print(m)
