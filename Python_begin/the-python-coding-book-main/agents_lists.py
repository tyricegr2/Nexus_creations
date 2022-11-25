# Introducing the Contact List Program

# pprint makes the syntax mor readable in the terminal
#   With dictionaries order of items are not important since they are not sequences
import pprint

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
# Default arguments: Use none
def add_agent(agents_list=[], first_name=None, last_name=None, email=None, **additional_details):
    if agents_list is None:
        agents_list=[]
    # Create the dictionary with the keys that will always be present even if value is None
    data = {"First Name": first_name, "Last Name": last_name, "Email": email}
    # Iterate through the dictionary additional_details and add these attributes to data
    for key, value in additional_details.items():
        data[key] = value
    # Append the dictonary data to the contact list
    agents_list.append(data)

    return agents_list

# Call functino without the agents_list argument, meaning a new list is created

scientists = add_agent(
        first_name="Albert",
        last_name="Einstein",
        subject="Physics",
        quote="Imagination is more important than knowledge",
        )

# Function is now called with the key-word argument agents_list = scientists

scientists = add_agent(
        agents_list=scientists,
        first_name="Alan",
        last_name="Turing",
        subject="Computer Science",
        skills=["programming", "Probability", "cryptography"]
        )
pprint.pprint(scientists)


#add_agent(agents, "Uzar", "Unite")

#agents = add_agent(agents, first_name="Epictetus", email="epic@nexus.com")
#agents = add_agent(agents, first_name="Albert", last_name="Einstein")
#agents = add_agent(agents, first_name="Crystal", last_name="Socrates")
#idol_agents = add_agent(first_name="Malcolm", last_name="X")
#personal_agents = add_agent(first_name="Conscious")


"""
def show_all_agents(*agents_list):
    for agent_li in agents_list: # agents_list is a tuple
        for person in agents_list: # Each agents_list is a list of dictionaries
            print(person) # Therefore person is a dictionary       
show_all_agents(agents)

# Introducing **kwargs
#   Allows for dictionary inputs into function parameters such as 'x = 5'
def kw_something(**kwargs):
    print(kwargs)
    print(type(kwargs))

kw_something(name="Tyrice", age=24, profession="futuristic scientist")
"""
"""
def repeat_message(message, repeats=1):
    # Underscore can be used as an arbitrary replaced for a variable with a for loop
    for _ in range(repeats):
        print(message)

#repeat_message("What if....", 5)
pprint.pprint(idol_friends)

first, *rest, last = [35, 10, 100, 2, 22, 34, 83]

print(first)
print(rest)
print(last)

# args can be any other word such as "words" instead of "args"
# Asterisk (*) Allows for multiple arguments
def count_letters(letter, *args):
    print(args)
    print(type(args))
    number = 0
    for word in args:
        number = number + word.count(letter)
    print(number)

count_letters("x", "nexus")

count_letters("e", "Elen", "We need to have more sense", "Cruelty is inevitable")
"""


