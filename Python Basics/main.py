a = 5
print("id(a)",id(a))
a = a+5
print("id(a)",id(a))

a = 3
b = a
a = 5
c=3

print (b is a)

my_set = {a, b, "3"}
my_set.pop()
print(my_set)