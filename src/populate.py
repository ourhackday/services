import requests
import json

headers = {'Content-Type': 'application/json'}

allspecies = [ 
    '{"id": "Cat", "description": "Cute Kittens"}', 
    '{"id": "Dog", "description": "Perfect Puppies"}', 
    '{"id": "Ferret", "description": "Feisty Ferrets"}'
]

url_species = 'http://localhost:5000/api/species'
for species in allspecies:
    requests.post(url_species, species, headers=headers)

allowners = [ 
    '{"id": "1", "name": "Alice", "town" : "Altrincham", "age": "21"}',
    '{"id": "2", "name": "Bob", "town" : "Boston", "age": "34"}',
    '{"id": "3", "name": "Charlie", "town" : "Chorley", "age": "55"}',
    '{"id": "4", "name": "Dave", "town" : "Dundee", "age": "67"}'
]

url_owners = 'http://localhost:5000/api/owner'
for owner in allowners:
    requests.post(url_owners, owner, headers=headers)

allpets = [ 
    '{"id": "1", "name": "Tiddles", "species": "Cat", "weight": "12", "age": "1",\
    "description": "An ickle fwuffy kitten", "favefood": "Sardines", "favetoy": "Catnip mouse", "owner": "1"}',
    '{"id": "2", "name": "Tiger", "species": "Cat", "weight": "10", "age": "5",\
    "description": "A tough tomcat", "favefood": "Mice", "favetoy": "Laser pointer toy", "owner": "1"}',
    '{"id": "3", "name": "Sheba", "species": "Cat", "weight": "11", "age": "8",\
    "description": "A dignified moggy", "favefood": "Bacon", "favetoy": "Ball of string", "owner": "2"}',
    '{"id": "4", "name": "Butcher", "species": "Dog", "weight": "43", "age": "4",\
    "description": "A Yorkshire terrier", "favefood": "Roast beef and Yorkshire pudding", "favetoy": "Frisbee", "owner": "3"}',
    '{"id": "5", "name": "Rover", "species": "Dog", "weight": "32", "age": "8",\
    "description": "A daft, bouncy Labrador", "favefood": "Sausages", "favetoy": "Tennis Ball", "owner": "4"}',
    '{"id": "6", "name": "Spot", "species": "Dog", "weight": "38", "age": "5",\
    "description": "A scruffy scamp", "favefood": "Kebabs", "favetoy": "A stick", "owner": "4"}'
]

url_pets = 'http://localhost:5000/api/pet'
for pet in allpets:
    requests.post(url_pets, pet, headers=headers)

alladvice = [
    '{"id": "1", "species": "Dog", "question": "Do I need to feed my dog ?",\
    "answer": "Yes, scientific studies show that this will help your dog to live longer"}',
    '{"id": "2", "species": "Dog", "question": "Is my dogs bark worse than its bite ?",\
    "answer": "No.  Bites are worse than barks.  Far worse."}',
    '{"id": "3", "species": "Cat", "question": "Why does my cat hate me ?",\
    "answer": "It is in all cat DNA to treat humans with disdain.  Please do not feel bad about this."}',
    '{"id": "4", "species": "Cat", "question": "Why does my cat leave half-eaten mice on my living room floor",\
    "answer": "Two reasons: 1) Turned out to not be very hungry after all, 2) For the expression on your face"}'
]

url_advice = 'http://localhost:5000/api/advice'
for advice in alladvice:
    requests.post(url_advice, advice, headers=headers)
