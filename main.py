import statistics
lst = []
  

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
  
    lst.append(ele) 
      
print(lst)
x = statistics.mean(lst)
print("Mean is :", x)