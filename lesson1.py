print("Hello Python")
print(2+5)
print(2-5)
#if statements

entered_value=input("enter the score")
print(type(entered_value))

if not entered_value.isnumeric():
    print("please enter a value no")
    exit(0)

score = int(entered_value)
if score >=78:
    print("A")
elif 71 <= score <= 77:
    print("A-")
elif 64 <= score <= 70:
    print("B+")
elif 57 <= score <= 63:
    print("B")
elif 50 <= score <= 56:
    print("B-")
elif 43 <= score <= 49:
    print("C+")
else:
    print("try again")