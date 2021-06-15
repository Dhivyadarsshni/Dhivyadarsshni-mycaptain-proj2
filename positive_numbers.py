user_list=[]
input_values=input("enter elements separated by space: ") #enter integers by space
print("\n") 
user_list=input_values.split()
print("list",user_list)                                   #it will displays the result

for i in range(len(user_list)):
    user_list[i]=int(user_list[i])                         #changes into integer

for i in user_list:
    if i>=0:                                               #checks whether it is positive
        print(i,end=" ")                                   #prints positive numbers
