for i in range(10, 0, -2):
	print(i)
a = [1, 2, 3, 4]
a[2] = 10
print(a)

b = "Python is cool"
print(b[7:-5])

c = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
print(c.get('friends')[-1].get("name"))

def my_function(counter=89):
	return counter + 1
print(my_function())

def my_function(counter=89):
	print("Counter: {}".format(counter))
my_function(12)

d = 12
if d > 2:
	if d % 2 == 0:
		print("Tech")
	else:
		print("C is fun")
else:
	print("School")
	
print("{:d} Mission street, {}".format(972, "San Francisco"))