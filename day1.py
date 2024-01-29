with open("input.txt","r") as txt_file:
    content=txt_file.readlines()
import re
sum=0
for line in content:
    match1=re.search(r'[0-9]+', line)
    match2=re.search(r'[0-9]+',line[::-1])
    first=match1.group()[0]
    last=match2.group()[0]
    single=int(first+last)
    sum+=single
print(sum )
    
