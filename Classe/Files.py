p = open("doc","a")
p.write(", comment tu vas ?")
p.close() 

p = open("doc","r")
print(p.read())