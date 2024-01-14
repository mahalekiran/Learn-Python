# # Calculator Program
# print("""Welcome Kiran 
# Create program for Calculator.
# Thank You!!""")
# a=int(input("Add Numbers: "))
# b=56
# print(a+b)
# print("Subtract Numbers: ")
# print(a-b)
# print("Multiply Numbers: ")
# print(a*b)
# print("Divide Numbers: ")
# print(a/b)

# #list and input function
# age=input("Please enter age:")
# print(a>b)
# print(int(age)>35)
names="Kiran","Manisha","Arti","Priti"
names=list(names)
names[3]="Trupti"
print(names)

#Dictionary
student={
    "name":"Kiran",
    "dob":"24-12-1988",
    "subject":"34,35,78"
}
print(student["subject"])

# len function
print(len(names))
#type
print(type(names))
#concat
names1=names+["Advait"]
print(names1)

#insert
#append
#extend
nn=["Chetna"]

names1.insert(1, "Aditi")
names1.append("cHARUL")
print(names1)

nn.extend(names1)
print(nn)

jj=["Prem","Syed","Prachit","Kumar","Kalyan","Niki"]
print(jj[2:6])

# #remove
# #pop
# names1.remove("cHARUL")
# print(names1)
# names1.pop(0)
# print(names1)

# #del class
# del names1[4]
# print(names1)



# #clear
# names1.clear()
# print(names1)

mm=("Firoza","MJ","DG")
m1=list(mm)
m1.append("Diksha")
ll=tuple(m1)
print(ll)

x=ll.index("DG")
y=ll.count("MJ")
print(x,y)


#tuple ordered, (), immutuable
#list ordered, [], mutable
#set unordered, {}, no duplicares allowed
num2=(1,2,3,1,6,9,7,3,3,2)
nums=[1,2,3,1,6,9,7,3,3,2]
nums1={1,2,3,1,6,9,7,3,3,2}
# z=len(nums)
print(num2, nums, nums1)