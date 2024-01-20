set1=set()
set2=set()
str1=input("Enter elements for set 1:")
str2=input("Enter elements for set 2:")

for i in str1.split(','):
    set1.add(i)

for j in str2.split(','):
    set2.add(j)

intersect=set1.intersection(set2)

print(set1)
print(set2)

if intersect==set():
    print("No common values")
else:
    print(intersect)
