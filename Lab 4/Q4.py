#Write a program to find linear search in a list.
n=int(input("Enter a range of number: "))
list1=[]
for i in range(0,n):
    ele=int(input("Enter a number:"))
    list1.append(ele)
l=len(list1)
def search(list1,l,key):
    for i in range(0,l):
        if list1[i]==key:
            print("element found")
            print("At position ",i)
            break
key=int(input("Enter a number to be searched:"))
search(list1,l,key)

