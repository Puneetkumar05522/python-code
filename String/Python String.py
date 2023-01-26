#multiline String:
#you can assign a multiline string to a variable by using three quotes..
a="""my name is
punit
kumar
nishad"""
print(a)

#String are Arrary....
#In Python, Array are containers which are able to store more than one item at the same time.
#Square bracket[] can be use to access of the string
a="Hello,Punit"
print(a[1])
#Looping Through a String
#for x in "Banana":
#    print(x)

#String Length:
#To get the length of string, use the len() function.
#The the total number of characters present in it.
a="Hello,World!"
print(len(a))

#Looping Through a String:
#for x in "Hello,World!":
#    print(x)


#    Or
str="Punitkumar"
for a in str:
    print(a)

#   or
str="DeepakKumar"
n=len(str)
for i in range(n):
    print(str[i])

#String Length....len()
a="hello,World"
print(len(a))

#Check String
txt="The best things in the life are free!"
print("free!" in txt)

#Use it in an if statement:
txt="The best things in life are free!"
if "free" in txt:
    print("Yes,'free' is present.")

#Check if Not;
txt="The best thing in life are free!"
print("punit" not in txt)

#Use it in an if Statement:
txt="The best things in life are free!"
if "punit" not in txt:
    print("No,'punit' is not present.")

#Slicing String:
#Get the character from position 2 to position 5 (not included):
b="helloWorld!"
print(b[2:5])

#Slice form start.
b="Hello,World"
print(b[:5])

#Slice to end ..
a="hello,World"
print(a[5:])

#Negative Indexing...
#Get the character from:'0' in 'World!' (position -5) but not include: 'd' in 'World!'(position -2)

a="Hello,World!"
print(a[-5:-2])

#Modify string...
#Upper Case..
a="hello,world!"
print(a.upper())

#Lower Case..
a="Hello,World!"
print(a.lower())

#Remove whitespace..
a="Hello,World!"
print(a.strip())

#Replace String..using replace() function.
a="hello,World!"
print(a.replace("h","A"))
print(a.replace("W","Z"))

#Concatenate String..using '+' opreator.
a="punit"
b="kumar"
c="nishad"
d=a+"  "+b+"  "+c
print(d)

#String Formate...We can use string and number using formate() method...
age=24
txt="My name is puneet,and i am {}"
print(txt.format(age))

quantity=5
itemno=500
price=200
myorder="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))


















































    
