#a = float(input("введите число:"))
#b = float(input("введите (2) число:"))
#i = (a*b)/2
#print(float(i))


#a = float(input("Введите число"))
#b =(a-32)/9*5
#print(float(b))


#a = float(input("введите число"))
#if a<=2:5
#    print(a*10.5)
#else:
    #print(21+((a-2)*4))

#a = str(input("введите слово"))
#if "синий" in a:
   # print("YES")
#else:
    # print("NO")


a = str(input("Введите город:"))
b = str(input("Введите город:"))
c = str(input("Введите город:"))

print(min(a, b, c, key=len), max(a, b, c, key=len))
