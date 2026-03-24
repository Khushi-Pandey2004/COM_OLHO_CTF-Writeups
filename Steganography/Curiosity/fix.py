data = open("a.bin","rb").read()

fixed = bytearray()

for i in range(0,len(data),4):
    fixed += data[i:i+4][::-1]

open("flag.png","wb").write(fixed)
