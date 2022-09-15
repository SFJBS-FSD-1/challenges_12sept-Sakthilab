# challenge 1

def digitCount(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

digit = int(input("Enter the number to count: "))
c = digitCount(digit)
print(f"number of digit is: {c}")

"----------------------------------------------------------------------------------------------------"

#challenge 2

def rev(number):
    revs = 0  
    while number > 0: 
        remainder = number % 10  
        revs = (revs * 10) + remainder  
        number = number // 10 
    return revs

 

number = int(input("Enter the integer number: "))
result = rev(number) 
print("The reverse number is : {}".format(result)) 

"----------------------------------------------------------------------------------------------------"

#challenge 3

def fact(n):
    num = 0
    if n == 1:
         num += 1
    else:
        result =  n * fact(n-1)
        num += result
    

n = int(input("Enter the number to factorial: "))
print(f"factorial of {n} is {fact(n)}")

"----------------------------------------------------------------------------------------------------"

#challenge 4

def dicConvert(l1, l2):
    dic = {}
    for i in range(len(l1)):
        key = l1[i]
        value = l2[i]
        dic[key] = value
    return dic      



list1 = ["India" , "England", "Spain"]
list2 = ["Delhi","London","Madrid"]
print(f"result is: {dicConvert(list1, list2)}")


"----------------------------------------------------------------------------------------------------"

#challenge 5

dic1 = {("19.07'53.2", "72.54'51.0"): "Mumbai", ("28.33'34.1", "77.06'16.6"): "Delhi"}
dic2 = {}
for key, value in dic1.items():
    dic = {}
    dic["Latitude"] = key[0]
    dic["longtitude"] = key[1]
    dic2[value] = dic

print(dic2)

"----------------------------------------------------------------------------------------------------"

#challenge 6

def findEven(list):
    sum = 0
    for i in list:
        if i%2 == 0:
            sum += i
    return sum


list = [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
result = findEven(list)
print(f"result is: {result}")

"----------------------------------------------------------------------------------------------------"
