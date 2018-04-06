
#a funtion object is a value you can assign to a veriable or pass as an argument

#def do_twice(f):
#    f()
#    f()
#Here’s an example that uses do_twice to call a function named print_spam twice.

#def print_spam():
#   print'spam'
#do_twice(print_spam)

#1)type this example into the script and test   

def do_twice(f):
    f()
    f()

def print_spam():
    print ('spam')

do_twice(print_spam)

# 2. Modify do_twice so that it takes two arguments, a function object and
# a value, and calls the function twice, passing the value as an argument.


def do_twice(f, arg):
    f(arg)
    f(arg)

# 3.Copy the definition of print_twice from earlier in this chapter to your script    

def print_twice(arg):
    print(arg)
    print(arg)
#4.Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
#argument.

do_twice(print_twice, 'spam')

#5.Define a new function called do_four that takes a function object and a value and calls the
#function four times, passing the value as a parameter. There should be only two statements in
#the body of this function, not four.

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)
    
#print the function    

do_four(print_twice, 'spam')


      
      
