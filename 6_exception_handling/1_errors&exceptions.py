from sys import excepthook
from typing import final

from jinja2.filters import do_sum


def stuff():
    while True:
        try:
           num = int(input("please provide a number :"))
        except OSError:
            print("this is a os error")
        except:
           print('this is any error')
           print("please provide a numer")
           continue
        else:
            print("yeas THank you") #oonly run when ther is no exception
            break
        finally:
             print("i will always run")

stuff()