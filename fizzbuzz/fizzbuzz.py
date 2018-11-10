
a=[3,3,3]
b=[3,5,5]
total= int(len(a)) + int(len(b))
def Fizzbuzz(a,b): 
    if total % 3 ==0:
       print('fizz') 
    elif total % 5 ==0:
        print('buzz') 
    elif total % 5 ==0 and total % 3==0:
        print('fizzbuzz') 
    else:
        print('Null')   
Fizzbuzz(a,b)
