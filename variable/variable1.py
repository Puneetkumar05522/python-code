x=5
y='punit'
print(x)
print(y)


#Casting Variable ;
x=str(3)
y=int(3)
z=float(3)

print(x),print(y),print(z)

#Get the Type;
x=10
y='punit'
z=()
a=.1
print(type(x)),print(type(y)),print(type(z)),print(type(a))

#Multi Word Variables Name;
#Camel Case;
myvariablename='punit'
#Pascal Case;
MyVariableName='Deepak'
#Snake Case;
my_variable_name='Amit'
print(myvariablename,MyVariableName,my_variable_name)

#Unpack a Collection;
fruits=["Apple","Banana","Mango","Gauava"]
a,b,c,d=fruits
print(a)
print(b)
print(c)
print(d)

#Global Variable or Keyword;

x="punit kumar"
def myfunc():
    print("my name is",x)
myfunc()

x="Awesome"#.....Thish is knowen as Global Variable...
def myfunc():
    x="fantastic"#.....Thish is knowen as Local Variable...
    print("python is",x)
myfunc()
print("python is",x)

#Global Keyword.....

x="Awesome"

def myfunc():
    global x
    x="fantastic"
myfunc()
print("Python is",x)
























