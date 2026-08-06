number_list=[]

for i in range(5):
    x=int(input("Enter number:"))
    number_list.append(x)

for i in range(1,max(number_list)+1):
    if i not in number_list:
        print("missing number =",i)
