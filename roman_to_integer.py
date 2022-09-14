#  IV==4  and  VI==6

roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
rm = input("enter a roman number: ")
num = 0
for i in range(len(rm)-1):
    if roman[rm[i]] < roman[rm[i+1]]:
        num -= roman[rm[i]]
    else:
        num += roman[rm[i]]
num += roman[rm[-1]]
print(num)
        
     
 