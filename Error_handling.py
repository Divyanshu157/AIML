# #syntax
# try : 
#     expression
# except Error_name:
#     expression
# finally:
#     expression

a= int(input(" enter num 1 : \n"))
b= (input(" enter num 2 : \n"))

result = 0
try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("check value of b")
    
except StringDivisionError:
     print("b is string") 
finally:
    print("finally is here\n")
    

