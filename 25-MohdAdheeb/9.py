fname=input("Enter file name: ")
fi=open(fname)
li=fi.readlines()
for i in li:
    print(str.upper(i))
