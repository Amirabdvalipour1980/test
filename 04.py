import random

a = random.choice(["gheichi" , "kughas" , "sang"])

b = str(input("lotfan harekat khod ra vared konid:"))

if a == "sang" and b == "gheichi" :
   print("a")
elif a == "gheichi" and b == "kughas" :
   print("a")
elif a == "kughas" and b == "sang" :
   print("a")
elif a == b  :
   print("mosavi")
else:
   print("b")