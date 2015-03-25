# Hackday Services

## Overview

This module contains the stubbed services for the hackday.  These are
RESTful JSON services that allow access to 

- Pets

- Species

- Q&A advice for different types of pet

- Tracking

## Running

Best to run this from a Python virtualenv.  To prep the environment:

```
$ virtualenv sandbox
$ . ./sandbox/bin/activate
$ pip install flask
$ pip install flask-restless
$ pip install Flask-SQLAlchemy
$ pip install requests 
``` 

The code can be cloned and run straigh from git:

```
$ git clone <repo>
$ cd repo/src
$ python pets.py
```

This should then startup the services running on port 5000 by default.

## Calling the services

You can play with the services running Postman.  The base URL for all
services is:

```
http://hackday.build.robotnot.org:5000/api
```

### Adding a new species

### Adding a new pet

### Getting a list of all the pets

### Gettiing a single pet

### Getting all the pets for an owner

### Registering a new owner

### Getting all the owners

### Getting Q&A advice for a species

### Getting the tracking data for a pet

### Getting the tracking data for all pets


