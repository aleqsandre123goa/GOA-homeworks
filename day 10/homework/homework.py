# string - ყველა ბრჭყალებში მოქცეული სიმბოლო
# integer - ყველა მთელი რიცხვი
# float - ყველა ათწილადი
# bool - ლოგიკური ცვლადი რომელსაც მხოლოდ ორი მნიშვნელობა აქვს - true & false
# ////////////////////////////////////////////////////////////////////////////////
# explicit - ეს ნიშნავს მონაცემის ტიპის შეცვლას ხილულად
# implicit - ეს ნიშნავს მონაცემის ტიპის შეცვლას ფარულად
# ////////////////////////////////////////////////////////////////////////////////
# implicit
x = 13
y = x/2
print(y)
x = 15
y = x/2
print(y)
x = 17
y = x/2
print(y)
x = 21
y = x/2
print(y)
x = 23
y = x/2
print(y)
# explicit
name = "aleqsi"
age = "14"
height = "1.73"
weight = "63"
hobby = "drawing"
print(str(name))
print(int(age))
print(float(height))
print(str(weight))
print(str(hobby))
# ////////////////////////////////////////////////////////////////////////////////
# concatenation - ორი ან მეტი ტექსტური ელემენტის ერთმანეთზე შეერთება
a = "visual_"
b = "studio_"
c = "code"
print(a + b + c)
# ////////////////////////////////////////////////////////////////////////////////
birth_year = 2010
this_year = 2025
age = this_year - birth_year
print(age)
# ////////////////////////////////////////////////////////////////////////////////
name = "aleqsandre"
age = 14
addres = "chiatura"
height = 1.73
weight = 63
print("my name is", name, "i am", age, "years old", "i live in", addres, "i am", height, "cm tall", "i am", weight, "kg")
# ////////////////////////////////////////////////////////////////////////////////