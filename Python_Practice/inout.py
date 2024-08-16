# Print, Input:
a = input("Enter something: ")
print(a)

# Biến (String, int, bool):
a = 45
b = "HungHa"
c = True

# Toán tử, so sánh:
a ** b  # Lũy thừa a^b
a + b   # Cộng chuỗi
a == b  # So sánh bằng
a != b  # So sánh không bằng
a >= b  # So sánh lớn hơn hoặc bằng
a <= b  # So sánh nhỏ hơn hoặc bằng

# String:
str_a = str(45) + str(100)  # Nối chuỗi
len(b)  # Độ dài của chuỗi
b.lower()  # Chuyển chuỗi về chữ thường
b.upper()  # Chuyển chuỗi về chữ hoa
new_b = b.replace("Hung", "NewName")  # Thay thế chuỗi con

# Array (List, Dictionary):
a = ["lop1", "lop2", "lop3"]
a_new = a.append("lop4")  # Thêm phần tử vào cuối danh sách
a.remove("lop2")  # Xóa phần tử khỏi danh sách
print("lop4" in a)  # Kiểm tra sự tồn tại của phần tử trong danh sách
a.extend(["lop5", "lop6"])  # Mở rộng danh sách với các phần tử khác

b = {"lop1": "thay Hung", "lop2": "co Ha"}
print(b["lop1"])  # Truy cập giá trị trong dictionary
b["lop3"] = "co Lan"  # Thêm cặp key-value mới
del b["lop2"]  # Xóa cặp key-value

# List vs Dictionary:
# Trong List, hai danh sách có thể cộng lại với nhau:
c = a + ["lop7", "lop8"]

# Trong Dictionary, hai dictionary không thể cộng lại với nhau, nhưng có thể hợp nhất:
c = {**b, "lop4": "thay Nam"}

# If, else, elif:
if a < 10:
    print("a nhỏ hơn 10")
elif a == 10:
    print("a bằng 10")
else:
    print("a lớn hơn 10")

# Loop:
# For loop
for i in a:
    print(i)

for i in range(len(a)):
    print(i)

# While loop
while a > 0:
    print(a)
    a -= 1  # Giảm giá trị của a

# Function:
def inchuoi(a, b, c):
    print(f"{a}, {b}, {c}")

inchuoi(1, 2, 3)

# Exception Handling:
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Không thể chia cho 0")
finally:
    print("Khối finally luôn được thực hiện")

# Import Module:
import math
print(math.sqrt(16))  # Tính căn bậc hai

# Lambda Function:
double = lambda x: x * 2
print(double(5))

# List Comprehension:
squares = [x**2 for x in range(10)]
print(squares)

# File Handling:
with open("file.txt", "w") as file:
    file.write("Hello World")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Classes and Objects:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Hung", 30)
p1.greet()

# Generators:
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# Decorators:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Context Managers:
with open("file.txt", "r") as file:
    content = file.read()

# Regular Expressions:
import re
pattern = r"\d+"
result = re.findall(pattern, "There are 2 apples and 5 bananas.")
print(result)
