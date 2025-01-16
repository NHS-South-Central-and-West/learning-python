import numpy

#
# Type assignment
#

a = str("123")
b = float(2)
c = int(1.9) #just throws away the .9; not rounded!
print ('a is a ' + str(type(a))+' with the value ' + str(a))
print ('b is a ' + str(type(b))+' with the value ' + str(b))
print ('c is a ' + str(type(c))+' with the value ' + str(c))

#
# Booleans
#

z = True
print(type(z)) 		#output: <class 'bool'>
print (10>9)		#output: True
print (1 == 2)		#output: False

print(bool(123))	#output: True
print(bool("abc"))	#output: True
print(bool(None))	#output: False
print(bool(0))		#output: False


#
# Numeric types
# 

a = 10  		#int
b = 3   		#int
c = 2.5 		#float
d = -2  		#int
p = numpy.pi 	#float

print(a+b) 			#output: 13, an int
print(a+c) 			#output: 12.5, a float

print(float(a)) 	#output: 10.0
print(int(2.88)) 	#output: 2; just throws away the decimal part

print(round(2.88)) 	#output: 3
print(round(2.88,1))#output: 2.9

#
# Strings
#

str_a = "Hello" #string
str_b = "SCW!"  #string

str_ab = str_a + " " + str_b #python repurposes the "+" to mean string concatenation as well as addition
print(str_ab)                #output: Hello SCW!

print(str_ab.find("SCW"))	 #output:6

str_repeated = str_ab * 3
print(str_repeated)          #output: Hello SCW!Hello SCW!Hello SCW!

print(len(str_a))  			 #output: 5
print(str_a[0])				 #output: H
print(str_a[0:1])			 #output: Hel (give me 3 characters starting at 0)
print(str_a[3:])			 #output: lo (give me everything starting at 3)

#
# Lists
#

fruits = ["banana", "lychee", "raspberry", "apple"]
print(fruits[0]) 		#output: banana (string)
print(fruits[0:2])		#output: ['banana','lychee'] (list!)
print(fruits[-1])		#output: apple (string)

fruits.append("orange")
print(fruits) 			#output: ['banana', 'lychee', 'raspberry', 'apple', 'orange']

print("orange" in fruits) #output: True
print("tomato" in fruits) #output: False

fruits.sort()
print(fruits)			#output: ['apple', 'banana', 'lychee', 'orange', 'raspberry']

mixed_list = ["blue", "green", False, 2, 2.55] #each item in a list can be a different data type!
for item in mixed_list:
	print(type(item)) 	#output:<class 'str'> <class 'str'> <class 'bool'> <class 'int'> <class 'float'>

str_number = "123"
print(type(str_number)) #output:<class 'str'>
str_number=int(str_number)
print(type(str_number)) #output:<class 'int'>

a = 321
print(type(a)) 			#output:<class 'int'>
a = float(a)
print(type(a)) 			#output:<class 'float'>

#b = int("kiwi")			#output: ValueError: invalid literal for int() with base 10: 'kiwi'

#
# Dicts
#
SCW_basic_info={
	"org_code": "0DF",
	"short_name": "SCW CSU",
	"long_name": "NHS South, Central and West Commissioning Support Unit",
	"year_opened": 2014,
	"active":True,
	"postcode":"SO50 5PB"
}

print(type(SCW_basic_info["active"]))		#output: <class 'bool'>
print(type(SCW_basic_info["year_opened"])) 	#output: <class 'int'>

