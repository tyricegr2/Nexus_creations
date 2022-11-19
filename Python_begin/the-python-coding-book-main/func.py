def do_something():
    print("This funciton is not the most interesting one I will ever write!")

def repeat_five_times(thee_function):
    for count in range(5):
        print(f"Function call {count+1}")
        thee_function()

repeat_five_times(do_something)

repeat_five_times(print)
