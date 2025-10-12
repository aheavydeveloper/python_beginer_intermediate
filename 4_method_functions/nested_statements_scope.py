my_name = 'khan'

def worker1():
    my_name='gudu'
    print(f'my name insdie worker1 is {my_name}')

def worker2():
    print(f'my name insdie worker2 is {my_name}')

def worker3(name):
    name="changed"
    print(f"name inside worker3 is {name}")
    def inner_worker():
        print(f"         name inside inner_worker is {name}")
    inner_worker()

worker1()
worker2()
worker3(my_name)
print(f'my name in global still is {my_name}')


#now lwt us see what happens if i pass an obj of a list or dictionary
print("\n  \n ==========now seeing ar passing obj======")
my_list = [(1,2) , (3,4) , (4,5)]
def do_stuff(list):
    list.append((9,10))
    list = [('gudu' , 'babulu') ]
    print(f'list insdied do_stuff is : {list}')
do_stuff(my_list)
print(f'list in global is {my_list}')





