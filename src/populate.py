import requests
import json

url_species = 'http://localhost:5000/api/species'
headers = {'Content-Type': 'application/json'}

allspecies = [ 
    '{"id": "Cat", "description": "Cute Kittens"}', 
    '{"id": "Dog", "description": "Perfect Puppies"}', 
    '{"id": "Ferret", "description": "Feisty Ferrets"}'
]

for species in allspecies:
    requests.post(url_species, species, headers=headers)

allpets = [ 
    '{"id": "1", "name": "Tiddles", "species": "Cat", "weight": "12", "age": "1", "description": "An ickle fwuffy kitten", "favefood": "Sardines", "favetoy": "Catnip mouse"}',
    '{"id": "2", "name": "Tiger", "species": "Cat", "weight": "10", "age": "5", "description": "A tough tomcat", "favefood": "Mice", "favetoy": "Laser pointer toy"}',
    '{"id": "3", "name": "Sheba", "species": "Cat", "weight": "11", "age": "8", "description": "A dignified moggy", "favefood": "Bacon", "favetoy": "Ball of string"}',
    '{"id": "4", "name": "Butcher", "species": "Dog", "weight": "43", "age": "4", "description": "A Yorkshire terrier", "favefood": "Roast beef and Yorkshire pudding", "favetoy": "Frisbee"}',
    '{"id": "5", "name": "Rover", "species": "Dog", "weight": "32", "age": "8", "description": "A daft, bouncy Labrador", "favefood": "Sausages", "favetoy": "Tennis Ball"}',
    '{"id": "6", "name": "Spot", "species": "Dog", "weight": "38", "age": "5", "description": "A scruffy scamp", "favefood": "Kebabs", "favetoy": "A stick"}'
]

url_pets = 'http://localhost:5000/api/pet'
for pet in allpets:
    requests.post(url_pets, pet, headers=headers)
