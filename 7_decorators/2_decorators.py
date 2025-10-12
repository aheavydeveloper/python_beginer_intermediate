#Now that we have understanding of passing function as param or returning function as a result we can  use those concepts in decorators
#suppose we want to create or add more functinlaliyt to an existing method or function ,w e can use decorators
#let us see the conceppt
from jinja2.lexer import newline_re


def new_decorator(original_fun):
    def wrap_fun():
        print('\texecuting tasks , before the original fun')
        original_fun()
        print('\tdoing some after math here')
    return  wrap_fun

def func_needs_decorator():
      print("i want to be a decorated")

final_fun=new_decorator(func_needs_decorator)
final_fun()


#insted of pasing the fun to the function ourself  we can use a @ operator ( a special syntax) that will do the job for us
print('\n\n')
@new_decorator #here this will take the bellow function pass it to the mentioned function and return the result from the new function
#whenever this function is called
def func_needs_decorator_2():
    print("i want to be a decorated")
func_needs_decorator_2()

