"""
def do_something():
    print("This funciton is not the most interesting one I will ever write!")

def repeat_five_times(thee_function):
    for count in range(5):
        print(f"Function call {count+1}")
        thee_function()

# Note: A string is not callable so inputting a string into the function parameters would yield a traceback
repeat_five_times(do_something)

repeat_five_times(print)

no_var = None

print(type(no_var))
print(no_var)

some_numbers = [4, 6, 34, 1, 5]
output_some = some_numbers.append(100)
print(output_some) # returns None
print(some_numbers)
"""
# Introducing the Contact List Program

agents = [
        {
            "First Name": "Nirvana",
            "Last Name": "Net",
            "Email": "nel@nexus.com",
            "Attributes": ["Compassion", "High Emotional Intelligence", "Systematic Thinking"],
        },
        { 
            "First Name": "Eon",
            "Last Name": "Roark",
            "Email": "eon@nexus.com",
            "Attributes": ["Explorative and Deep Thinking", "Infinite Analysis", "Bliss Joy of Creative exploration"],
        }, 
        { 
            "First Name": "X",
            "Last Name": "Unknown",
            "Email": "x@nexus.com",
            "Status": "unknown but w(p)ondering",
        },
    ]

def add_agent(first_name, last_name):
    agents.append({"First Name": first_name, "Last Name": last_name})


print(agents)

add_agent("Uzar", "Unite")

print(agents)
