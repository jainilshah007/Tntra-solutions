size=int(input("enter the lentgh of array"))
arr=[]
for i in range(size):
    arr.append(int(input("Enter the Values–>")))
    arr.sort()
print("the smallest value",min(arr),"the gretaes value",max(arr))