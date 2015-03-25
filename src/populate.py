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

alltrips = [
    '{"date": "01/01/15", "pet": "1", "lat_start": "5.4",  "long_start": "45.9",  "lat_end": "84.6", "long_end": "88.0",  "distance": "89.7"}',
    '{"date": "01/01/15", "pet": "1", "lat_start": "46.7", "long_start": "4.3",   "lat_end": "10.4", "long_end": "29.4",  "distance": "44.1"}',
    '{"date": "01/01/15", "pet": "1", "lat_start": "18.6", "long_start": "68.3"	  "lat_end": "22.7", "long_end": "18.8",  "distance": "49.7"}',
    '{"date": "02/01/15", "pet": "1", "lat_start": "92.8", "long_start": "6.3",	  "lat_end": "6.6",  "long_end": "61.1",  "distance": "102.2"}',
    '{"date": "02/01/15", "pet": "1", "lat_start": "49.1", "long_start": "34.4",  "lat_end": "35.0", "long_end": "39.8",  "distance": "15.1"}',
    '{"date": "02/01/15", "pet": "1", "lat_start": "79.5", "long_start": "78.5",  "lat_end": "0.4",  "long_end": "25.8",  "distance": "95.1"}',
    '{"date": "01/01/15", "pet": "2", "lat_start": "80.5", "long_start": "76.4",  "lat_end": "48.7", "long_end":   "29.9", "distance":   "56.4"}',
    '{"date": "01/01/15", "pet": "2", "lat_start": "37.5", "long_start": "37.4",  "lat_end": "77.3", "long_end":   "43.0", "distance":   "40.2"}',
    '{"date": "01/01/15", "pet": "2", "lat_start": "83.3", "long_start": "62.0",  "lat_end": "31.0", "long_end":   "29.9", "distance":   "61.3"}',
    '{"date": "02/01/15", "pet": "2", "lat_start": "66.3", "long_start": "41.4",  "lat_end": "59.3", "long_end":   "85.0", "distance":   "44.2"}',
    '{"date": "02/01/15", "pet": "2", "lat_start": "9.7",  "long_start": "82.0",  "lat_end": "3.7", "long_end":   "2.5", "distance":   "79.8"}',
    '{"date": "02/01/15", "pet": "2", "lat_start": "88.3", "long_start": "10.3",  "lat_end": "63.6", "long_end":   "37.5", "distance":   "36.7"}',
    '{"date": "01/01/15", "pet": "3", "lat_start": "44.8", "long_start": "98.6",  "lat_end":   "77.3", "long_end":   "24.3", "distance":   "81.1"}',
    '{"date": "01/01/15", "pet": "3", "lat_start": "77.2", "long_start": "77.7",  "lat_end":   "50.1", "long_end":   "57.7", "distance":   "33.7"}',
    '{"date": "01/01/15", "pet": "3", "lat_start": "54.1", "long_start": "98.7",  "lat_end":   "87.6", "long_end":   "91.6", "distance":   "34.2"}',
    '{"date": "02/01/15", "pet": "3", "lat_start": "36.1", "long_start": "64.9",  "lat_end":   "34.5", "long_end":   "19.4", "distance":   "45.6"}',
    '{"date": "02/01/15", "pet": "3", "lat_start": "26.9", "long_start": "65.5",  "lat_end":   "49.3", "long_end":   "93.2", "distance":   "35.6"}',
    '{"date": "02/01/15", "pet": "3", "lat_start": "6.9",  "long_start": "8.6",   "lat_end":   "78.1", "long_end":   "16.6", "distance":   "71.7"}',
    '{"date": "01/01/15", "pet": "4", "lat_start": "90.6", "long_start": "81.9",  "lat_end":   "19.1", "long_end":   "78.9", "distance":   "71.6"}',
    '{"date": "01/01/15", "pet": "4", "lat_start": "92.2", "long_start": "82.7",  "lat_end":   "16.4", "long_end":   "37.0", "distance":   "88.5"}',
    '{"date": "01/01/15", "pet": "4", "lat_start": "81.4", "long_start": "93.7",  "lat_end":   "61.3", "long_end":   "58.5", "distance":   "40.5"}',
    '{"date": "02/01/15", "pet": "4", "lat_start": "71.4", "long_start": "11.4",  "lat_end":   "16.2", "long_end":   "25.5", "distance":   "56.9"}',
    '{"date": "02/01/15", "pet": "4", "lat_start": "10.1", "long_start": "3.8",   "lat_end":   "17.0", "long_end":   "46.2", "distance":   "43.0"}',
    '{"date": "02/01/15", "pet": "4", "lat_start": "68.7", "long_start": "51.6",  "lat_end":   "65.6", "long_end":   "95.6", "distance":   "44.1"}',
    '{"date": "01/01/15", "pet": "5", "lat_start": "17.1", "long_start": "14.9",  "lat_end":   "88.7", "long_end":   "24.0", "distance":   "72.2"}',
    '{"date": "01/01/15", "pet": "5", "lat_start": "23.4", "long_start": "66.9",  "lat_end":   "40.6", "long_end":   "14.0", "distance":   "55.6"}',
    '{"date": "01/01/15", "pet": "5", "lat_start": "48.8", "long_start": "59.7",  "lat_end":   "93.0", "long_end":   "41.0", "distance":   "48.0"}',
    '{"date": "02/01/15", "pet": "5", "lat_start": "42.4", "long_start": "9.4",   "lat_end":   "78.0", "long_end":   "23.8", "distance":   "38.3"}',
    '{"date": "02/01/15", "pet": "5", "lat_start": "3.1",  "long_start": "39.3",  "lat_end":   "82.3", "long_end":   "74.5", "distance":   "86.7"}',
    '{"date": "02/01/15", "pet": "5", "lat_start": "50.6", "long_start": "98.6",  "lat_end":   "99.9", "long_end":   "60.8", "distance":   "62.1"}',
    '{"date": "01/01/15", "pet": "6", "lat_start": "2.4",  "long_start": "17.0",  "lat_end":   "7.0", "long_end":   "71.0", "distance":   "54.3"}',
    '{"date": "01/01/15", "pet": "6", "lat_start": "68.6", "long_start": "72.5",  "lat_end":   "66.6", "long_end":   "85.7", "distance":   "13.3"}',
    '{"date": "01/01/15", "pet": "6", "lat_start": "87.4", "long_start": "55.3",  "lat_end":   "9.7", "long_end":   "10.8", "distance":   "89.5"}',
    '{"date": "02/01/15", "pet": "6", "lat_start": "22.2", "long_start": "50.3",  "lat_end":   "24.8", "long_end":   "71.0", "distance":   "20.8"}',
    '{"date": "02/01/15", "pet": "6", "lat_start": "10.1", "long_start": "17.8",  "lat_end":   "12.0", "long_end":   "52.5", "distance":   "34.8"}',
    '{"date": "02/01/15", "pet": "6", "lat_start": "27.2", "long_start": "89.9",  "lat_end":   "76.3", "long_end":   "30.3", "distance":   "77.3"}'
]

url_tracking = 'http://localhost:5000/api/tracking'
for trip in alltrips:
    requests.post(url_tracking, trip, headers=headers)

