from dataclasses import dataclass
import random

names = ['John', 'Jane', 'Jhin', 'Jack', 'Jones', 'Jessica']
surnames = ['Doe', 'Reese', 'Clark', 'Smith', 'Davis', 'Miller']

blacklist = set()

# Generates a random, unique full name.
def generate_random_name():
    name = random.choice(names)
    surname = random.choice(surnames)

    full_name = f'{name} {surname}'

    if full_name in blacklist:
        return generate_random_name()
    
    blacklist.add(full_name)
    
    return full_name

@dataclass
class Employee:
    name: str
    performance: int
    salary: int

    # Creates a random Employee object.
    @classmethod
    def create_random(cls):
        name = generate_random_name()
        performance = random.randint(0, 100)
        salary = random.randint(2500, 10000)

        return cls(name, performance, salary)
