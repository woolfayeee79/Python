#1. Write a function that draws a grid like the following:
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    
def print_beam():
    print('+ - - - - ', end='')

def print_post():
    print('|         ', end='')
#print the posts get output. print anouther +
def print_beams():
    do_twice(print_beam)
    print('+')
    
#print the posts, get the output and add anouther |
def print_posts():
    do_twice(print_post)
    print('|')

def print_grid():
    print_beams()
    do_four(print_posts)
    print_beams()
    do_four(print_posts)
    print_beams()






