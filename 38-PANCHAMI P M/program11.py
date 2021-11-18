file=open('sample.txt','x')
count=0
for line in file:
    if line!="\n":
        count+=1
file.close()
print(count)
