list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']

# name = list_of_names[0]
# Choose a function name that clearly describes what the function does
def find_names_starting_with(first_letter, names): 
    result = []
    for name in names:
        if name[0] == first_letter:
            result.append(name)
    return result

def find_names_of_length(length_of_name, names):
    result = []
    for name in names:
        if len(name) == length_of_name:
            result.append(name)
    return result


# Calling the function below
names_p = find_names_starting_with("P", list_of_names)
print(names_p)

names_a = find_names_starting_with("A", list_of_names)
names_a_5 = find_names_of_length(5, names_a)

print(names_a_5)
