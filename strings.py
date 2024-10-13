#looping through strings(use for in looping with new x-ter eg x, y,z or a, b,c etc)
name= "namalwa"
for a in "name":
    print(a)
    


    
# looping thrgh list, tupple etc
fruits = ["apple" , "orange" , "mango","pawpaw"]
for x in fruits:
    print(x)
    
# the Break statement in loops after print
#exit thew loop if x is manago
fruits = ["apple" , "orange" , "mango" , "pawpaw"]
for x in fruits:
    print(x)
    if x == "mango":
        break
    
#break before print
fruits = ["apple" , "orange" , "mango" , "pawpaw"]
for x in fruits:
    if x == "mango":
        break
    print(x)
    
#slicing a string, get x-ticer from 1 to 4(exclusive 4)
# accessing a given range of x-cters
    x = "hello"
    print(x[1:4])
    
#slice from the start to 3
    x = "hello"
    print(x[:3])
    
 #slice to the end from 2
    x = "hello"
    print(x[2:])
    
#negative indixes
    x = "hello"
    print(x[-3:-1])
    
#modifying strings
#upper case
    x = "hello"
    print(x.upper())
    
#lower case
    x = "HELLO"
    print(x.lower())
    
# Removing whitespace from the beginning of at the end we use (strip())
    b = " am going! "
    print(b.strip())
    
 #Replacing strings
    x = "hello"
    print(x.replace('e','a'))
    
    
#split metthod, 
    x = "come, here" 
    print(x.split(","))
    
 #formatting a string(f-string method)
    weight= 30
    txt=f"Am millia and i weigh {weight} "
    print(txt)
    
# despaying weight with decimal point
    
 #formatting a string(f-string method)
    weight= 30.7779
    txt=f"Am millia and i weigh {weight:.1f}kgs "
    print(txt)
    
#escape x-cters
#The escape character allows you to use double quotes when you normally would not be allowed:
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)


#strings in depth (arrays are lists) and are accessed using indexes
#example
#print character"a" in the name below
name= "grace"
print(name[2])

#print the last x-cter in the name grace
print(name[4])

#loop thrgh
address ="kamokya"
for x in address:
    print(x)
    
#slicing
    x = "hello, here"
    print(x[1:8])
    
x = "hello"
print(x[-4:])
print(x[4:]) 

#add a coma to ur figure(,)
x=5000000
print(f"{x:,}")